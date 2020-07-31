#Задание 1 - создание файла в текстовом формате
with open('text.txt','w') as f:
    while True:
        line=input('Введите строку: ')
        if line=='':
            break
        f.write(line+ '\n')

#Задание 2 - сохранение строк в файле, подсчет строк и слов
with open ('text.txt') as f:
    lines=f.readlines()
    print=('Количество строк:',len(lines))
    for num_line,line in enumerate(lines, start=1):
        print('{} строка содержит- {} слов'.format(num_line, len(line.split())))

#Задание 3 - фильтр оклад менее 20 тыс. руб.