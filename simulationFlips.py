import random

numFlips = int(input("How many flips? "))

flips = [0] * 2

for i in range(numFlips):
    flip = random.randint(0,1)
    flips[flip-1] += 1

print("0 is tails, 1 is heads")
for i in range(len(flips)):
    print(f"{i}: {flips[i]}/{numFlips} = {flips[i]/numFlips*100}%")

