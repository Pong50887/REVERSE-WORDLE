import json
import player_data
from pathlib import Path
import random
from score import Score
from character_word import Character
from row import Row


def read_file():
    with open('text_word', 'r') as word_file:
        word_files = word_file.read().splitlines()
        return word_files


class Data:

    def __init__(self, file):
        self.file = file

    def open_file(self):
        game_word1 = random.choice(self.file)
        return game_word1


def check_word(word, word_list1):
    stage = []

    for f in range(len(words)):
        if len(word_list1[f]) == 0 or [f'\033[1;31m{word[f]}\033[0m'] == \
                word_list1[f]:
            stage.append(True)
        else:
            stage.append(False)

    return all(stage)


print('Welcome to REVERSE WORDLE')
while True:
    print('Please Sign up or Login account to play the game')
    print('1. Sign up account')
    if Path('player_data.json').exists():
        print('2. Login your account')
    print('3. Show ranking')
    print('4. Exit')
    print()
    ''' User choose there choice'''
    path = input('please select your choice: ')
    ''' Create User account which it will go to player_data class'''
    if path == '1':
        name = input('Please input your name (4. Exit): ')
        if name == '4':
            break
        password = input('Please input your password: ')
        data = player_data.Player(name, password)
        data.create_data()
        print()
    elif path == '2':
        '''This path will go to the main game, 
        which need to have user to login'''
        while True:
            name = input('Please input your name (4. Exit): ')
            if name == '4':
                break
            password = input('Please input your password: ')
            data = player_data.Player(name, password)
            if data.check_password():
                ''' If password correct, start the game'''
                end_game_count = 0
                Row_list = []
                yellow_and_red_word = []
                word_list = [[], [], [], [], []]
                game_word = Data(read_file()).open_file()
                all_list = []
                character_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                  'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                                  'y', 'z']
                print('Welcome to REVERSE WORDLE!!')
                print(f'RULES!'.center(26))
                print("1. If you guess a letter that's not in the word, "
                      "it's \033[1;37m grayed \033[0m out "
                      "and you can't use it again.")
                print('2. If you guess a letter that is in the word, '
                      'it turns \033[1;33m yellow \033[0m '
                      'and you must include it.')
                print('3. If you guess a letter in the exact position, '
                      'it turns \033[1;31m red \033[0m '
                      'and is locked in place.')
                print('Guesses as much as you can. '
                      'The more guesser, The winner')
                print(f'Enjoy!')
                while True:
                    words = input('Please input FIVE letter exist word: ')
                    ''' Check if the word the user input is a number'''
                    for i in words:
                        if i.isnumeric():
                            print('please type word, not number')
                            break
                    for k in words:
                        if k.isupper():
                            print('Word suppose to be non capital letter.')
                            break
                    if len(words) != 5:
                        print('your word is not five letter')
                    else:
                        ban_list = []
                        for j in words:
                            if j not in character_list and \
                                    j not in yellow_and_red_word and \
                                    j not in ban_list:
                                ban_list.append(j)
                        if words in read_file():
                            count1 = len(yellow_and_red_word)
                            count2 = 0
                            word_include = []
                            for jk in yellow_and_red_word:
                                if jk in words:
                                    count2 += 1
                                else:
                                    word_include.append(jk)
                            if count1 != count2:
                                print(f'You must use character '
                                      f'{word_include}')
                            else:
                                if ban_list:
                                    print(f'You already use character '
                                          f'{ban_list}')
                                elif check_word(words, word_list):
                                    char = [Character(words[i], i).check_if(
                                        word_list[i], game_word,
                                        yellow_and_red_word) for i in range(5)]
                                    row = Row(char)
                                    row.add_lst(Row_list)
                                    row.print_table(Row_list)
                                    for g in range(5):
                                        if words[g] in character_list:
                                            character_list.remove(words[g])
                                    c = Score(word_list)
                                    if c.check_score():
                                        break
                                else:
                                    print('Must use red character')
                        else:
                            print('please use existing word')
                last = Score(words)
                score = last.count_score(Row_list)
                print(f'Your score is {score}')
                with open('player_data.json', 'r') as data_file:
                    data = json.load(data_file)
                if score > data[name]['score']:
                    data[name]['score'] = score
                with open('player_data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
                print()
                break

    elif path == '3':
        ''' This path show the score of all data in json data.'''
        with open('player_data.json', 'r') as data_file:
            data = json.load(data_file)
        for i in data:
            print(f"Name : {data[i]['name']} | score : {data[i]['score']}")
        print()

    elif path == '4':
        ''' Exit the application'''
        exit()

    else:
        ''' Input correct choice'''
        print('Please input correct choices')
        print()
