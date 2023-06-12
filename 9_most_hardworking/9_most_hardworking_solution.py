import sqlite3
import datetime

conn = sqlite3.connect('retailcompany.db')
cursor = conn.cursor()

# Создание словаря для хранения времени пребывания каждого сотрудника
employee_time = {}

# Запрос на вычисление времени пребывания каждого сотрудника в CRM
cursor.execute('''SELECT date, first_name, last_name, time_in, time_out
                FROM workload_june''')

# Суммирование времени пребывания каждого сотрудника за каждый день
for row in cursor.fetchall():
    date_str = row[0]
    first_name = row[1]
    last_name = row[2]
    time_in_str = row[3]
    time_out_str = row[4]

    # Преобразование даты и времени в нужный формат
    date = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
    time_in = datetime.datetime.combine(date, datetime.datetime.strptime(time_in_str, '%H:%M').time())
    time_out = datetime.datetime.combine(date, datetime.datetime.strptime(time_out_str, '%H:%M').time())

    employee = (first_name, last_name)

    if employee not in employee_time:
        employee_time[employee] = {}

    if date not in employee_time[employee]:
        employee_time[employee][date] = 0

    # Вычисление времени пребывания сотрудника в системе
    time_spent = time_out - time_in
    minutes_spent = time_spent.seconds // 60
    employee_time[employee][date] += minutes_spent

# Суммирование времени пребывания каждого сотрудника за весь месяц
for employee, days in employee_time.items():
    total_minutes_spent = sum(days.values())
    total_hours_spent = total_minutes_spent // 60
    total_minutes_spent = total_minutes_spent % 60

    if total_hours_spent >= 100:
        print(f'{employee[0]} {employee[1]}: {total_hours_spent} ч. {str(total_minutes_spent).ljust(2, "0")} мин.')

# Закрытие базы данных
conn.close()
