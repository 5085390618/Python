class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2000 <= year < 2022:
                    return f'Корректная дата'
                else:
                    return f'Год некорректен'
            else:
                return f'Месяц некорректен'
        else:
            return f'День некорректен'

    def __str__(self):
        return f'Сегодня: {Data.extract(self.day_month_year)}'


today = Data('16 - 8 - 2021')
print(today)
print(Data.valid(11, 11, 2023))
print(today.valid(11, 13, 2020))
print(Data.extract('16 - 08 - 2020'))
print(today.extract('16 - 08 - 2021'))
print(Data.valid(16, 8, 2021))
