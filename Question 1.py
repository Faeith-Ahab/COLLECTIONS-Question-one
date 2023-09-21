# COLLECTIONS
# Consider a list that
# Takes in positive integers a = [1,1,2,3,5,8,13,21,34,55,89]
# Write a program that prints all the elements of that list that are less that 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 24, 55, 89]
for item in a:
    if item<5:
        print(item)

#  Creating a new list for items less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 24, 55, 89]
new_list = []
for item in a:
    if item<5:
        new_list.append(item)
        new_list.sort()
        print(new_list)






