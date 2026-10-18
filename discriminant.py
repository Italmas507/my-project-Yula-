import math
a = float((input)('Введите коэффициент а: '))
b = float((input)('Введите коэффициент b: '))
c = float((input)('Введите коэффициент c: '))
D = b**2-4*a*c
print ('Дискриминант равен ', D)
if D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print ('Ответ: x1 = ', x1, ', x2 = ', x2)
elif D == 0:
    x = -b /2*a
    print ('Ответ: x = ', x)
elif D < 0:
    print ('Ответ: Действительных корней нет')
