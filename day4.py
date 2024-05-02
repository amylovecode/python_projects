import random 

#generate a random number between 1 and 10, inclusive [1,10]
random_integer = random.randint(1, 10)
print(random_integer)

#generate a random float number between 0 and 1, 1 is not inclusive, [0.0, 1.0)
random_float = random.random()
print(random_float) 

#generate a decimal number between 0 and 5, [0,5)
random_number = 5 * random.random()
print(random_number)