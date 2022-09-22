import sqlite3
import os


def create_table_db():
    return '''CREATE TABLE IF NOT EXISTS users
                                        (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        Second_name TEXT,
                                        First_name TEXT,
                                        Patronymic TEXT,
                                        Region_id INT,
                                        City_id INT,
                                        Phone TEXT,
                                        Email TEXT);
                           CREATE TABLE IF NOT EXISTS regions
                                                      (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                       Region_name TEXT);
                           CREATE TABLE IF NOT EXISTS cities
                                                    (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                     Region_id INT,
                                                     City_name TEXT);
                           CREATE TRIGGER IF NOT EXISTS regions_id AFTER INSERT ON regions BEGIN UPDATE regions SET Id = rowid-1 WHERE rowid = new.rowid;
                                END;
                           CREATE TRIGGER IF NOT EXISTS cities_id AFTER INSERT ON cities BEGIN UPDATE cities SET Id = rowid-1 WHERE rowid = new.rowid;
                                END;
                           CREATE TRIGGER IF NOT EXISTS users_id AFTER INSERT ON users BEGIN UPDATE users SET Id = rowid-1 WHERE rowid = new.rowid;
                                END;'''


def check_db(datebase_name):
    """
    Проверка на наличие: базы данных, таблиц базы данных и заполненности данными таблиц
    """
    create_table = create_table_db()
    if os.path.isfile(datebase_name):
        connection = sqlite3.connect(datebase_name)
        cursor = connection.cursor()

        cursor.executescript(create_table)
        info = cursor.execute('SELECT * FROM users')
        if info.fetchone() is None:
            cursor.execute('''INSERT INTO users(Second_name,
                                                  First_name,
                                                  Patronymic,
                                                  Region_id,
                                                  City_id,
                                                  Phone,
                                                  Email) VALUES
                                ('Краснов', 'Николай', 'Владимирович', 0, 0, '79065986543', 'krasnov@mail.ru'),
                                ('Веселов', 'Никита', 'Владимирович', 1, 3, '79030012349', 'veselov@mail.ru'),
                                ('Петрова', 'Анна', 'Владимировна', 2, 6, '8905893471', 'petrova_anna@mail.ru'),
                                ('Измайлова', 'Александра', 'Ивановна', 0, 1, '7907004389', 'best_star@mail.ru'),
                                ('Лебедева', 'Анастасия', 'Игоревна', 0, 2, '7907004008', 'lebedeva_nas@mail.ru'),
                                ('Михайлов', 'Михаил', 'Владиславович', 1, 4, '7907004008', 'misha@mail.ru')''')
        info = cursor.execute('SELECT * FROM regions')
        if info.fetchone() is None:
            cursor.execute('''INSERT INTO regions(Region_name) VALUES
                                ('Краснодарский край'),
                                ('Ростовская область'),
                                ('Ставропольский край')''')
        info = cursor.execute('SELECT * FROM cities')
        if info.fetchone() is None:
            cursor.execute(''' INSERT INTO cities(Region_id, City_name) VALUES
                                (0, 'Краснодар'),
                                (0, 'Кропоткин'),
                                (0, 'Славянск'),
                                (1, 'Ростов'),
                                (1, 'Шахты'),
                                (1, 'Батайск'),
                                (2, 'Ставрополь'),
                                (2, 'Пятигорск'),
                                (2, 'Кисловодск');''')

    else:
        connection = sqlite3.connect(datebase_name)
        cursor = connection.cursor()
        cursor.executescript(create_table)
        cursor.executescript('''INSERT INTO regions(Region_name) VALUES
                                ('Краснодарский край'),
                                ('Ростовская область'),
                                ('Ставропольский край');
                                INSERT INTO cities(Region_id, City_name) VALUES
                                (0, 'Краснодар'),
                                (0, 'Кропоткин'),
                                (0, 'Славянск'),
                                (1, 'Ростов'),
                                (1, 'Шахты'),
                                (1, 'Батайск'),
                                (2, 'Ставрополь'),
                                (2, 'Пятигорск'),
                                (2, 'Кисловодск');
                                INSERT INTO users(Second_name,
                                                  First_name,
                                                  Patronymic,
                                                  Region_id,
                                                  City_id,
                                                  Phone,
                                                  Email) VALUES
                                ('Краснов', 'Николай', 'Владимирович', 0, 0, '79065986543', 'krasnov@mail.ru'),
                                ('Веселов', 'Никита', 'Владимирович', 1, 3, '79030012349', 'veselov@mail.ru'),
                                ('Петрова', 'Анна', 'Владимировна', 2, 6, '8905893471', 'petrova_anna@mail.ru'),
                                ('Измайлова', 'Александра', 'Ивановна', 0, 1, '7907004389', 'best_star@mail.ru'),
                                ('Лебедева', 'Анастасия', 'Игоревна', 0, 2, '7907004008', 'lebedeva_nas@mail.ru'),
                                ('Михайлов', 'Михаил', 'Владиславович', 1, 4, '7907004008', 'misha@mail.ru')''')
    connection.commit()
    connection.close()
