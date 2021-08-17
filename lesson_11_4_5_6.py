class Warehouse:
    def __init__(self, warehouse):
        self.warehouse = warehouse

class OfficeAppliances:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Модель:': self.name, 'Стоимость:': self.price, 'Количество:': self.quantity}

    def income(self):
        try:
            name = input(f'Введите модель: ')
            price = int(input(f'Введите стоимость: '))
            quantity = int(input(f'Введите количество: '))
            item = {'Модель:': name, 'Цена:': price, 'Количество:': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение!')

class Printer(OfficeAppliances):
    pass

class Scanner(OfficeAppliances):
    pass

class Xerox(OfficeAppliances):
    pass

printer = Printer('OKI', 100, 10)
skaner = Scanner('HP', 200, 20)
xerox = Xerox('Epson', 300, 30)
printer.income()
skaner.income()
xerox.income()
