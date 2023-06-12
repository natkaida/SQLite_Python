import sqlite3

con = sqlite3.connect('sales.db')
cursor = con.cursor()

# Создаем таблицу items
cursor.execute('''
    CREATE TABLE items (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        model TEXT,
        color TEXT,
        engine_volume REAL,
        max_speed INTEGER,
        price INTEGER
    )
''')

# Заполняем таблицу items данными
cars = [
    ('Audi', 'A6', 'черный', 2.0, 240, 2000000),
    ('Audi', 'Q7', 'серый', 3.0, 230, 4000000),
    ('BMW', 'X5', 'белый', 4.4, 250, 4500000),
    ('BMW', '5-серии', 'синий', 2.0, 220, 1800000),
    ('Chevrolet', 'Camaro', 'красный', 3.6, 280, 3000000),
    ('audi', 'Q7', 'серый', 3.0, 230, 4000000),
    ('Chevrolet', 'Tahoe', 'серый', 5.3, 180, 3500000),
    ('Chevrolet', 'camaro', 'красный', 3.6, 280, 3000000),
    ('Ford', 'Focus', 'желтый', 1.6, 180, 900000),
    ('Ford', 'Mustang', 'синий', 5.0, 280, 2700000),
    ('Honda', 'Civic', 'черный', 1.5, 220, 1200000),
    ('Honda', 'Accord', 'белый', 2.0, 240, 1800000),
    ('Hyundai', 'Santa Fe', 'серый', 2.4, 180, 1400000),
    ('Hyundai', 'Sonata', 'красный', 2.0, 220, 1300000),
    ('kia', 'sorento', 'синий', 2.2, 200, 1800000),
    ('Infiniti', 'FX35', 'черный', 3.5, 240, 2500000),
    ('Infiniti', 'Q50', 'серый', 2.0, 220, 2100000),
    ('KIA', 'Ceed', 'белый', 1.4, 180, 1000000),
    ('KIA', 'Sorento', 'синий', 2.2, 200, 1800000),
    ('Lexus', 'NX200', 'черный', 2.0, 220, 2700000),
    ('Nissan', 'x-Trail', 'красный', 2.0, 220, 1800000),
    ('Lexus', 'RX350', 'белый', 3.5, 240, 3500000),
    ('Mercedes-Benz', 'S500', 'серый', 5.5, 250, 10000000),
    ('Mercedes-Benz', 'GLE250', 'синий', 2.2, 230, 4000000),
    ('Nissan', 'Teana', 'белый', 2.5, 200, 1600000),
    ('Nissan', 'X-Trail', 'красный', 2.0, 220, 1800000),
    ('Toyota', 'Camry', 'черный', 2.5, 210, 2000000),
    ('Toyota', 'Land Cruiser 200', 'белый', 4.5, 220, 7000000),
    ('mercedes-Benz', 'S500', 'серый', 5.5, 250, 10000000),
    ('Volkswagen', 'Passat', 'серый', 1.8, 200, 1300000)
]

for i, car in enumerate(cars):
    cursor.execute(
        f"INSERT INTO items VALUES ({i+1}, ?, ?, ?, ?, ?, ?)",
        (car[0], car[1], car[2], car[3], car[4], car[5])
    )

con.commit()
con.close()