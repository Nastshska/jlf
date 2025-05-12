def display_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Список задач:")
        for index in range(len(tasks)):
            print(f"{index + 1}. {tasks[index]}")

def add_task(tasks):
    new_task = input('Введите задачу, которую хотите добавить: ')
    tasks.append(new_task)
    print("Задача добавлена.")
    return tasks

