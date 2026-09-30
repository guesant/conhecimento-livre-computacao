from collections import Counter
from pathlib import Path

import yaml

MAX_NAV_CHILDREN = 5
OVERVIEW_LABELS = {"visão geral", "overview"}
ALLOWED_COMPOUND_CATEGORIES = {
  "Dados e comunicação",
  "Segurança e confiabilidade",
}


def collect_nav_paths(node, paths):
  if isinstance(node, str):
    if node.endswith(".md"):
      paths.append(Path(node).as_posix())
    return

  if isinstance(node, dict):
    for value in node.values():
      collect_nav_paths(value, paths)
    return

  if isinstance(node, list):
    for value in node:
      collect_nav_paths(value, paths)


def collect_category_labels(node, labels):
  if isinstance(node, dict):
    for label, value in node.items():
      if isinstance(value, (dict, list)):
        labels.append(label)
        collect_category_labels(value, labels)
    return

  if isinstance(node, list):
    for value in node:
      collect_category_labels(value, labels)


def collect_mixed_categories(node, violations, path=()):
  if isinstance(node, dict):
    for label, value in node.items():
      if isinstance(value, list):
        pages = []
        has_categories = False
        for child in value:
          if not isinstance(child, dict):
            continue
          child_label, child_value = next(iter(child.items()))
          if isinstance(child_value, str):
            pages.append((child_label, child_value))
          elif isinstance(child_value, list):
            has_categories = True

        non_index_pages = [
          (child_label, child_value)
          for child_label, child_value in pages
          if child_label.lower() not in OVERVIEW_LABELS
          and Path(child_value).name != "index.md"
        ]
        index_pages = [
          (child_label, child_value)
          for child_label, child_value in pages
          if child_label.lower() in OVERVIEW_LABELS
          or Path(child_value).name == "index.md"
        ]
        if has_categories and (non_index_pages or len(index_pages) > 1):
          violations.append((path + (label,), pages))
        collect_mixed_categories(value, violations, path + (label,))
    return

  if isinstance(node, list):
    for value in node:
      collect_mixed_categories(value, violations, path)


def collect_page_entries(node, entries, parents=()):
  if isinstance(node, dict):
    for label, value in node.items():
      if isinstance(value, str) and value.endswith(".md"):
        entries.append((label, value, parents))
      else:
        collect_page_entries(value, entries, parents + (label,))
    return

  if isinstance(node, list):
    for value in node:
      collect_page_entries(value, entries, parents)


def collect_compound_pages(node, violations, parents=()):
  if isinstance(node, dict):
    for label, value in node.items():
      if isinstance(value, str) and value.endswith(".md"):
        is_compound = "," in label or " e " in f" {label} "
        allowed_prefixes = ("Mapa ", "Comparação")
        if is_compound and not label.startswith(allowed_prefixes):
          violations.append((label, value))
      else:
        collect_compound_pages(value, violations, parents + (label,))
    return

  if isinstance(node, list):
    for value in node:
      collect_compound_pages(value, violations, parents)


def collect_compound_titles(entries, violations, docs_dir):
  allowed_prefixes = ("Mapa ", "Comparação")
  for label, relative_path, parents in entries:
    path = docs_dir / relative_path
    lines = path.read_text(encoding="utf-8").splitlines()
    title = next((line[2:] for line in lines if line.startswith("# ")), "")
    is_compound = "," in title or " e " in f" {title} "
    is_index = path.name == "index.md"
    if is_compound and not is_index and not title.startswith(allowed_prefixes):
      violations.append((label, relative_path, title))


def collect_empty_entries(node, violations, path=()):
  if isinstance(node, dict):
    for label, value in node.items():
      current_path = path + (label,)
      if value in (None, ""):
        violations.append(current_path)
      else:
        collect_empty_entries(value, violations, current_path)
    return

  if isinstance(node, list):
    for value in node:
      collect_empty_entries(value, violations, path)


def collect_wide_categories(node, violations, path=()):
  if isinstance(node, dict):
    for label, value in node.items():
      if isinstance(value, list):
        children = [child for child in value if isinstance(child, dict)]
        navigable = [
          child
          for child in children
          if next(iter(child)).lower() not in OVERVIEW_LABELS
        ]
        if len(navigable) > MAX_NAV_CHILDREN:
          violations.append((path + (label,), len(navigable)))
        collect_wide_categories(value, violations, path + (label,))
    return

  if isinstance(node, list):
    for value in node:
      collect_wide_categories(value, violations, path)


def main():
  repository = Path(__file__).resolve().parent.parent
  config_path = repository / ".config" / "mkdocs.yml"
  config = yaml.load(config_path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
  docs_dir = (config_path.parent / config["docs_dir"]).resolve()

  nav_paths = []
  collect_nav_paths(config["nav"], nav_paths)
  nav_set = set(nav_paths)
  doc_paths = {
    path.relative_to(docs_dir).as_posix()
    for path in docs_dir.rglob("*.md")
    if path.is_file()
  }
  missing = sorted(nav_set - doc_paths)
  orphaned = sorted(doc_paths - nav_set)
  duplicated = sorted(path for path, count in Counter(nav_paths).items() if count > 1)
  category_labels = []
  collect_category_labels(config["nav"], category_labels)
  compound_categories = sorted(
    label
    for label in category_labels
    if ("," in label or " e " in f" {label} ")
    and label not in ALLOWED_COMPOUND_CATEGORIES
  )
  mixed_categories = []
  collect_mixed_categories(config["nav"], mixed_categories)
  compound_pages = []
  collect_compound_pages(config["nav"], compound_pages)
  page_entries = []
  collect_page_entries(config["nav"], page_entries)
  compound_titles = []
  collect_compound_titles(page_entries, compound_titles, docs_dir)
  empty_entries = []
  collect_empty_entries(config["nav"], empty_entries)
  wide_categories = []
  collect_wide_categories(config["nav"], wide_categories)

  if missing:
    print("nav references Markdown files that do not exist:")
    print("\n".join(f"  {path}" for path in missing))
  if orphaned:
    print("Markdown files are not included in nav:")
    print("\n".join(f"  {path}" for path in orphaned))
  if duplicated:
    print("nav includes Markdown files more than once:")
    print("\n".join(f"  {path}" for path in duplicated))
  if compound_categories:
    print("nav contains compound category labels:")
    print("\n".join(f"  {label}" for label in compound_categories))
  if mixed_categories:
    print("nav categories must contain canonical pages or child categories plus one index page:")
    for path, pages in mixed_categories:
      labels = ", ".join(label for label, _ in pages)
      print(f"  {' > '.join(path)}: {labels}")
  if compound_pages:
    print("nav contains compound canonical pages without a map or comparison label:")
    for label, path in compound_pages:
      print(f"  {label}: {path}")
  if compound_titles:
    print("Markdown pages contain compound titles without a map or comparison label:")
    for label, path, title in compound_titles:
      print(f"  {label}: {path} ({title})")
  if empty_entries:
    print("nav contains empty categories or pages:")
    print("\n".join(f"  {' > '.join(path)}" for path in empty_entries))
  if wide_categories:
    print(f"nav categories contain more than {MAX_NAV_CHILDREN} navigable items:")
    for path, count in wide_categories:
      print(f"  {count}: {' > '.join(path)}")

  return (
    1
    if missing
    or orphaned
    or duplicated
    or compound_categories
    or mixed_categories
    or compound_pages
    or compound_titles
    or empty_entries
    or wide_categories
    else 0
  )


raise SystemExit(main())
