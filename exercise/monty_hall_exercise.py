import random
from random import choice

def monty_hall(n, trials, switching=True):
    successes = 0
    for _ in range(trials):
        car_door_index = random.randrange(0, n)
        door_choice_1 = random.randrange(0, n)
        revealed_door = choice([i for i in range(0,n) if i not in [car_door_index, door_choice_1]])
        if switching:
            door_choice_2 = choice([i for i in range(0,n) if i not in [door_choice_1, revealed_door]])
            if door_choice_2 == car_door_index:
                successes += 1
        else:
            if door_choice_1 == car_door_index:
                successes += 1
    percentage_won = successes / trials
    return percentage_won

def print_monty_hall_comparison(doors_list, num_tries = 1000):
    print("doors\t\t\t% wins")
    for door_num in doors_list:
        print(f'''{door_num} doors:''')
        print(f'''\tswitch:\t\t''', monty_hall(n=door_num, trials=num_tries))
        print(f'''\tno switch:\t''', monty_hall(n=door_num, trials=num_tries, switching=False))
    return True


if __name__ == "__main__":
    door_combos = [3, 5, 10, 50, 100, 1000]
    print_monty_hall_comparison(door_combos)
