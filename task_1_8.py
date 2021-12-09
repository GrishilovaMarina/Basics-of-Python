class Date:
    DATA = ''
    def __init__(self, data):
        Date.DATA = str(data)
    def __str__(self):
       return Date.DATA

    @classmethod
    def transformation(cls):
        data_num = []
        for i in range(len(cls.DATA.split('-'))):
            data_num.append(cls.DATA.split('-')[i])
        return f'{data_num[0]}.{data_num[1]}.{data_num[2]}'

    @staticmethod
    def val():
        my_dict = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
        k = Date.DATA.split('-')[1]
        if k in my_dict:
            if my_dict[Date.DATA.split('-')[1]] >= int(Date.DATA.split('-')[0]):
                return
            else:
                print("Неверное число дней в месяце")
        else:
            print('Неверный номер месяца')

a = Date(input("Введите дату в формате 'день-месяц-год':  "))
a.val()
print(a.transformation())
