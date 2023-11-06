

def get_words(path=r"\gamefiles\words.txt"):
    file = open('words.txt', mode='r', encoding='utf8')
    words = file.read().upper().splitlines()
    file.close()
    return words
def get_record(path=r"\gamefiles\record.txt"):
    file = open('record.txt', mode='r', encoding='utf8')
    record = file.read()
    file.close()
    return record
def overwrite_record(current_record, path=r"\gamefiles\record.txt"):
    file = open('record.txt', mode='w', encoding='utf8')
    file.truncate(0)
    file.write(f'{current_record}')









