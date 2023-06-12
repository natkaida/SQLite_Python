import sqlite3

# подключение к базе данных
conn = sqlite3.connect('mybooks.db')

# создание таблицы books
conn.execute('''CREATE TABLE books
                (id INTEGER PRIMARY KEY,
                 имя_автора TEXT,
                 фамилия_автора TEXT,
                 название_романа TEXT,
                 страна TEXT);''')

books = [
    ('Джон', 'Р. Р. Толкин', 'Властелин колец', 'Великобритания'),
    ('Джейн', 'Остин', 'Гордость и предубеждение', 'Великобритания'),
    ('Филип', 'Пулман', 'Тёмные начала', 'Великобритания'),
    ('Дуглас', 'Адамс', 'Автостопом по галактике', 'Великобритания'),
    ('Джоан', 'Роулинг', 'Гарри Поттер и Кубок огня', 'Великобритания'),
    ('Харпер', 'Ли', 'Убить пересмешника', 'США'),
    ('Алан Александр', 'Милн', 'Винни Пух', 'Великобритания'),
    ('Джордж', 'Оруэлл', '1984', 'Великобритания'),
    ('Клайв Стэйплз', 'Льюис', 'Лев, колдунья и платяной шкаф', 'Великобритания'),
    ('Шарлотта', 'Бронте', 'Джейн Эйр', 'Великобритания'),
    ('Джозеф', 'Хеллер', 'Уловка-22', 'США'),
    ('Эмили', 'Бронте', 'Грозовой перевал', 'Великобритания'),
    ('Себастьян', 'Фолкс', 'Пение птиц', 'Великобритания'),
    ('Дафна', 'Дюморье', 'Ребекка', 'Великобритания'),
    ('Джером', 'Сэлинджер', 'Над пропастью во ржи', 'США'),
    ('Кеннет', 'Грэм', 'Ветер в ивах', 'Великобритания'),
    ('Чарльз', 'Диккенс', 'Большие надежды', 'Великобритания'),
    ('Луиза Мэй', 'Олкотт', 'Маленькие женщины', 'США'),
    ('Луи', 'де Берньер', 'Мандолина капитана Корелли', 'Великобритания'),
    ('Лев', 'Толстой', 'Война и мир', 'Россия'),
    ('Маргарет', 'Митчелл', 'Унесённые ветром', 'США'),
    ('Джоан', 'Роулинг', 'Гарри Поттер и философский камень', 'Великобритания'),
    ('Джоан', 'Роулинг', 'Гарри Поттер и Тайная комната', 'Великобритания'),
    ('Джоан', 'Роулинг', 'Гарри Поттер и узник Азкабана', 'Великобритания'),
    ('Джон', 'Р. Р. Толкин', 'Хоббит, или Туда и обратно', 'Великобритания')
]

# внесение записей в таблицу
conn.executemany("INSERT INTO books (имя_автора, фамилия_автора, название_романа, страна) VALUES (?, ?, ?, ?)", books)
conn.commit()

conn = sqlite3.connect('mybooks.db')

# выборка данных из таблицы books по условию
cursor = conn.execute("SELECT * FROM books WHERE страна NOT IN (?, ?)", ('США', 'Великобритания'))

# вывод результатов выборки
for row in cursor:
    print(f"{row[0]} - {row[1]} {row[2]}, \"{row[3]}\", {row[4]}")
conn.close()
