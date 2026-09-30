# Datas SQL

Datas representam calendários; timestamps representam instantes. Misturar os dois sem definir fuso, precisão e origem do valor é uma fonte frequente de bugs.

## Valores atuais

```sql
SELECT CURRENT_DATE;
SELECT CURRENT_TIME;
SELECT CURRENT_TIMESTAMP;
```

MySQL também oferece `CURDATE()`, `CURTIME()` e `NOW()`. PostgreSQL possui formas SQL padrão e funções equivalentes. A escolha da função não resolve sozinha o fuso: documente se o valor representa UTC, horário local ou um instante com offset.

## Extrair partes

```sql
SELECT
    EXTRACT(YEAR FROM created_at) AS year,
    EXTRACT(MONTH FROM created_at) AS month,
    EXTRACT(DAY FROM created_at) AS day,
    EXTRACT(ISODOW FROM created_at) AS iso_weekday
FROM events;
```

PostgreSQL também possui `DATE_PART`. MySQL costuma usar `YEAR`, `MONTH`, `DAY`, `WEEKDAY` e funções próprias para o mesmo objetivo:

```sql
SELECT
    YEAR(created_at) AS year,
    MONTH(created_at) AS month,
    WEEKDAY(created_at) AS weekday_number
FROM events;
```

No MySQL, `WEEKDAY` retorna zero para segunda-feira e seis para domingo. Não confunda essa convenção com funções que iniciam a semana no domingo.

## Truncar e agrupar

Para agrupar eventos por mês sem transformar o valor em texto, PostgreSQL oferece `DATE_TRUNC`:

```sql
SELECT
    DATE_TRUNC('month', created_at) AS month,
    COUNT(*) AS total
FROM events
GROUP BY DATE_TRUNC('month', created_at)
ORDER BY month;
```

Em MySQL, é comum construir uma chave com `DATE_FORMAT` ou usar os componentes de data:

```sql
SELECT
    DATE_FORMAT(created_at, '%Y-%m-01') AS month,
    COUNT(*) AS total
FROM events
GROUP BY DATE_FORMAT(created_at, '%Y-%m-01');
```

O resultado formatado é texto. Se a consulta precisar de ordenação e comparação temporal em várias etapas, mantenha uma expressão de data ou um intervalo explícito.

## Intervalos

PostgreSQL:

```sql
SELECT created_at + INTERVAL '7 days'
FROM events;

SELECT *
FROM events
WHERE created_at >= CURRENT_TIMESTAMP - INTERVAL '30 days';
```

MySQL:

```sql
SELECT created_at + INTERVAL 7 DAY
FROM events;

SELECT *
FROM events
WHERE created_at >= CURRENT_TIMESTAMP - INTERVAL 30 DAY;
```

Para comparar períodos, prefira um intervalo semiaberto:

```sql
WHERE created_at >= TIMESTAMP '2025-01-01 00:00:00'
  AND created_at < TIMESTAMP '2025-02-01 00:00:00'
```

Isso evita depender da maior precisão possível do último instante do mês.

## Fuso horário

Um evento deve registrar um instante quando precisa ser comparado globalmente. Armazenar apenas `10:00` não informa se é horário de Brasília, UTC ou horário de verão.

No PostgreSQL, a conversão pode ser expressa com `AT TIME ZONE`:

```sql
SELECT created_at AT TIME ZONE 'America/Sao_Paulo'
FROM events;
```

A interpretação exata depende do tipo da coluna. Defina uma política para entrada, armazenamento e apresentação e teste transições de horário de verão quando elas forem relevantes.

## Idade e diferença

PostgreSQL possui `AGE`:

```sql
SELECT AGE(CURRENT_DATE, birth_date)
FROM users;
```

Para relatórios, decida se a diferença deve ser medida em dias, meses de calendário ou segundos. “Um mês” não possui sempre a mesma quantidade de dias.

## Formatação

MySQL:

```sql
SELECT DATE_FORMAT(created_at, '%d/%m/%Y %H:%i')
FROM events;
```

PostgreSQL:

```sql
SELECT TO_CHAR(created_at, 'DD/MM/YYYY HH24:MI')
FROM events;
```

Essas funções são adequadas para relatórios e interfaces, não para substituir o tipo temporal no armazenamento.
