import random
import datagen


def game():
    change_difficulty = 1
    lost_once = 0
    word_list = datagen.get_words()
    round_number = len(word_list) #Общее количество туров(словв в фалйе)
    lives: int = 0
    record: int = 0
    win_tour: int = 2
    while True:
        if win_tour == 1: # Проверка на победу в предыдущем туре
            word_list.pop(word_list.index(winning_word))    #При выигрыше угаданное слово исключается из списка по индексу
            lost_once = 0 #Cнимается метка позора
        if lost_once == 0:  #Если еще не было проигрыша в туре
            winning_word = word_list[random.randint(0, len(word_list)) - 1]  #Выбирается слово из списка
            show_winning_word = "■" * len(winning_word)   #Закрашивается искомое слово
            show_winning_word = list(show_winning_word)   #Строка преобразуется в список
        elif lost_once == 1: #Если был проигрыш в туре, но был выбран вариант начать заново
            word_list = datagen.get_words() #Обновляем список, на случай, если выбыл из игры после выигранного тура
            round_number = len(word_list) #Кол-во туров(всего слов в текстовом файле)
            winning_word = word_list[random.choice([i for i in range(len(word_list) - 1) if i not in [winning_word]])] #Выбирается слово, отличное от того, которое было в пред. туре
            show_winning_word = "■" * len(winning_word)
            show_winning_word = list(show_winning_word)
        if change_difficulty == 1:  #Выбор уровня сложности
            difficulty_level = input("Введите уровень сложности: ez(7 жизней), medium(5 жизней), hard(3 жизней)\n")
            difficulty_level.lower()
            while True:
                difficulty_level.lower()
                if difficulty_level == "ez":
                    lives = 7
                    break
                elif difficulty_level == "medium":
                    lives = 5
                    break
                elif difficulty_level == "hard":
                    lives = 3
                    break
                else:
                    difficulty_level  = input("Неккоректный ввод\n Выберите уровень сложности: ez(7 жизней), medium(5 жизней), hard(3 жизней)\n Введите: ez, medium или hard\n")
        print(f"Текущий уровень слонжости: {difficulty_level}\n Количество жизней:{lives}")
        change_difficulty = 0
        opened_letters: int = 0 #Количество угаданных букв
        while True:
            print(winning_word)  # cheat
            print(''.join(show_winning_word), f"|❤x{lives}")
            choice = input("Хотите ввести букву или всё слово сразу? Помните, что при неправильном вводе слова вы выбываете из игры\n Введите букву или слово: ")
            if len(choice) > 1: #Проверка на ввод слова или буквы
                if choice.upper() == winning_word:
                    print("Вы победили в этом туре!")
                    win_tour = 1
                    record += 1
                    round_number -= 1
                    break
                elif choice.upper() != winning_word:
                    print("Вы выбываете из игры")
                    win_tour = 0
                    break
            if choice.upper() in winning_word and choice.upper() not in show_winning_word and choice.upper() != '': #Проверка, есть ли буква в слове, открыта ли она, и ввёл ли пользователь что-то
                print("Вы отгадали букву!")
                for i in range(0, len(winning_word)):  #Открытие букв слова
                    if choice.upper() == winning_word[i]:
                        show_winning_word[i] = winning_word[i]
                        opened_letters += 1
            elif choice.upper() in show_winning_word: #Проверка, была ли уже открыта эта буква
                print("Эта буква уже была, попробуйте снова")
            elif choice.upper() == '':
                print("Молчите? Мотивацию надо поднять! Отнимем у вас жизнь(в игре)")
                lives -= 1
            else:
                print("Ответ неверный! Минус жизнь(в игре)")
                lives -= 1
            if lives == 0:
                print("У вас закончились жизни, вы выбываете из игры!")
                win_tour = 0
                break
            if opened_letters == len(winning_word):
                print("Вы победили в этом туре!")
                win_tour = 1
                record += 1
                round_number -= 1
                break
        if round_number == 0 and win_tour == 1:
            break
        if win_tour == 1:
            while True:
                leave_or_stay = input("Хотите продолжить?\n Да или Нет?: ")
                if leave_or_stay.lower() == 'нет':
                    print(f"Количество отгаданных слов:{record}")
                    print(f"Лучший рекорд:{datagen.get_record()}")
                    break
                elif leave_or_stay.lower() == 'да':
                    if difficulty_level == "ez":     #Восстановление жизней после тура
                        lives = 7
                        break
                    elif difficulty_level == "medium":
                        lives = 5
                        break
                    elif difficulty_level == "hard":
                        lives = 3
                        break
                else:
                    print("Мы вас не поняли, повторите ответ")
            if leave_or_stay.lower() == 'нет':
                break
        elif win_tour == 0:
            while True:
                leave_or_stay = input("Хотите начать игру заново?\n Да или Нет?: ")
                if leave_or_stay.lower() == 'нет':
                    print(f"Количество отгаданных слов:{record}")
                    print(f"Лучший рекорд:{datagen.get_record()}")
                    break
                elif leave_or_stay.lower() == 'да':
                    if difficulty_level == "ez":  #Восстановление жизней после тура
                        lives = 7
                        break
                    elif difficulty_level == "medium":
                        lives = 5
                        break
                    elif difficulty_level == "hard":
                        lives = 3
                        break
                else:
                    print("Мы вас не поняли, повторите ответ")
            if leave_or_stay.lower() == 'нет':
                break
            print(f"Текущий уровень слонжости:{difficulty_level}")
            while True:
                change = input("Хотите сменить уровень сложности?\n Да или нет?: ")
                if change.lower() == "да":
                    change_difficulty = 1
                    break
                elif change.lower() == "нет":
                    break
                else:
                    print("Мы вас не поняли, повторите ответ")

    if round_number == 0 and win_tour == 1:   #Если не осталось слов в списке и был выигран предыдущий раунд
        print("У нас есть победитель! Приз в студию!")
        print("Вы выиграли автомобиль!")
        print('             ______--------___')
        print('            /|             / |')
        print(' o___________|_\\__________/__|')
        print(']|___     |  |=   ||  =|___  |"')
        print('//   \\    |  |____||_///   \\|"')
        print('|  X  |\\--------------/|  X  |\\"')
        print(' \\___/                  \\___/\\\n')

    if record > int(datagen.get_record()): #Перезапись лучшего рекорда в текстовом файле
        print("Вы побили рекорд отгаданных слов!")
        print(f"Предыдущий лучший рекорд:{datagen.get_record()}")
        print(f"Текущий лучший рекорд:{record}")
        datagen.overwrite_record(record)

if __name__ == '__main__':
    game()



