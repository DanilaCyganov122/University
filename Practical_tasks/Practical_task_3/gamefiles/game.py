import random
import datagen

word_list = datagen.get_words()
winning_word = word_list[random.randint(0, len(word_list))-1]
word_list.pop(word_list.index(winning_word))
print(winning_word)
show_winning_word = "■"*len(winning_word)
print(show_winning_word)
difficulty_level = input("Введите уровень сложности: Ez, medium, hard\n")
temp = 1
while( temp ):
    if difficulty_level == "ez":
        lives = 7
        temp = 0
    elif difficulty_level == "medium":
        lives = 5
        temp = 0
    elif difficulty_level == "hard":
        lives = 3
        temp = 0
    else:
        difficulty_level  = input("Неккоректный ввод\n Введите уровень сложности: ez, medium, hard\n")
while True:
    choice = input("Хотите ввести букву или всё слово сразу? Помните, что при неправильном вводе слова вы выбваете из игры\n Введите букву или слово: ")
    if (len(choice) > 1):
        if choice == winning_word:
            print("Вы победили в этом туре!")
            win = 1
            break
        elif choice != winning_word:
            print("Вы выбываете из игры")
            win = 0
            break
    if choice in winning_word:
            print("Вы отгадали букву!")



