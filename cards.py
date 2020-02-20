import random
import sys 

#-------- deck creation -----------

deck = []
suits = ["♠", "♥", "♦", "♣"]
for i in range(4):
    suit = ""
    for j in range(1,14):
        value = str(j)
        suit = suits[i]
        if(j == 1):
            value = "A"
        elif(j == 11):
            value = "J"
        elif(j == 12):
            value = "Q"
        elif(j == 13):
            value = "K"
        deck.append(f"{value}{suit}")
print("Created: ")
print(deck)


#-------- deck shuffle (Fisher Yates)  -----------

def randomize (arr):
    n = len(arr)
    for i in range(n-1,0,-1): 
        j = random.randint(0,i+1) 
        arr[i],arr[j] = arr[j],arr[i] 
    return arr 

print("Shuffled: ")
print(randomize(deck))

#-------- deck sort -----------
def bubble_sort(arr):
    n = len(arr)
    s={"♠":0,"♥":1,"♦":2,"♣":3}
    f={"A":1,"J":11,"Q":12,"K":13}
    
    for i in range(n):
        for j in range(0, n-i-1):
            a = arr[j]
            b = arr[j+1]

            aface  = a[0:len(a)-1];
            asuit  = a[len(a)-1];
            avalue = f[aface] if aface in f else int(aface)

            bface  = b[0:len(b)-1];
            bsuit  = b[len(b)-1];
            bvalue = f[bface] if bface in f else int(bface)

            if (asuit > bsuit or (asuit == bsuit and avalue > bvalue)):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
def selectionSort(arr):
    f={"A":1,"J":11,"Q":12,"K":13}
    n = len(arr)
    for i in range(n): 
        min_idx = i 
        for j in range(i+1, len(arr)):
            a = arr[min_idx]
            b = arr[j]
            aface  = a[0:len(a)-1]
            asuit  = a[len(a)-1]
            avalue = f[aface] if aface in f else int(aface)

            bface  = b[0:len(b)-1]
            bsuit  = b[len(b)-1]
            bvalue = f[bface] if bface in f else int(bface)

            if (asuit > bsuit or (asuit == bsuit and avalue > bvalue)):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
  
selectionSort(deck)
print("Sorted: ")
print(deck)


