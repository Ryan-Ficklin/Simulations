deck = []
suits = ["♠", "♥", "♦", "♣"]
for i in range(4):
    suit = ""
    for j in range(1,14):
        value = str(j)
        suit = suits[i]
        if(j == 1):
            value = "A"
        if(j == 11):
            value = "J"
        elif(j == 12):
            value = "Q"
        elif(j == 13):
            value = "K"
        deck.append(f"{value}{suit}")

print(deck)
