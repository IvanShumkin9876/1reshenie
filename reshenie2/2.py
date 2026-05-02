tasks = []
today = []
tomorrow = []
other = []

run = True

while run:

    command = input("Введите команду: ")

    if command == "add":


        day = input('Введите дату: ')
        task = input('Введите задачу: ')


        if day=='Сегодня':
            today.append(task)
        if day=='Завтра':
            tomorrow.append(task)
        if day=='Другие':
            other.append(task)

    if command == "show":
        print(today)
        print(tomorrow)
        print(other)

    if command=='exit':
        print('Спасибо за использование! До свидания!')
        break
