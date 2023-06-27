import random
import time

room_size = 3

player_coordinate = {'x': room_size, 'y': room_size, 'v': 'n'}
monster_coordinate = {'x': 1, 'y': 1, 'v': 's'}

step_counter = 0

Game_over = False

start_text = "You are placed in a dark room with a monster, and your task is to avoid meeting him for 30 turns.\nYour hands will tell you if you stumble on a wall, and your sensitive hearing will give you an idea of how far away the monster is.\nUse the 'forward', 'right', 'left', 'back' commands to move, or any other command to stay in place.\n"

speed = 0.01

print(start_text)


def vector_back(current_vector):
    if current_vector == 'n':
        return 's'
    if current_vector == 'e':
        return 'w'
    if current_vector == 's':
        return 'n'
    if current_vector == 'w':
        return 'e'


def vector_left(current_vector):
    if current_vector == 'n':
        return 'w'
    if current_vector == 'e':
        return 'n'
    if current_vector == 's':
        return 'e'
    if current_vector == 'w':
        return 's'


def vector_right(current_vector):
    if current_vector == 'n':
        return 'e'
    if current_vector == 'e':
        return 's'
    if current_vector == 's':
        return 'w'
    if current_vector == 'w':
        return 'n'


def step(current_vector):
    if current_vector == 'n':
        player_coordinate['y'] -= 1
    if current_vector == 'e':
        player_coordinate['x'] += 1
    if current_vector == 's':
        player_coordinate['y'] += 1
    if current_vector == 'w':
        player_coordinate['x'] -= 1


def wall_message():
    print('there is a wall in front of you')


def wall_checker():
    if player_coordinate['x'] == room_size and player_coordinate['v'] == 'e':
        return False
    elif player_coordinate['x'] == 1 and player_coordinate['v'] == 'w':
        return False
    elif player_coordinate['y'] == 1 and player_coordinate['v'] == 'n':
        return False
    elif player_coordinate['y'] == room_size and player_coordinate['v'] == 's':
        return False
    else:
        return True

def monster_choice_randomizer():
    monster_choice = random.choice('nesw')
    return monster_choice


def monster_step():
    if distance_checker() < 2:
        monster_coordinate['x'] = player_coordinate['x']
        monster_coordinate['y'] = player_coordinate['y']
    else:
        monster_choice = monster_choice_randomizer()
        while monster_coordinate['x'] == room_size and monster_choice == 'e' or monster_coordinate['x'] == 1 and monster_choice == 'w' or monster_coordinate['y'] == 1 and monster_choice == 'n' or monster_coordinate['y'] == room_size and monster_choice == 's':
            monster_choice = monster_choice_randomizer()

        monster_coordinate['v'] = monster_choice

        if monster_choice == 'n':
            monster_coordinate['y'] -= 1
        if monster_choice == 'e':
            monster_coordinate['x'] += 1
        if monster_choice == 's':
            monster_coordinate['y'] += 1
        if monster_choice == 'w':
            monster_coordinate['x'] -= 1


def distance_checker():
    x_diff = abs(player_coordinate['x'] - monster_coordinate['x'])
    y_diff = abs(player_coordinate['y'] - monster_coordinate['y'])
    return x_diff + y_diff


while not Game_over:

    choice = input('Where will you take a step?\n')

    monster_step()
    step_counter += 1

    if choice.lower() == 'forward':
        if wall_checker():
            step(player_coordinate['v'])
        else:
            wall_message()

    if choice.lower() == 'back':
        player_coordinate['v'] = vector_back(player_coordinate['v'])
        if wall_checker():
            step(player_coordinate['v'])
        else:
            wall_message()

    if choice.lower() == 'left':
        player_coordinate['v'] = vector_left(player_coordinate['v'])
        if wall_checker():
            step(player_coordinate['v'])
        else:
            wall_message()

    if choice.lower() == 'right':
        player_coordinate['v'] = vector_right(player_coordinate['v'])
        if wall_checker():
            step(player_coordinate['v'])
        else:
            wall_message()

    # print(player_coordinate)
    # print(monster_coordinate)
    distance_message = "The distance between you and monster: "

    # print(f'{distance_checker()} \n')
    # print(distance_message+f'{distance_checker()}')
    for i in distance_message:
        time.sleep(0.01)
        print(i, end='', flush=True)

    time.sleep(0.5)
    print(f'{distance_checker()} \n')
    time.sleep(0.5)


    if player_coordinate['x'] == monster_coordinate['x'] and player_coordinate['y'] == monster_coordinate['y']:
        Game_over = True
        print('you fucked up')
        print(f'Stayed alive: {step_counter}')

    if step_counter == 30:
        Game_over = True
        print('you win handsome')

quit = input('Game over.')