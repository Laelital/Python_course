# Напишите метод, который будет вычислять угол между часовыми и минутными стрелками часов. На вход функции подаётся время в виде двух переменных: "hours" и "minutes".
# Расчет угла производить относительно реального поведения стрелок часов.

# def method_corner1(hours: int, minutes: int):
#     if 0 <= hours <=11 and 0 <= minutes <= 60:
#         return minutes*6 - (hours + minutes/60) * 30
#     else:
#         return None

# print(method_corner1(0, 59))

def method_corner(hours: int, minutes: int):
    if 0 <= hours <=11 and 0 <= minutes <= 60:
        corner_m = minutes*6
        corner_h = (hours + minutes/60) * 30
        if abs(corner_m-corner_h) > 180:
            return abs(corner_h-corner_m)
        else: 
            return abs(corner_m-corner_h)
    else: 
        return None
    
print(method_corner(6, 5))