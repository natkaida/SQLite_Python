import sqlite3

con = sqlite3.connect('calories.db')
cursor = con.cursor()

input_str = input('Введите названия продуктов и их вес через запятую: ')

items = input_str.split(',')
total_calories = 0
for item in items:
    # Разбиваем строку на название продукта и его вес
    name, weight = map(str.strip, item.split(':'))
    name = name.capitalize()
    
    # Получаем калорийность продукта из базы данных
    result = cursor.execute("SELECT calories FROM calories WHERE name=?", (name,))
    row = result.fetchone()
    
    if row is not None:
        # Считаем калорийность текущего продукта
        product_calories = row[0] * float(weight) / 100
        
        # Добавляем калории этого продукта к общей калорийности
        total_calories += product_calories
    else:
        print(f"Продукт {name} отсутствует в базе данных.")

# Выводим общую калорийность готового блюда
print(f"Калорийность готового блюда: {total_calories:.2f} ккал")
con.close()