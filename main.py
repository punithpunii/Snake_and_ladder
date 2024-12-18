#use case 4:  Repeat till the Player reaches the winning position 100

import random

def play_game():
    player1_pos=0
    p2_dice_rolled_count=0
play_game()

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

def snakeorladder_check(pos):
 
    check_roll=random.randint(1,3)

    if check_roll==1:
        return event_snake(pos)

    elif check_roll==2 and pos<=94:
        return event_ladder(pos)

    return pos

def event_snake(pos):
    print("  Encountered snake at pos:",pos)
    snake_roll=random.randint(1,6)
    print("  snake_rolled",snake_roll)
    pos-=snake_roll
    print("  After snake encounterd, position is:",pos)
    return pos

def event_ladder(pos):
    print("  Encountered ladder at pos:",pos)
    ladder_up=random.randint(1,6)
    print("  ladder_rolled",ladder_up)
    pos+=ladder_up
    print("  After ladder encountered, position is:",pos)
    return pos

