#iterate over sentence of 10 numbers, 0-9
for x in range(10):
    print(x)
    
print(' ')
#iterate over sentence of 10 numbers, 0-9
for x in range(0, 10):
    print(x)
    
print(' ')
#iterate over sentence of 5 numbers, 1-6
for x in range(1, 7):
    print(x)
    
print(' ')
#iterate over sentence of 6 numbers, 0-28 ,skipping every 6 numbers
for x in range(0, 30, 7):
    print(x, end = ' ')
    
print(' ')
#iterate over sentence of 6 numbers, 0-28 , counting backwords from 5-0
for x in range(5, -1, -1):
    print(x, end = ' ')
    
print(' ')
#find the number between 1 and 1200 that are odd
odd_numbers = []
for number in range(1, 1200):
#if odd, append ot odd number list
    if (number % 2 !=0):
        odd_numbers.append(number)

print(odd_numbers)
    

