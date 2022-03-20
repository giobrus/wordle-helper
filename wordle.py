import os
import numpy as np
os.system('cls')

words = open("wordle.txt", "r").read().split(",")
words = [x[1:-1] for x in words]

y = np.zeros(5, dtype=str)
for i in range(0, len(y)):
    y[i] = input("letter in position "+str(i+1)+"? ")

black = np.zeros(int(input("how many")), dtype=str)
for i in range(0, len(black)):
    black[i] = input("black letter number "+str(i+1)+": ")

for i in range(0, len(y)):
    if y[i] != "":
        words = [x for x in words if x[i] == y[i] and set(x).isdisjoint(black)]
    else:
        continue

print("\nPossible solutions:")

for word in words:
    print(word)
