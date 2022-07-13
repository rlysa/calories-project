import json


def check_words(word):  # 'пизд', 'хер', 'хуй', 'хуё', 'хуе', 'бля', 'поп', 'жоп', 'ебл', 'хуи'
    with open('words_for_check.json') as file:
        list_of_mats = json.load(file)
    return True if all(i not in word for i in list_of_mats['mats']) else False


# word = input()
# print(check_words(word))
