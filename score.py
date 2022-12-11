class Score:

    def __init__(self, word_list):
        self.__word1 = word_list[0]
        self.__word2 = word_list[1]
        self.__word3 = word_list[2]
        self.__word4 = word_list[3]
        self.__word5 = word_list[4]

    @property
    def word1(self):
        return self.__word1

    @property
    def word2(self):
        return self.__word2

    @property
    def word3(self):
        return self.__word3

    @property
    def word4(self):
        return self.__word4

    @property
    def word5(self):
        return self.__word5

    def check_score(self):
        return self.word1 != [] and self.word2 != [] and self.word3 != [] and\
               self.word4 != [] and self.word5 != []

    @staticmethod
    def count_score(row_list):
        return len(row_list)
