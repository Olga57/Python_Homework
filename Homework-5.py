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
with open ('salaries.txt') as f:
    salaries = []
    lines = f.readlines()
    for line in lines:
        name,salary = line.split('-')
        salaries.append(int(salary))
        if int(salary)<20000:
            print (line, end='')
    print('\nСредняя зп:', sum(salaries / len(salaries)))

#Задание 4 - перевод на др. язык
with open ('english.txt', encoding='utf-8') as f:
    lines=f.readlines()

with open ('russian.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        if '1' in lines:
            line=line.replace('One', 'Один')
        elif '2' in lines:
            line=line.replace('Two', 'Два')
        elif '3' in lines:
            line = line.replace('Three', 'Три')
        elif '4' in lines:
            line=line.replace('Four', 'Четыре')
        f.write(line)
#Задание 5 - запись набора числе в файл, подсчет суммы чисел в файле
with open ('number.txt', 'w') as f:
    numbers=input('Введите целые числа через пробел:')
    f.write('Введенные числа:' +numbers+'\n')
    numbers=map(int,numbers.split())
    sum_numbers=sum(numbers)
    f.write('Сумма чисел:' +str(sum_numbers))
    print('Сумма введенных чисел:',sum_numbers)
print('Все записано')

#Задание 6 - создание словаря по данным файла
my_dict = dict()
with open('les.txt',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        splitted_line=line.split()
        subject=splitted_line[0]
        sum_lessons=sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '('in x])
        my_dict[subject]=sum_lessons
print(my_dict)



