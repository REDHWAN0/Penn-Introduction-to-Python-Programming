#here is a string with my favorite restaurant
my_restaurant_choice = 'Mcdonalds'

#convert the string to a list
my_restaurant_choice_list = list(my_restaurant_choice)
#update the third item in the list
my_restaurant_choice_list[2] = 'D'
#covert the list back to a string
my_restaurant_choice = ''.join(my_restaurant_choice_list)

print(my_restaurant_choice)