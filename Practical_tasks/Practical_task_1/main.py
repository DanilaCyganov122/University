import random

win1: int = 0
win2: int = 0
for i in range(1, 10001):
    winning_door = random.randint(1, 3)
    chosen_door = random.randint(1,3)
    excluded_door = random.choice([i for i in range(1, 4) if i not in [winning_door, chosen_door]])
    rechosen_door = random.choice([i for i in range(1, 4) if i not in [chosen_door, excluded_door]])
    if chosen_door == winning_door:
        win1 += 1
    elif rechosen_door == winning_door:
        win2 += 1
chance_chosen = win1
chance_rechosen = win2
print("Кол-во угаданных дверей, выбранных изначально: ", chance_chosen)
print("Кол-во угаданных дверей, при смене выбора двери: ", chance_rechosen)

