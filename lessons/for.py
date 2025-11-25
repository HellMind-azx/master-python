#total = 0
#for i in range(3):
#    price = float(input())
#    total = total + price
#print('Сумма введённых чисел равна', total)

#n = int(input())
#total = 0
#for i in range(n):
#    print('Рассматриваем число', i)
#    total += i
#    print('Промежуточная сумма равна', total)
#print('Итоговая сумма всех этих чисел равна', total)

#for i in range(8):
#    count_of_string = input()+
#    print(count_of_string, end="")

#sep = input()
#word1 = input()
#word2 = input()
#word3 = input()
#
#print(word1, word2, word3, sep=sep)


#phrase = input()
#n = int(input())
#for i in range(n):
#    print(phrase)

#n = int(input())
#for i in range(n+1):
#    print(i, end=" ")

#n = int(input())
#for i in range(n):
#    cube = i ** 3
#    print(f'Куб числа {i} равен {cube}')

#for i in range(7):
#    if i == 0:
#        continue
#    total = 0
#    total += i * 2
#print(total)

#n = int(input())
#m = int(input())
#for i in range(n, 31, m):
#    print(i)

#sec = int(input())
#for i in range(sec, -1, -1):
#    print('Осталось секунд:', i)
#print('Пуск')

#h = int(input())
#
#for i in range(1, h + 1):
#    print(' ' * (h - i) + '*' * (2 * i - 1))


#n = int(input())
#found = False
#
#for i in range(n):
#    line = input()
#    if "Кот" in line or "кот" in line:
#        found = True
#
#if found:
#    print("МЯУ")
#else:
#    print("НЕТ")

#line_number = 0
#found = -1
#
#while True:
#    line = input()
#    line_number += 1
#
#    if line == "СТОП":
#        break
#
#    if "Кот" in line or "кот" in line:
#        found = line_number
#        break
#
#print(found)


#total = 0
#count = 0
#
#while True:
#    n = int(input())
#    total += n
#    count += 1
#
#    if n == 0:
#        break
#    if total == 10:
#        break
#print(count)
    

#while True:
#    n = int(input())
#
#    if n == 0:         
#        break
#
#    if n % 3 == 0 and n % 7 == 0:
#        print("Караул!")
#        break
#
#    if n % 3 == 0:
#        print("несчастливое")
#        continue
#
#    if n % 7 == 0:
#        print("опасное")
#        continue



