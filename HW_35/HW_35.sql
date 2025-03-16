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
    ('Отменена', 'Запись отменена');

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