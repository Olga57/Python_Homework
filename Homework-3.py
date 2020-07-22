#Задание 1 - позиционные аргументы, деление
def div_func (*args):
    try:
        arg1=int(input('Введите делимое: '))
        arg2=int(input('Введите делитель: '))
        result=arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return 'Некорректный делитель. На ноль делить нельзя'
    return result
print(f'result {div_func()}')

#Задание 2 -именованные аргументы
def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Tsybakova', name='Olga', year='1982', city='Moscow', email='olga_subbotkina@mail.ru',
              telephone='8-903-264-91-69'))

#Задание 3 - позиционные аргументы, сумма наибольших двух
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')

#Задача №4 - возведение в степень
def power(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res

print(power(float(input("Первое значение - ")), int(input("Второе значение - "))))

#Задание 5 -
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
        print(f'Your final sum is {sum_res}')

#Задание 6
def int_func (*args):
    word = input("Input words ")
    print(word.title())
    return
int_func()
