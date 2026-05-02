run = True

while run:

    tasks = []

    command = input('Введите команду: ')
    task = input('Введите задачу: ')
    s = command + ' ' + task
    tasks.append(task)
    print ('Задача ' + task + ' добавлена')

    command = input('Введите команду: ')

    if command=='show':
        print(task)

    if command=='exit':
        print('Спасибо за использование! До свидания!')
        break
