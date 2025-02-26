-- HomeWork 32.
-- SQL запросы к однотабличной базе данных


-- 1. Лысые злодеи 90-х годов
SELECT name, FIRST_APPEARANCE, Year, APPEARANCES
FROM MarvelCharacters
WHERE 
    HAIR = 'Bald' AND 
    ALIGN = 'Bad Characters' AND 
    YEAR BETWEEN 1990 AND 1999
ORDER BY APPEARANCES DESC;

-- 2. Герои с тайной идентичностью и необычными глазами
SELECT name, YEAR, EYE
FROM  MarvelCharacters
WHERE 
    identify = 'Secret Identity' AND 
    EYE NOT LIKE 'Blue%' AND 
    EYE NOT LIKE 'Green%' AND 
    EYE NOT LIKE 'Brown%' AND 
    FIRST_APPEARANCE NOT Null
ORDER BY YEAR DESC;

-- 3. Персонажи с изменяющимся цветом волос
SELECT name, HAIR
FROM MarvelCharacters
WHERE HAIR = 'Variable Hair';

-- 4. Женские персонажи с редким цветом глаз
SELECT name, EYE
FROM MarvelCharacters
WHERE 
    SEX = 'Female Characters' AND 
    (EYE LIKE 'Gold%' OR 
    EYE LIKE 'Amber%');

-- 5. Персонажи без двойной идентичности, сортированные по году появления
SELECT name, YEAR, identify
FROM MarvelCharacters
WHERE identify is 'No Dual Identity'
ORDER BY YEAR DESC;

-- 6. Герои и злодеи с необычными прическами
SELECT name, ALIGN, HAIR
FROM MarvelCharacters
WHERE
    HAIR NOT LIKE 'Brown%' AND
    HAIR NOT LIKE 'Black%' AND
    HAIR NOT LIKE 'Blond%' AND
    HAIR NOT LIKE 'Red%' AND
    ALIGN IN ('Good Characters', 'Bad Characters');

-- 7. Персонажи, появившиеся в определённое десятилетие
SELECT name, YEAR
FROM MarvelCharacters
WHERE YEAR BETWEEN 1960 AND 1969
ORDER BY YEAR;

-- 8. Персонажи с уникальным сочетанием цвета глаз и волос
SELECT name, EYE, HAIR
FROM MarvelCharacters
WHERE 
    EYE LIKE 'Yellow%' AND
    HAIR LIKE 'Red%';

-- 9. Персонажи с ограниченным количеством появлений
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES < 10
ORDER BY APPEARANCES DESC;

-- 10. Персонажи с наибольшим количеством появлений
SELECT name, APPEARANCES
FROM MarvelCharacters
ORDER BY APPEARANCES DESC
LIMIT 5;