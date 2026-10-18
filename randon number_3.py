import random
random_number = random.randint(0,99)
print(random_number)
human_numder = int((input)('Введите целое число от 0 до 99:')) 

while human_numder != random_number:
    if human_numder > random_number:
        print ('Введенное число больше загаданного, введите число еще раз:')
    elif human_numder < random_number:
        print ('Введенное число меньше загаданного, введите число еще раз:')
    human_numder = int((input)('Введите целое число от 0 до 99:')) 
        
else: print ('Молодец! Вы угадали число!')  
