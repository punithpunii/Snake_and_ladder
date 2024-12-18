#use case 5:  Ensure the player gets to exact winning position 100

import random

def play_game():
    player1_pos=0
    p2_dice_rolled_count=0
    while True:
        print("Player 1 turn, pos :",player1_pos)
        player1_pos=snakeladder(player1_pos)
        p1_dice_rolled_count+=1
        if player1_pos==100:  #use case 5 
            print("Player 1 won by reaching 100 first")
            break
play_game()

def snakeladder(pos):

    dice=random.randint(1,6)
    print("Rolled:",dice)
    pos+=dice
    if pos<100:
        print("Current position :",pos)
        pos=snakeorladder_check(pos)
    if pos>100: #the player stays in the same position till the player gets the exact number that adds to 100
        pos-=dice
        print("Current position :",pos)
        pos=snakeorladder_check(pos)
        
    return pos

def snakeorladder_check(pos):
 
    check_roll=random.randint(1,3)

    if check_roll==1: # Snake
        return event_snake(pos)

    elif check_roll==2 and pos<=94:   # Ladder
        return event_ladder(pos)
    else:  # No Play
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

