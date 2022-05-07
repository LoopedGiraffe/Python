import random
#import my_module

random_integer = random.randint(1, 10)
print(random_integer)

#print(my_module.pi)


#0.00000... - 0.99999...
random_float = random.random()
print(random_float)

#0.000.... - 4.999999...
randfive = random_float * 5
print(randfive)

#random score for love test ;)
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")