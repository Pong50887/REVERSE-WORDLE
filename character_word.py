class Character:

    def __init__(self, character, number):
        self.__character = character
        self.__number = number

    @property
    def character(self):
        return self.__character

    @property
    def number(self):
        return self.__number

    def check_if(self, word_list, game_word, yellow_and_red_word):
        if self.character in game_word:
            count_lst = []
            count = -1
            for i in game_word:
                if self.character == i:
                    count += 1
                    count_lst.append(count)
                else:
                    count += 1
            if self.number in count_lst:
                if len(word_list) == 0:
                    if self.character in yellow_and_red_word:
                        word_list.append(f'\033[1;31m{self.character}\033[0m')
                        return f'\033[1;31m{self.character}\033[0m'
                    else:
                        yellow_and_red_word.append(self.character)
                        word_list.append(f'\033[1;31m{self.character}\033[0m')
                        return f'\033[1;31m{self.character}\033[0m'
                else:
                    return f'\033[1;31m{self.character}\033[0m'
            else:
                if self.character in yellow_and_red_word:
                    return f'\033[1;33m{self.character}\033[0m'
                else:
                    yellow_and_red_word.append(self.character)
                    return f'\033[1;33m{self.character}\033[0m'
        else:
            return self.character
