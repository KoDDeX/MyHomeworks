-- HomeWork 33
-- Работа с базой данных `marvel` и написание SQL-запросов

-- 1. Общее количество персонажей по статусу
SELECT ALIVE, COUNT(*) AS TOTAL_ALIVE
From MarvelCharacters
WHERE ALIVE IS NOT NULL
GROUP BY ALIVE;

-- 2. Среднее количество появлений персонажей с разным цветом глаз
SELECT EYE, AVG(APPEARANCES) AS Average
FROM MarvelCharacters
WHERE 
    EYE IS NOT NULL AND
    EYE IS NOT 'No Eyes'
GROUP BY EYE
ORDER BY Average DESC;

-- 3. Максимальное количество появлений у персонажей с определенным цветом волос
SELECT HAIR, MAX(APPEARANCES) AS MAX_APPEARANCES
FROM MarvelCharacters
WHERE 
    HAIR IS NOT NULL AND
    HAIR IS NOT 'No Hair' AND
    HAIR IS NOT 'Bald'
GROUP BY HAIR
ORDER BY MAX_APPEARANCES DESC;

-- 4. Минимальное количество появлений среди персонажей с известной и публичной личностью
SELECT identify, min(APPEARANCES) as MIN_APPEARANCES
FROM MarvelCharacters
WHERE identify = 'Public Identity'
GROUP BY identify;

-- 5. Общее количество персонажей по полу
SELECT SEX, count(*) AS TOTAL
FROM MarvelCharacters
WHERE SEX IS NOT NULL
GROUP BY SEX
ORDER BY TOTAL DESC;

-- 6. Средний год первого появления персонажей с различным типом личности
SELECT identify, AVG(YEAR) AS Average
FROM MarvelCharacters
WHERE identify IS NOT NULL
GROUP BY identify
ORDER BY Average DESC;

-- 7. Количество персонажей с разным цветом глаз среди живых
SELECT EYE, COUNT(*) AS TOTAL_ALIVE
FROM MarvelCharacters
WHERE 
    EYE IS NOT NULL AND
    EYE IS NOT 'No Eyes' AND
    ALIVE = 'Living Characters'
GROUP BY EYE
ORDER BY TOTAL_ALIVE DESC;

-- 8. Максимальное и минимальное количество появлений среди персонажей с определенным цветом волос
SELECT HAIR, MAX(APPEARANCES) AS MAX_APPEARANCES, MIN(APPEARANCES) AS MIN_APPEARANCES
FROM MarvelCharacters
WHERE
    HAIR IS NOT NULL AND
    HAIR IS NOT 'No Hair' AND
    HAIR IS NOT 'Bald'
GROUP BY HAIR
ORDER BY MAX_APPEARANCES DESC;

-- 9. Количество персонажей с различным типом личности среди умерших
SELECT identify, COUNT(*) AS TOTAL_DEAD
FROM MarvelCharacters
WHERE 
    identify IS NOT NULL AND 
    ALIVE = 'Deceased Characters'
GROUP BY identify
ORDER BY TOTAL_DEAD DESC;

-- 10.  Средний год первого появления персонажей с различным цветом глаз
SELECT EYE, AVG(YEAR) AS Average
FROM MarvelCharacters
WHERE
    EYE IS NOT NULL AND
    EYE IS NOT 'No Eyes'
GROUP BY EYE
ORDER BY Average DESC;

-- ПОДЗАПРОСЫ

-- 11. Персонаж с наибольшим количеством появлений
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES = (SELECT MAX(APPEARANCES) FROM MarvelCharacters);

-- 12. Персонажи, впервые появившиеся в том же году, что и персонаж с максимальными появлениям
SELECT name, YEAR
FROM MarvelCharacters
WHERE YEAR = (SELECT YEAR FROM MarvelCharacters WHERE APPEARANCES = (SELECT MAX(APPEARANCES) FROM MarvelCharacters));

-- 13. Персонажи с наименьшим количеством появлений среди живых
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES = (SELECT MIN(APPEARANCES) FROM MarvelCharacters WHERE ALIVE = 'Living Characters');

-- 14. Персонажи с определенным цветом волос и максимальными появлениями среди такого цвета
SELECT name, HAIR, APPEARANCES
FROM MarvelCharacters
WHERE HAIR LIKE 'Red%' AND APPEARANCES = (SELECT MAX(APPEARANCES) FROM MarvelCharacters WHERE HAIR LIKE 'Red%');

SELECT HAIR, max(APPEARANCES) AS MAX_APPEARANCES, name
FROM MarvelCharacters
GROUP BY HAIR
ORDER BY MAX_APPEARANCES DESC;

-- 15. Персонажи с публичной личностью и наименьшим количеством появлений
SELECT name, identify, APPEARANCES
FROM MarvelCharacters
WHERE identify = 'Public Identity' AND APPEARANCES = (SELECT MIN(APPEARANCES) FROM MarvelCharacters WHERE identify = 'Public Identity');