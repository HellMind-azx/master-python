# THEHE: DEBUGGING

# ERRORS :
# 1. SyntaxError: Occurs when the code is not written in proper Python syntax.
# Example: print("Hello World"
# Fix: print("Hello World")

# 2. Run time Error: Occurs during the execution of the program, causing it to crash.
# Example: result = 10 / 0
# Fix: Check for division by zero before performing the operation.
# if divisor != 0:
#     result = 10 / divisor

# 3. TypeError: Occurs when an operation is performed on incompatible data types.
# Example: result = '5' + 10
# Fix: Convert the string to an integer before performing the addition.
# result = int('5') + 10

#num1 = 10
#num2 = 0
#
#print('wait a moment...')
#print('calculating...')
#print('-' * 20)
#print(f'{num1} / {num2} = {num1 / num2}')

#n = int(input("Введите число: "))
#factorial = 1
#
#for i in range(1, n + 1):
#    factorial *= i
#print('Factorial number :', factorial) 

#first = 0
#second = 1
#n = int(input('Enter num: '))
#
#for i in range(n - 1):
#    first, second = second, first + second
#
#print(first)

number = int(input('Enter num: '))

