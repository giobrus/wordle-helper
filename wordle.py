import os
import numpy as np
os.system('cls')

words = open("wordle.txt", "r").read().split(",")
words = [x[1:-1] for x in words]

y = np.zeros(5, dtype=str)
for i in range(0, len(y)):
    y[i] = input("letter in position "+str(i)+"? ")

for i in range(0, len(y)):
    if y[i] != "":
        words = [x for x in words if x[i] == y[i]]
    else:
        continue

for word in words:
    print(word)
