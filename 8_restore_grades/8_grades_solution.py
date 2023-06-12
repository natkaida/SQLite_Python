import sqlite3

con = sqlite3.connect('exams.db')
cursor = con.cursor()

# Выполняем запрос для обновления оценок
cursor.execute('''
    UPDATE math SET grade = grade - 1 WHERE group_name = 'b23';
''')

# Сохраняем изменения в базе данных
con.commit()
con.close()