run = True

while run:

    tasks = []
    today = []
    tomorrow = []
    other = []

    day = input('Введите дату: ')
    task = input('Введите задачу: ')
  

    if day=='Сегодня':
        today.append(task)
    if day=='Сегодня':
        tomorrow.append(task)
    if day=='Другие':
        other.append(task)

    if command=='exit':
        print('Спасибо за использование! До свидания!')
        break
