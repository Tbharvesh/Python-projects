import random

numberOfNames = int(input("How many names to choose from? "))
names = []
lower_limit = 0

for x in range(numberOfNames):
    names.append(input("What is the name?"))

randomNumber = random.randint(lower_limit, numberOfNames)
print(names[randomNumber])