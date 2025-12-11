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

#k = int(input())
#for j in range(1, k + 1):
#    for i in range(1, 10):
#        print(i, '*', j, '=', j * i, sep='', end='\t')
#    print()

#=================================
#========== NESTED LISTS =========
#=================================

table = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

combinations = [
    # horizontal
    *table, 

    # Vertical
    [table[0][0], table[1][0], table[2][0]],  # first column
    [table[0][1], table[1][1], table[2][1]],  # second column
    [table[0][2], table[1][2], table[2][2]],  # third column

    # Diagonal
    [table[0][0], table[1][1], table[2][2]],  # first 
    [table[0][2], table[1][1], table[2][0]],  # second 
]
# [print(x) for x in combinations]
x = []
o = []

while True:
    not_availables = set(x).union(o)
    availables = set([1, 2, 3, 4, 5, 6, 7, 8, 9]).difference(not_availables)
    if len(availables) == 0:
        print("Game overed evenly!")
        break

    x_ = input(f"❌ | Choose from: {str(availables)}: ")
    if len(x_) == 1 and x_.isnumeric() and int(x_) < 10 and int(x_) > 0:
        x.append(int(x_))
        found = False
        for comb in combinations:
            found = set(x).issuperset(set(comb))
        if found:
            print("X Won")
            break

    # -------------------------------------------
    # -------------------------------------------
    not_availables = set(x).union(o)
    availables = set([1, 2, 3, 4, 5, 6, 7, 8, 9]).difference(not_availables)
    if len(availables) == 0:
        print('   _______________________________')
        print('  /                              /|')
        print(' /                              / |')
        print('/______________________________/  |')
        print('|                              |  /')
        print("|     Game overed evenly!      | /")
        print('|______________________________|/')
        break


    o_ = input(f"⭕️ | Choose from: {str(availables)}: ")
    if len(o_) == 1 and o_.isnumeric() and int(o_) < 10 and int(o_) > 0:
        o.append(int(o_))
        found = False
        for comb in combinations:
            found = set(x).issuperset(set(comb))
        if found:
            print("O Won")
            break


        