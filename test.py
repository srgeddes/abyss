import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use random.sample() to get 5 unique random elements from my_list
selected_numbers = random.sample(my_list, 5)

# Now selected_numbers contains the 5 unique random numbers
print(selected_numbers)

del selected_numbers[0]

print(selected_numbers)
print(selected_numbers[0])
