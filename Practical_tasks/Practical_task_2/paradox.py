import random
def monty_hall(iterations):
    win1: int = 0
    win2: int = 0
    for i in range(1, iterations+1):
        winning_door = random.randint(1, 3)
        chosen_door = random.randint(1, 3)
        excluded_door = random.choice([i for i in range(1, 4) if i not in [winning_door, chosen_door]])
        rechosen_door = random.choice([i for i in range(1, 4) if i not in [chosen_door, excluded_door]])
        if chosen_door == winning_door:
            win1 += 1
        elif rechosen_door == winning_door:
            win2 += 1
    chance_chosen = win1
    chance_rechosen = win2
    return (chance_chosen/iterations)*100, (chance_rechosen/iterations)*100

def birthday(iterations):
    match1: int = 0 #Кол-во совпадениий дней рождения для класса из 23 человек
    match2: int = 0 #Кол-во совпадениий дней рождения для класса из 60 человек
    for i in range(1, iterations+1):
        class23 = []
        for k in range(0, 23):
            class23.append(random.randint(1,336))  #1 месяц = 28 дней, значит в году 28*12 = 336 дней, дата дня рождения = случайный день в году
        for k in range(0, 22):
            for j in range(k+1, 23):
                if class23[k] == class23[j]:
                    match1 += 1
                    break
            if class23[k] == class23[j]:
                break
    for i in range(1, iterations+1):
        class60 = []
        for k in range(0, 60):
            class60.append(random.randint(1,336))  #1 месяц = 28 дней, значит в году 28*12 = 336 дней, дата дня рождения = случайный день в году
        for k in range(0, 59):
            for j in range(k+1, 60):
                if class60[k] == class60[j]:
                    match2 += 1
                    break
            if class60[k] == class60[j]:
                break
    return (match1/iterations)*100, (match2/iterations)*100





