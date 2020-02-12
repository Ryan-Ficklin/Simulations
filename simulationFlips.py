import random

numFlips = int(input("How many flips? "))

flips = [0] * numFlips
heads = 0
tails = 0
doubleHeads = 0

for i in range(numFlips):
    flip = random.randint(0,1)
    flips[i] += flip

for i in range(len(flips)):
    if(flips[i] == 0):
        tails+=1
    elif(flips[i] == 1):
        heads+=1

print(f"{heads} Heads {heads/numFlips*100}%, {tails} Tails {tails/numFlips*100}%")
    
for i in range(len(flips)):
    if(flips[i:i+3] == [0,0,1]):
        doubleHeads+=1
    #print(flips[i])


print(f"Heads shows up twice in a row {doubleHeads} times")
