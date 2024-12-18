#use case 3:  Player then checks for No Play, Ladder or Snake

import random

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

