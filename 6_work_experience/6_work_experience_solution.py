import sqlite3
import datetime


def calculate_experience(date_hired):
    today = datetime.date.today()
    hire_date = datetime.datetime.strptime(date_hired, '%Y-%m-%d').date()
    experience = (today.year - hire_date.year) * 12 + today.month - hire_date.month
    return experience


# Добавление данных в таблицу employees
employees_data = [('Иван', 'Петров', 'менеджер', 28, '2021-01-01'),
                  ('Анна', 'Смирнова', 'разработчик', 35, '2020-02-01'),
                  ('Егор', 'Сергеев', 'технический писатель', 30, '2022-01-01'),
                  ('Александр', 'Иванов', 'дизайнер', 42, '2019-11-01'),
                  ('Ольга', 'Попова', 'финансист', 37, '2018-06-01'),
                  ('Дмитрий', 'Кузнецов', 'менеджер', 26, '2020-08-01'),
                  ('Мария', 'Ковалева', 'разработчик', 31, '2021-03-01'),
                  ('Сергей', 'Морозов', 'технический писатель', 48, '2017-05-01'),
                  ('Елена', 'Новикова', 'дизайнер', 34, '2019-09-01'),
                  ('Игорь', 'Соколов', 'финансист', 30, '2017-11-01'),
                  ('Алексей', 'Смирнов', 'менеджер', 33, '2020-04-01'),
                  ('Екатерина', 'Крылова', 'разработчик', 29, '2021-02-01'),
                  ('Денис', 'Медведев', 'технический писатель', 45, '2018-05-01'),
                  ('Елена', 'Иванова', 'дизайнер', 31, '2023-05-01'),
                  ('Дмитрий', 'Терентьев', 'финансист', 29, '2017-09-01'),
                  ('Олег', 'Кузьмин', 'менеджер', 39, '2019-12-01'),
                  ('Анастасия', 'Григорьева', 'разработчик', 33, '2021-05-01'),
                  ('Павел', 'Куликов', 'технический писатель', 47, '2018-03-01'),
                  ('Марина', 'Егорова', 'дизайнер', 28, '2023-03-01'),
                  ('Артем', 'Буров', 'финансист', 26, '2017-11-01'),
                  ('Андрей', 'Игнатьев', 'менеджер', 32, '2022-06-01')]

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Создание таблицы employees
cursor.execute('''CREATE TABLE employees
                (id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                position TEXT,
                age INTEGER,
                hire_date TEXT)''')

# Добавление данных в таблицу employees
for employee in employees_data:
    cursor.execute('INSERT INTO employees (first_name, last_name, position, age, hire_date) VALUES (?, ?, ?, ?, ?)',
                   (employee[0], employee[1], employee[2], employee[3], employee[4]))

# Извлечение данных из таблицы employees и сортировка по столбцу hire_date
cursor.execute('SELECT * FROM employees')
employees = cursor.fetchall()
employees_sorted = sorted(employees, key=lambda x: calculate_experience(x[5]), reverse=True)

# Вывод отсортированного списка сотрудников
for employee in employees_sorted:
    experience = calculate_experience(employee[5])
    print(f'{employee[1]} {employee[2]} - {experience} мес. опыта работы')

conn.commit()
conn.close()