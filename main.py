from деф import display_tasks, add_task
tasks = []
from друг import factorial


action = input('Выберите действие. \n1. Добавить задачу;\n2. Просмотреть задачи;\n3. Найти факториал;\nВведите 1-3 или стоп: ')

while action != 'стоп':
    if action == '1':
        tasks = add_task(tasks)
    elif action == '2':
        display_tasks(tasks)

    elif action == '3':
        user_input = int(input("Введите целое неотрицательное число для вычисления его факториала: "))
        cBo = factorial(user_input)
        print('Факториал вашего числа равен:', cBo)
    else:
        print("Вы ввели некорректные данные!")

    action = input('Выберите действие. \n1. Добавить задачу;\n2. Просмотреть задачи;\n3. Найти факториал;\nВведите 1-3 или стоп: ')




