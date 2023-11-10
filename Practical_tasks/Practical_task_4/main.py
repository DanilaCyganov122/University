def read_file(fname) -> list:
    file = open(fname, mode='r', encoding='utf8')
    text = file.read().replace(',', '').replace('...','').replace('.','').lower().split()
    file.close()
    unique_words = []
    for i in range(0, len(text)):
        if text[i] not in unique_words:
            unique_words.append(text[i])
    return unique_words

def save_file(fname: str, list_words: list[str]):
    list_words.sort()
    stroka = f"Всего уникальных слов: {len(list_words)}\n========================\n"
    file = open(f"{fname}", mode="w", encoding='utf8')
    file.write(stroka)
    for i in range(0, len(list_words)):
        file.write(f"{list_words[i]}\n")
    file.close()

if __name__ == '__main__':
    save_file('count.txt', read_file('data.txt'))





print(read_file('data.txt'))