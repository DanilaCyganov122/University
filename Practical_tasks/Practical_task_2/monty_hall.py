import random
def monty_hall(iterations):
    win1: int = 0
    win2: int = 0
    for i in range(1, iterations):
        winning_door = random.randint(1, 3)
        chosen_door = random.randint(1,3)
        excluded_door = random.choice([i for i in range(1, 4) if i not in [winning_door, chosen_door]])
        rechosen_door = random.choice([i for i in range(1, 4) if i not in [chosen_door, excluded_door]])
        if chosen_door == winning_door:
            win1 += 1
        elif rechosen_door == winning_door:
            win2 += 1
    chance_chosen = float(win1)
    chance_rechosen = float(win2)
    return (chance_chosen/iterations)*100, (chance_rechosen/iterations)*100

print(monty_hall(35))