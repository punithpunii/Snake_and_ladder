#use case 2: The Player rolls the die to get a number between 1 to 6 

def snakeladder(pos):

    dice=random.randint(1,6)
    print("Rolled:",dice)
    pos+=dice
    if pos<100:
        print("Current position :",pos)
        pos=snakeorladder_check(pos)
    if pos>100:
        pos-=dice
        print("Current position :",pos)
        pos=snakeorladder_check(pos)
        
    return pos
