-- Домашнее задание №34
-- Создание таблиц SQLite и внесение записей для барбершопа

-- Таблица «Запись на услуги»:
--    - id – первичный ключ
--    - name – имя клиента, записавшегося на услугу
--    - phone – телефон клиента
--    - Дата – дата, устанавливаемая автоматически при записи (можно использовать функцию CURRENT_TIMESTAMP)
--    - master_id – внешний ключ на таблицу мастеров
--    - status – статус записи (например, подтверждена, отменена, ожидает)

CREATE TABLE IF NOT EXISTS ServiceRecord (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    master_id INTEGER,
    status TEXT,
    FOREIGN KEY (master_id) REFERENCES Masters(id) ON DELETE SET NULL
);

-- Таблица «Мастера»:
--    - id – первичный ключ (если не указан, рекомендуется добавить)
--    - first_name – имя мастера
--    - last_name – фамилия мастера
--    - middle_name – отчество мастера
--    - phone – контактный телефон мастера

CREATE TABLE IF NOT EXISTS Masters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    middle_name TEXT,
    phone TEXT
);

-- Таблица «Услуги»:
--    - id – первичный ключ
--    - title – название услуги (*уникальная*)
--    - description – описание услуги
--    - price – стоимость услуги

CREATE TABLE IF NOT EXISTS Services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    price REAL NOT NULL
);

-- Таблица для связи мастеров и услуг (masters_services):
--      - Поля: master_id (внешний ключ на таблицу мастеров) и service_id (внешний ключ на таблицу услуг)
--      - Требование уникальности пары

CREATE TABLE IF NOT EXISTS MastersServices (
    master_id INTEGER,
    service_id INTEGER,
    FOREIGN KEY (master_id) REFERENCES Masters(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES Services(id) ON DELETE CASCADE,
    PRIMARY KEY (master_id, service_id)
);

-- Таблица для связи записей и услуг (appointments_services):
--      - Поля: appointment_id (внешний ключ на таблицу записей) и service_id (внешний ключ на таблицу услуг)
--      - Требование уникальности пары

CREATE TABLE IF NOT EXISTS AppointmentsServices (
    appointment_id INTEGER,
    service_id INTEGER,
    FOREIGN KEY (appointment_id) REFERENCES ServiceRecord(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES Services(id) ON DELETE CASCADE,
    PRIMARY KEY (appointment_id, service_id)
);

-- Включение проверки целостности базы данных и поддержки внешних ключей
PRAGMA foreign_keys = ON

-- Добавить 2 записи в таблицу «Мастера». Каждая запись должна содержать имя, фамилию, отчество и телефон
INSERT INTO Masters (first_name, last_name, middle_name, phone)
VALUES
    ('Иван', 'Иванов', 'Иванович', '1234567890'),
    ('Петр', 'Петров', 'Петрович', '9876543210');

-- Добавить 5 записей в таблицу «Услуги» с указанием названия услуги, описания и цены.
INSERT INTO Services (title, description, price)
VALUES
    ('Стрижка мужская', 'Модная стрижка для мужиков', 1500),
    ('Стрижка женская', 'Няшная стрижка для девушек', 3000),
    ('Стрижка детская', 'Супер крутая стрижка для супер крутых подростков', 1000),
    ('Стрижка лысый бородач', 'Голые вершки - волосатые корешки (подбородки)', 6000),
    ('Lambersexual`s cut', 'Ламберсексуалам сюда', 7500);

    