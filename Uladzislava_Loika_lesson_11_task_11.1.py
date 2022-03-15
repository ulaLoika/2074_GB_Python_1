class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def splitting(cls, date_obj):
        return [int(i) for i in (date_obj.date.split('-'))]

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Дата верна.'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {self.date}'


today = Date('11-1-2001')
fail_date = Date('12/12-12')
day, month, year = Date.splitting(today)
day_fail, month_fail, year_fail = Date.splitting(fail_date)

print(day, month, year)
print(Date.valid(day, month, year))
print(Date.valid(day_fail, month_fail, year_fail))
print(today)
