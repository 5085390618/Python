class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'\nМашина {self.name} остановилась.'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nСкорость машины {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость превышина. Скорость машины {self.speed}'
        else:
            return f'Скорость {self.name} нормальная'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость превышина. Скорость машины {self.speed}'
        else:
            return f'Скорость {self.name} нормальная'

class PoliceCar(Car):
    pass

town = TownCar('ГАЗ', 90, 'Белый', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('ВАЗ', 120, 'Красный', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.turn('налево'), sport.stop())

work = WorkCar('ПАЗ', 40, 'Жёлтый', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('налево'), work.stop())

police = PoliceCar('УАЗ', 60, 'Синий', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())
