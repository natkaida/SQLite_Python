import sqlite3

# подключение к базе данных
conn = sqlite3.connect('clothing.db')

# создание таблицы t_shirts
conn.execute('''CREATE TABLE IF NOT EXISTS t_shirts
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 бренд TEXT,
                 размер TEXT,
                 цена REAL,
                 цвет TEXT);''')

# данные для заполнения таблицы
t_shirts = [
    ('Levi\'s', 'S', 29.99, 'белый'),
    ('Nike', 'M', 24.99, 'черный'),
    ('Adidas', 'L', 19.99, 'синий'),
    ('H&M', 'S', 14.99, 'красный'),
    ('Reebok', 'M', 39.99, 'черный'),
    ('Zara', 'L', 29.99, 'белый'),
    ('Puma', 'S', 19.99, 'серый'),
    ('Lacoste', 'M', 49.99, 'зеленый'),
    ('Calvin Klein', 'L', 59.99, 'синий'),
    ('Tommy Hilfiger', 'S', 44.99, 'красный'),
    ('Gap', 'M', 34.99, 'серый'),
    ('Uniqlo', 'L', 24.99, 'белый'),
    ('Hollister', 'S', 29.99, 'синий'),
    ('Diesel', 'M', 39.99, 'черный'),
    ('Gucci', 'L', 199.99, 'красный'),
    ('Armani', 'S', 149.99, 'серый'),
    ('Ralph Lauren', 'M', 89.99, 'белый'),
    ('Hugo Boss', 'L', 129.99, 'синий'),
    ('Burberry', 'S', 299.99, 'красный'),
    ('Versace', 'M', 249.99, 'черный')
]

# вставка данных в таблицу
conn.executemany("INSERT INTO t_shirts (бренд, размер, цена, цвет) VALUES (?, ?, ?, ?)", t_shirts)

# сохранение изменений в базе данных
conn.commit()

conn.close()