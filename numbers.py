my_list = []
print(type(my_list))
my_list = list()
print(type(my_list))

#   0, 1, 2,  3,  4 
numbers = [2, 6, 10, 12.5, 0 ] #this is also comment
print(numbers)
print(type(numbers))

print(numbers[1])
print(type(numbers[1]))
print([2, 6, 10, 12.5, 0][1])
print(6)
print(numbers[1]*2.5)
print(type(numbers[1]*2.5))

# name_of_list_list_we_want_to_index[index]
print(numbers[3])
print(type(numbers[3]))


foods = ["pizza", "tacos", "dimsum", "pussy"]
print(foods [3])
print(type(foods[3]))
print(foods[3].upper())

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods.append("cheeseburger"))
print(foods)
# THIS DOES NOT WORK!!!!
# foods = foods.append("cheeseburger")
# print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods)
foods.remove("pizza")
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods.pop())
print(foods)
