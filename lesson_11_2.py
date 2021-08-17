class Exception(Exception):
    def __init__(self, exception):
        self.exception = exception

def div():
    try:
        divisible = int(input('Делимое: '))
        divider = int(input('Делитель: '))
        if divider == 0:
            raise Exception('!!! Деление на ноль !!!')
        else:
            res = divisible / divider
            return res
    except Exception as err:
        return err

print(div())
