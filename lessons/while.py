# while True:
#    s = input()
#    if s == '':
#        break
#    print(s)

# total = 0.0
#

# =================================

# while True:
#    price = float(input())
#    if price < 0:
#        break
#    if price > 1000:
#        price *= 0.95
#    total += price
# print(total)

# ==================================

# total = 0
#
# while True:
#    price = float(input('Enter a price (negativa number - break process): '))
#
#    if price < 0:
#        break
#
#    elif price > 1000:
#        price *= 0.95
#
#    total += price
# print('Total price: ', total)

# =================================

# +price = float(input("Введите цену товара: "))
# +total = 0
# +
# +while price >= 0:  # пока цена не отрицательная
# +    if price > 1000:
# +        price *= 0.95
# +    total += price
# +    price = float(input("Введите цену товара: "))
# +
# +print("Общая стоимость:", total)

# count = 0            # количество подходящих кандидатов
# min_height = None    # минимальный рост
# max_height = None    # максимальный рост
#
# while True:
#    data = input("Введите рост претендента (или '!' для окончания): ")
#    if data == "!":
#        break
#
#    height = int(data)
#
#    # учитываем кандидата
#    count += 1
#
#    # если это первый кандидат — задаём минимальный и максимальный рост
#    if min_height is None or max_height is None:
#        min_height = max_height = height
#    else:
#        # обновляем минимальный и максимальный рост
#        if height < min_height:
#            min_height = height
#        if height > max_height:
#            max_height = height
#
# вывод результатов
# if count > 0:
#    print(count)
#    print(min_height, max_height)
# else:
#    print("Нет данных о росте")

# ================================

# count = 0
#
# while True:
#    text = input()
#    count += 1
#    if text == "Спасибо.":
#        break
#
# print(count)

# ================================

#total = 0
#count = 0
#
#while True:
#    temp = float(input())
#    if temp < -300:
#        break
#    total += temp
#    count += 1
#    
#average = total / count
#
#print(average)

while True:
    password1 = input("Введите пароль: ")
    password2 = input("Повторите пароль: ")

    if len(password1) < 8:
        print("Короткий! Попробуйте снова.")
    elif "123" in password1:
        print("Простой! Попробуйте снова.")
    elif password1 != password2:
        print("Различаются. Попробуйте снова.")
    else:
        print("OK")
        break


while True:
    n = int(input())
    if n % 10 != 0:
        break
    print(n)
 