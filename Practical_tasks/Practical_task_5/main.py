
def error():
    while True:
        try:
            file_name = input("Введите имя файла: ")
            file = open(file_name, mode='r', encoding='utf8')
            break
        except:
            print("Некорректный ввод! Введите снова")
    number_list = file.readlines()
    file.close()
    number_list.pop(0)
    for i in range(0, len(number_list)):
        number_list[i] = int((str(number_list[i])).replace('\n', ''))
    return number_list

if __name__ == '__main__':
    print(error())



