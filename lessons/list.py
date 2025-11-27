#l = ['apple', 'banana', 'orange', 'strawberry']
#longest_word = ''
#
#for word in l:
#    if len(longest_word) < len(word):
#        longest_word = word
#print(longest_word)

numbers = [1, 2, 3, 4, 5, 6, 7]
#total = 0
#max_num = numbers[0]
#min_num = numbers[0]

#for num in numbers:
#    total += num
#print(total)

#for num in numbers:
#    if max_num < num:
#        max_num = num
#    elif min_num > num:
#        min_num = num
#    
#print(max_num)
#print(min_num)

# ================================
# ========== TUPLE ===============
# ================================

k = int(input())
for j in range(1, k + 1):
    for i in range(1, 10):
        print(i, '*', j, '=', j * i, sep='', end='\t')
    print()