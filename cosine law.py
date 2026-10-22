import math
side_1 = float((input)('Всем привет! Введите длину первой стороны треугольника: '))
side_2 = float((input)('Введите длину второй стороны треугольника: '))
angle_deg = float((input)('Введите угол между данными сторонами треугольника: '))
angle_rad = math.radians(angle_deg)
side_3 = math.sqrt((side_1)**2+(side_2)**2 - 2*side_1*side_2* (math.cos(angle_rad)))
print('Длина третьей стороны треугольника равна', side_3)
