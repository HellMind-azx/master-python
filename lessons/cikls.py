# num = 10
# while num > 0:
#    print('Counter: ' + str(num))
#    num -= 1
#
# print('Vse koncheno!')

# number = int(input('Vvedite chislo: '))
# while number > 0:
#    print('Вы ввели положительное число: ' + str(number))
#    number = int(input())
#    print('Введите следующее число: ')
#    break
# print('Вы ввели отрицательное число или ноль.')

# count = 0
# number = int(input('write a number: '))
# while number % 2 != 0:
#    number = int(input('Write an even number: '))
#    if number % 2 == 0:
#        print('You write an even number , bro!')
#        break

#enter_number = input('Vvedite chislo: ')
#random_num = 54
#lives = 3
#while enter_number.isnumeric():
#
#    if int(enter_number) == random_num:
#        print('You win! Congrats from Bill Jigsaw!')
#        break
#    else:
#        lives -= 1
#        print('Ne pravilno ! U vas ostalos ' + str(lives) + ' popitok')
#        enter_number = input('Vvedite chislo: ')
#    if lives == 0:
#        print('U vas ne ostalos popitok. Igra zakonchena!')
#        break

#                              ===========================================
#                              ==============  CIKL FOR ==================
#                              ===========================================

#for i in range(20, 10, -2):
#    print('Counter: ' + str(i))

#enter_number2 = int(input('Vvedite chislo: '))
#for i in range(enter_number2):
#    print('Number: ' + str(i))

#total = 0
#for i in range(4):
#    number = float(input('Vvedite chislo: '))
#    total = number
#print('Summa vvedennih chisel: ' + str(total))

#n = int(input('Vvedite chislo: '))
#total = 0
#for i in range(n):
#    print('Chislо ', i)
#    total += i
#    print('Summa vvedennih chisel: ' + str(total))
#print('Obshaya summa: ' + str(total))

#======================================================================
#first_num = int(input('Vvedite pervoe chislo: '))
#last_num = int(input('Vvedite poslednee chislo: '))
#summ = 0
#for i in range(first_num, last_num):
#    summ += i
#print('Summa chisel ot ' + str(first_num) + ' do ' + str(last_num) + ' ravna: ' + str(summ))
#======================================================================

#======================================================================
#first_number = int(input('Vvedite pervoe chislo: '))
#last_number = int(input('Vvedite poslednee chislo: '))
#
#for i in range(first_number, last_number):
#    if i % 2 == 0:
#        print('Chetnoe chislo: ' + str(i))
#======================================================================

#======================================================================
#number = int(input('Vvedite chislo: '))
#count_of_str = int(input('Vvedite kolichestvo strok: '))
#result = 0
#for i in range(count_of_str):
#    result = i * number
#    print(i, '*', number, '=' , result)
##======================================================================

# ===================================================
# ==============  NESTED LOOPS  =====================
# ===================================================

#n = int(input())  # ввод числа от 2 до 8
#
#for i in range(1, n + 1):         # внешний цикл — номер строки
#    for j in range(i):            # внутренний цикл — повторяем i раз
#        print(i, end='')          # выводим номер строки без переноса
#    print()                        # после внутреннего цикла перевод строки

# ===================================================

#n = int(input())  # ввод размера таблицы
#
#for i in range(1, n + 1):         # строки
#    for j in range(1, n + 1):     # столбцы
#        print(i * j, end='\t')    # выводим результат с табуляцией
#    print()                       # переход на новую строку после каждого ряда

#n = int(input())
#for i in range(1, n + 1):
#    for j in range(i):
#        print(i , end='')

#N = int(input())
#
#current = 1  
#
#for i in range(1, N + 1):       
#    for j in range(i):
#        if current > N:
#            break
#        print(current, end=' ')
#        current += 1
#    print()


#roads = int(input())
#
#best_height = 0
#best_road = 0
#
#for road_num in range(1, roads + 1):
#    tunnels_count = int(input())
#    min_height = float('inf') 
#
#    for _ in range(tunnels_count):
#        h = int(input())
#        if h < min_height:
#            min_height = h  
#
#    if min_height > best_height:
#        best_height = min_height
#        best_road = road_num
#
#print(best_road, best_height)

