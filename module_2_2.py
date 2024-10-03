while True:
    try:
        first = int(input('Введите первое число: '))
        break
    except ValueError:
        print('Вы напечатали что-то другое')
        continue
while True:
    try:
        second = int(input('Введите второе число: '))
        break
    except ValueError:
        print('Вы напечатали что-то другое')
        continue
while True:
    try:
        third = int(input('Введите третье число: '))
        break
    except ValueError:
        print('Вы напечатали что-то другое')
        continue
arr = {first, second, third}
if len(arr) == 3:
    print(0)
elif len(arr) == 2:
    print(2)
elif len(arr) == 1:
    print(3)