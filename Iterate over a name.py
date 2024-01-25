name= input('what is your name?')

letter_count = 0
print(name, 'is spelled:')
for x in name:
    print(x, end = ' ')
    letter_count += 1
    
print(' ')
print(letter_count, 'letter in the name', name)