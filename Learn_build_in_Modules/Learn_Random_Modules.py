import random

# List out all the attribute in the random module
# print(dir(random))

# Generate random number with in the default range -0.0 to 1.0
print(random.random())

# Float[10 to 20]
print(random.uniform(10, 20))


print(random.randint(10 , 20))

#Odd
print(random.randrange(1, 10, 2)) #[1,3,5,7,9]


# choice
lst = ['dev', 'test', 'devops', 'ds']
print(random.choice(lst))
