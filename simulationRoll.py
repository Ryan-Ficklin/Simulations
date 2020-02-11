import random
import math

roll = random.randint(1,6)
counter1 = 0
counter2 = 0
counter3 = 0 
counter4 = 0
counter5 = 0
counter6 = 0
numRoll = int(input("How many times would you like to roll?: "))
for i in range (numRoll):
    roll = random.randint(1,6)
    if(roll == 1):
        counter1+=1
    if(roll == 2):
        counter2+=1
    if(roll == 3):
        counter3+=1
    if(roll == 4):
        counter4+=1
    if(roll == 5):
        counter5+=1
    if(roll == 6):
        counter6+=1
    
percent1 = (counter1/numRoll) * 100
percent2 = (counter2/numRoll) * 100
percent3 = (counter3/numRoll) * 100
percent4 = (counter4/numRoll) * 100
percent5 = (counter5/numRoll) * 100
percent6 = (counter6/numRoll) * 100
print("1: " + str(counter1) + "/" + str(numRoll) + " " + str((percent1)) + "%")
print("2: " + str(counter2) + "/" + str(numRoll) + " " + str((percent2)) + "%")
print("3: " + str(counter3) + "/" + str(numRoll) + " " + str((percent3)) + "%")
print("4: " + str(counter4) + "/" + str(numRoll) + " " + str((percent4)) + "%")
print("5: " + str(counter5) + "/" + str(numRoll) + " " + str((percent5)) + "%")
print("6: " + str(counter6) + "/" + str(numRoll) + " " + str((percent6)) + "%")

    
    
    
