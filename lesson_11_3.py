class OnlyNumber(ValueError):
    pass

box = []
while True:
    try:
        value = input('Введите число:')
        if value == 'stop':
            break
        if not value.isdigit():
            raise OnlyNumber(value)
        box.append(int(value))
    except OnlyNumber as exception:
        print('Введено не число:', exception)

print(box)
