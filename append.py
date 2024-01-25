numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
even_count = 0
for number in numbers:
    if(number % 2 == 0):
        even_numbers.append(number)
        even_count += 1
    
print(even_numbers)
print('There are', even_count, 'numbers in the even list')
