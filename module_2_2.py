first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
arr = {first, second, third}
if len(arr) == 3:
    print(0)
elif len(arr) == 2:
    print(2)
elif len(arr) == 1:
    print(3)