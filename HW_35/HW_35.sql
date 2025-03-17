-- Homework 35
-- Расширение базы данных SQLite для барбершопа с дополнительными таблицами и модификацией существующих

-- 1. Модификация таблицы masters_services:
--    - Добавить поле `price` (REAL) — индивидуальная цена мастера на услугу.
--    - Добавить поле `duration_minutes` (INTEGER) — индивидуальная длительность выполнения услуги (значение может быть NULL).

ALTER TABLE MastersServices
ADD COLUMN 
    price REAL NOT NULL DEFAULT 0;

ALTER TABLE MastersServices
ADD COLUMN
    duration_minutes INTEGER;

-- 2. Модификация таблицы Services:
--    - Добавить поле `duration_minutes` (INTEGER NOT NULL) — стандартная длительность услуги в минутах.

ALTER TABLE Services
ADD COLUMN
    duration_minutes INTEGER NOT NULL DEFAULT 0;

-- 3. Модификация таблицы ServiceRecord:
--    - Добавить поле `start_time` (TEXT NOT NULL) — время начала записи в формате "HH:MM".
--    - Добавить поле `end_time` (TEXT NOT NULL) — расчетное время окончания записи.
--    - Заменить поле `status` на поле `status_id` (INTEGER) с внешним ключом на новую таблицу статусов.

ALTER TABLE ServiceRecord
ADD COLUMN
    start_time TEXT NOT NULL DEFAULT '00:00';

ALTER TABLE ServiceRecord
ADD COLUMN
    end_time TEXT NOT NULL DEFAULT '00:00';

ALTER TABLE ServiceRecord
DROP COLUMN
    status;

ALTER TABLE ServiceRecord
ADD COLUMN
    status_id INTEGER;  --FOREIGN KEY добавлю после создания таблицы

-- 4. Таблица StatusDictionary
--    - Поля:
--      - `status_id` (INTEGER PRIMARY KEY AUTOINCREMENT) — идентификатор статуса.
--      - `name` (TEXT NOT NULL UNIQUE) — название статуса (например, "Подтверждена", "Отменена", "Выполнена").
--      - `description` (TEXT) — описание статуса (необязательно).

CREATE TABLE IF NOT EXISTS StatusDictionary (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Так при помощи ALTER сделать FOREIGN KEY не получилось, создаем новую таблицу (кстати в данном ДЗ на уже с другим именем), а данные переносим из старой.
CREATE TABLE IF NOT EXISTS Appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    master_id INTEGER,
    start_time TEXT NOT NULL DEFAULT '00:00',
    end_time TEXT NOT NULL DEFAULT '00:00',
    status_id INTEGER,
    FOREIGN KEY (master_id) REFERENCES Masters(id) ON DELETE SET NULL
    FOREIGN KEY (status_id) REFERENCES StatusDictionary(status_id) ON DELETE SET NULL ON UPDATE CASCADE
);

INSERT INTO Appointments
SELECT * FROM ServiceRecord;

DROP TABLE ServiceRecord;

-- 5. Таблица Reviews (Отзывы)
--    - Поля:
--      - `review_id` (INTEGER PRIMARY KEY AUTOINCREMENT) — идентификатор отзыва.
--      - `appointment_id` (INTEGER NOT NULL) — внешний ключ на таблицу Appointments.
--      - `rating` (INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5)) — оценка от 1 до 5.
--      - `comment` (TEXT) — текстовое поле для комментария (опционально).
--      - `date` (TEXT DEFAULT CURRENT_TIMESTAMP) — дата создания отзыва.

CREATE TABLE IF NOT EXISTS Reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    comment TEXT,
    date TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- 6. Таблица MasterSchedule (Расписание)
