-- Домашнее задание №34
-- Создание таблиц SQLite и внесение записей для барбершопа

-- Таблица «Запись на услуги» (Хранит информацию о записях клиентов):
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

-- Таблица «Мастера» (Сведения о мастерах барбершопа):
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

-- Таблица «Услуги» (Детали оказываемых услуг):
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

-- Таблица для связи мастеров и услуг (masters_services) (Связывает мастеров с оказываемыми услугами):
--      - Поля: master_id (внешний ключ на таблицу мастеров) и service_id (внешний ключ на таблицу услуг)
--      - Требование уникальности пары

CREATE TABLE IF NOT EXISTS MastersServices (
    master_id INTEGER,
    service_id INTEGER,
    FOREIGN KEY (master_id) REFERENCES Masters(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES Services(id) ON DELETE CASCADE,
    PRIMARY KEY (master_id, service_id)
);

-- Таблица для связи записей и услуг (appointments_services) (Позволяет установить связь между записью и несколькими услугами):
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

-- В таблице masters_services установить связи между мастерами и услугами (каждый мастер может выполнять несколько услуг, одна услуга может выполняться несколькими мастерами). Запросы должны показать, какие мастера оказывают какие услуги.
INSERT INTO MastersServices (master_id, service_id)
VALUES
    (1, 1),
    (1, 3),
    (1, 5),
    (2, 2),
    (2, 4);

SELECT m.first_name, m.last_name, s.title, s.description, s.price
FROM Masters m
JOIN MastersServices ms ON m.id = ms.master_id
JOIN Services s ON ms.service_id = s.id;

-- В таблице «Запись на услуги» добавить 4 записи, где клиент может записаться на одну или несколько услуг. В таблице `appointments_services` задать связанные услуги для каждой записи.
INSERT INTO ServiceRecord (name, phone, master_id, status)
VALUES
    ('Васька Филипенко', '+7 (922) 877-17-33', 1, 'Подтверждена'),
    ('Иешуа Га-Ноцри', '+7 (777) 777-77-77', 1, 'Подтверждена'),
    ('Алиса', '+7 (932) 122-13-54', 2, 'Подтверждена'),
    ('Елизавета Васильевна', '+7 (911) 442-11-32', 2, 'Подтверждена');

INSERT INTO AppointmentsServices (appointment_id, service_id)
VALUES
    (1, 4),
    (2, 5),
    (3, 2),
    (3, 3),
    (4, 2);

-- Статус записи может изменяться,предусмотреть возможность обновления этого поля.
UPDATE ServiceRecord
SET status = 'Отменена'
WHERE id = 1;