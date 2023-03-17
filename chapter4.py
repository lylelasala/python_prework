foods = [ "pizza", "tacos", "dim sum", "sushi"]

print(foods[1])

#for PLACEHOLDER in THE_LIST_WE_WANT_TO_LOOK_AT:
    # this is a code block
    # this code block
    # will run every every item in the list
for food in foods:
    if food == "dim sum":
        continue
    print(f"I like (food) because they are yummy")

for index in range(len(foods)):
    print(index)
    print(foods[index])

print(list(enumerate(foods)))
for index, food in enumerate(foods):
    print(f"My No {index + 1} food is {food.title()}")
                                         
# Loop of the index
print(list(range(len(foods))))
print(len(foods))                                         



my_tup = 1, 2
print(type(my_tup))
my_tup = (1,2)
print(type(my_tup))
print(my_tup)

print(my_tup[1])

for num in my_tup:
    print(my_tup)
#Slicing

my_string = "Hey Guy Let Learn Python"
my_list = ["pizza", "taco", "dim sum", "sushi"]

print(my_list[1:])