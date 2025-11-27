# ===================================================
# THEME: Boolean
# ===================================================

#numbers = '153429786'
#sum_ = 0
#max_ = 0
#second_max = 0

#for letter in numbers:
#    num = int(letter)
#    sum_ += num
#    if num > max_:
#        max_ = num
#
#
#print('The sum is: ', sum_)
#print('The max is: ', max_)
#print('The second max is: ', second_max)

#temperature = float(input('Enter the temperature: '))
#cold = 15.5
#hot = 28
#
#if temperature <= cold:
#    print('ХОЛОДНО')
#elif temperature >= hot:
#    print('ЖАРКО')
#else:
#    print('НОРМАЛЬНО')

#password = input()
#confirm = input()
#
#if len(password) < 8:
#    print('Korotko')
#elif password != confirm:
#    print('Razlichayutsya')
#else:
#    print('OK') 

#while True:
#    n = int(input())
#    if n == 0:
#        break
#    print(n)
#

#         || 
#         || 
#        \  /
#         \/


#n = int(input())
#while n != 0:
#    print(n)
#    n = int(input())

#numbers = []
#
#while True:
#    n = int(input())
#    if n == 0:
#        break
#    numbers.append(n)
#
#for num in numbers:
#    print('...')
#    print(num)

n = int(input())
found_cat = False

for _ in range(n):
    line = input()
    
    # если нашли кота
    if "кот" in line or "Кот" in line:
        found_cat = True
    
    # если нашли пса — кот теряется
    if "пёс" in line or "Пёс" in line:
        found_cat = False

print("МЯУ" if found_cat else "НЕТ")

# ===================================================

n = int(input())  # запас терпения учителя

expected = ["раз", "два", "три", "четыре"]
index = 0  # на каком слове сейчас должны быть
correct_count = 0  # количество правильных подряд
mistakes = 0  # число ошибок

while mistakes < n:
    try:
        word = input()
    except EOFError:
        break  # если ввод закончился

    if word == expected[index]:
        correct_count += 1
        index = (index + 1) % 4  # циклическое переключение 0→1→2→3→0
    else:
        mistakes += 1
        print(f"Правильных отсчётов было {correct_count}, но теперь вы ошиблись.")
        correct_count = 0
        index = 0  # начинаем заново с «раз»

print("На сегодня хватит.")

# ===================================================

while True:
    try:
        parts = input().strip().split()
    except EOFError:
        break

    if not parts:
        continue

    # Форматы:
    # a op
    # a op b

    # --- операции без второго числа ---
    if len(parts) == 2:
        a, op = parts
        try:
            a = int(a)
        except:
            continue

        # факториал
        if op == '!':
            if a < 0:
                continue
            fact = 1
            for i in range(1, a + 1):
                fact *= i
            print(fact)

        # завершение
        elif op == 'x':
            print(a)
            break

        continue

    # --- операции с двумя числами ---
    if len(parts) == 3:
        a, op, b = parts
        try:
            a = int(a)
            b = int(b)
        except:
            continue

        try:
            if op == '+':
                print(a + b)
            elif op == '-':
                print(a - b)
            elif op == '*':
                print(a * b)
            elif op == '/':
                print(a // b)
            elif op == '%':
                print(a % b)
        except:
            continue

# ===================================================

# читаем первую цену
prev = int(input())
if prev == 0:
    exit()

buy = None
sell = None

while True:
    price = int(input())
    if price == 0:
        break

    # ещё не купили — ищем рост
    if buy is None:
        if price > prev:
            buy = price
    else:
        # купили — ищем падение
        if price < prev:
            sell = prev
            break

    prev = price

# вывод результата
profit = sell - buy
print(buy, sell, profit)

need = int(input())
count = 0
done = False

# ===================================================

while True:
    line = input().strip()

    if line == "КОНЕЦ":
        break

    if done:       # если уже собрали — всё игнорируем
        continue

    if "доска" in line or "дощечка" in line:
        count += 1
        print(f"Прибили {count} дощечку.")
        if count == need:
            print("ГОТОВО")
            done = True

if not done:       # дошли до КОНЕЦ, а досок мало
    print("МАЛОВАТО")
