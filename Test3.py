
class BaseConverter:                      
    def __init__(self):
        pass
        
    def convert(self, celsius: float, to_unit):
        if to_unit == 'k':
            return celsius + 273.15
        elif to_unit == 'f':
            return celsius * 1.8 + 32
        else:
            return None
converter = BaseConverter()

celsius = input('Введите температуру в градусах Цельсия: ')
t = converter.convert(celsius, input('Введите "k" для перевода в Кельвины, "f" для перевода в Фаренгейты: '))
print('Температура = ', t)

print(converter.convert(input(), input()))
