import random


a = random.randint(1, 100)
b = random.randint(1, 100)
c = a + b
x = random.randint(1, 100)
z = x + b * c
k = (random.randint(1, 100) + z) * 5
print("k ravno " + str(k))
for m in range(4):
    k = k + m
k = k / 12
print("k ravno " + str(k))