--    - Поля:
--      - `schedule_id` (INTEGER PRIMARY KEY AUTOINCREMENT) — идентификатор записи расписания.
--      - `master_id` (INTEGER NOT NULL) — внешний ключ на таблицу Masters.
--      - `day_of_week` (INTEGER NOT NULL CHECK(day_of_week BETWEEN 1 AND 7)) — день недели (1 – понедельник, 7 – воскресенье).
--      - `start_time` (TEXT NOT NULL) — время начала работы.
--      - `end_time` (TEXT NOT NULL) — время окончания работы.
--      - `status_id` (INTEGER NOT NULL) — статус дня (например, рабочий день, выходной).
--      - `comment` (TEXT) — комментарий к расписанию (необязательно).

CREATE TABLE IF NOT EXISTS MasterSchedule (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    master_id INTEGER NOT NULL,
    day_of_week INTEGER NOT NULL CHECK(day_of_week BETWEEN 1 AND 7),
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    status_id INTEGER NOT NULL,
    comment TEXT,
    FOREIGN KEY (master_id) REFERENCES Masters(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (status_id) REFERENCES StatusDictionary(status_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);


-------------------Серия запросов в БД----------------------------------
-- 1. Новая запись записи на услугу
    -- Создать транзакцию, в рамках которой:
    -- - Добавить новую запись в таблицу Appointments для клиента.
    -- - Добавить одну или несколько записей в appointments_services, связывающих запись с выбранными услугами.
    -- - При возникновении ошибки откатить все изменения.

BEGIN TRANSACTION;
INSERT INTO StatusDictionary 
(name, description)
VALUES 
    ('Подтверждена', 'Запись подтверждена'),
    ('Отменена', 'Запись отменена'),
    ('Выполнена', 'Запись выполнена'),
    ('Работает', 'Рабочий день'),
    ('Выходной', 'Выходной день');

INSERT INTO Appointments (name, phone, date, master_id, start_time, end_time, status_id)
VALUES (
    'Вася Васечкин', 
    '1234567890', 
    '2023-09-20 10:00:00', 
    1, 
    '10:00', 
    '11:00', 
    1
);

INSERT INTO AppointmentsServices (appointment_id, service_id)
VALUES (
    (SELECT id FROM Appointments WHERE name = 'Вася Васечкин'),
    (SELECT id FROM Services WHERE title = 'Стрижка')
);

INSERT INTO AppointmentsServices (appointment_id, service_id)
VALUES (
    (SELECT id FROM Appointments WHERE name = 'Вася Васечкин'),
    (SELECT id FROM Services WHERE title = 'Стрижка бороды')
);

COMMIT;

-- 2. Изменение статуса записи 
    -- Создать транзакцию, которая обновит запись в таблице Appointments:
    
    -- - Заменить статус старого значения на новый, изменив поле status_id.
    -- - Если запись имеет связанные элементы в Reviews (например, автоматически установить отрицательную оценку при отмене), обновите их.
    -- - Обеспечьте корректный откат в случае возникновения проблем.

BEGIN TRANSACTION;

UPDATE Appointments
SET status_id = (SELECT status_id FROM StatusDictionary WHERE name = 'Отменена')
WHERE id = (SELECT id FROM Appointments WHERE name = 'Васька Филипенко');

INSERT INTO Reviews (appointment_id, rating, comment)
VALUES (
    (SELECT id FROM Appointments WHERE name = 'Васька Филипенко'),
    1,
    'Парикмахер скотина - опять нажрался'
);

UPDATE Appointments
SET status_id = (SELECT status_id FROM StatusDictionary WHERE name = 'Подтверждена')
WHERE id = (SELECT id FROM Appointments WHERE name = 'Иешуа Га-Ноцри');

UPDATE Appointments
SET status_id = (SELECT status_id FROM StatusDictionary WHERE name = 'Подтверждена')
WHERE id = (SELECT id FROM Appointments WHERE name = 'Алиса');

UPDATE Appointments
SET status_id = (SELECT status_id FROM StatusDictionary WHERE name = 'Подтверждена')
WHERE id = (SELECT id FROM Appointments WHERE name = 'Елизавета Васильевна');

COMMIT;

-- 3. Корректировка цены услуги
    -- Сделать транзакцию по обновлению цены услуги:
    
    -- - Обновить базовую цену в таблице Services.
    -- - Обновить индивидуальные цены в таблице masters_services для данной услуги (при необходимости).
    -- - Проверить, что транзакция фиксируется только при успешном выполнении всех шагов.

BEGIN TRANSACTION;

UPDATE Services
SET price = 1500
WHERE title = 'Стрижка детская';

UPDATE MastersServices
SET price = 1750
WHERE service_id = (SELECT id FROM Services WHERE title = 'Стрижка детская')
AND master_id = (SELECT id FROM Masters WHERE last_name = 'Иванов' AND first_name = 'Иван');    

COMMIT;

-- 4. Обновление расписания мастера
    -- Создать транзакцию для изменения расписания мастера в таблице MasterSchedule:
    
    -- - Обновить поля start_time и end_time для выбранного мастера.
    -- - При этом можно добавить проверку – например, чтобы новый интервал не пересекался с уже существующими.
    -- - В случае ошибки провести ROLLBACK.

BEGIN TRANSACTION;

INSERT INTO MasterSchedule (master_id, day_of_week, start_time, end_time, status_id, comment)
VALUES (
    1,
    1,
    '15:00',
    '17:00',
    (SELECT status_id FROM StatusDictionary WHERE name = 'Работает'),
    'Работаем с 15 до 17'
);

UPDATE MasterSchedule
SET start_time = '13:00', end_time = '15:00'
WHERE master_id = 1 AND day_of_week = 1;

COMMIT

-- 5. Добавление нового статуса 
    -- Реализуйте транзакцию для массовой вставки новой записи в таблицу StatusDictionary:
    
    -- - Выполните вставку нового статуса с уникальным именем.
    -- - Если имя статуса уже существует, откатите транзакцию и выведите сообщение об ошибке.

BEGIN TRANSACTION;

INSERT INTO StatusDictionary (name, description)
VALUES ('Уволился', 'Больше не работает');

COMMIT;

-- 6. Добавление отзыва клиента
    -- В транзакции:
    
    -- - Добавьте новую запись в таблицу Reviews для конкретной записи из Appointments.
    -- - При этом проверьте, что рейтинг находится в допустимом диапазоне (от 1 до 5) и все внешние ключи корректны.
    -- - Зафиксируйте вставку только если все условия выполнены.

BEGIN TRANSACTION;

INSERT INTO Reviews (appointment_id, rating, comment)
VALUES (
    (SELECT id FROM Appointments WHERE name = 'Вася Васечкин'),
    5,
    'Отличная работа, рекомендую!'
    );
    
COMMIT;

-- 7. Массовая вставка новых услуг

    -- Создайте транзакцию для пакетного добавления нескольких новых записей в таблицу Services:
    
    -- - Вставьте 2–3 услуги за одну транзакцию.
    -- - Проверьте, что для каждой услуги поле `duration_minutes` заполнено, а название услуги уникально.
    -- - В случае ошибки – отмените вставку всех услуг.

BEGIN TRANSACTION;

INSERT INTO Services (title, description, duration_minutes, price)
VALUES ('Маникюр', 'Маникюр с покрытием', 45, 1000),
       ('Педикюр', 'Педикюр с покрытием', 60, 1500);

COMMIT;

-- 8. Отмена записи на услугу

    -- Сформируйте транзакцию для отмены уже существующей записи:
    
    -- - Измените status_id записи в таблице Appointments на значение, соответствующее статусу «Отменена» из таблицы StatusDictionary.
    -- - Удалите связанные записи в таблице appointments_services, если это необходимо (например, если отмена записи подразумевает удаление услуг).
    -- - Зафиксируйте изменения или выполните откат при ошибке.

BEGIN TRANSACTION;

UPDATE Appointments
SET status_id = (SELECT status_id FROM StatusDictionary WHERE name = 'Отменена')
WHERE id = 1;

DELETE FROM AppointmentsServices
WHERE appointment_id = 1;

COMMIT;