import sqlite3

# соединяемся с БД
con = sqlite3.connect("vetPatients_base.db")
# создаем объект курсора
cur = con.cursor()

# создаем таблицу 1
cur.execute("""CREATE TABLE pets
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name       VARCHAR,
    species    VARCHAR,
    breed      VARCHAR,
    sex        CHAR(1),
    birth_date DATE,
    owner_id   INTEGER,
    nursery_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES owners (id),
    FOREIGN KEY (nursery_id) REFERENCES nurseries (id)
)
""")
# таблица 2
cur.execute("""CREATE TABLE owners
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name         VARCHAR,
    phone_number VARCHAR
)
""")
# таблица 3
cur.execute("""CREATE TABLE nurseries
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name         VARCHAR,
    phone_number VARCHAR
)
""")
# вводим данные
cur.execute('INSERT INTO pets VALUES(1, "Tuzik", "dog", "Pug", "m", "2010.02.11", 1, 2)')
cur.execute('INSERT INTO pets VALUES(2, "Murzik", "cat", "Maine coon", "m", "2015.08.05", 2, 3)')
cur.execute('INSERT INTO pets VALUES(3, "Leia", "cat", "Devon rex", "f", "2018.06.26", 3, 1)')
cur.execute('INSERT INTO owners VALUES(1, "Sergeev Sergey", "0972498345")')
cur.execute('INSERT INTO owners VALUES(2, "Marinina Marina", "0634657788")')
cur.execute('INSERT INTO owners VALUES(3, "Korshikova Tetiana", "0931112233")')
cur.execute('INSERT INTO nurseries VALUES(1, "Gold Star", "0955553545")')
cur.execute('INSERT INTO nurseries VALUES(2, "Leader", "0977773747")')
cur.execute('INSERT INTO nurseries VALUES(3, "Super Duper", "0633333343")')
cur.execute('INSERT INTO nurseries VALUES(4, "Best of the best", "0676776777")')
cur.execute('INSERT INTO nurseries VALUES(5, "Champions", "0991992939")')
# сохранить изменения
con.commit()
# закрыть соединение
cur.close()
con.close()
