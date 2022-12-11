class Row:

    def __init__(self, char):
        self.__cha_1 = char[0]
        self.__cha_2 = char[1]
        self.__cha_3 = char[2]
        self.__cha_4 = char[3]
        self.__cha_5 = char[4]

    @staticmethod
    def print_table(row_list):
        print('|---|---|---|---|---|')
        for j in row_list:
            print(f'| {j[0]} | {j[1]} | {j[2]} | {j[3]} | {j[4]} |')
            print('|---|---|---|---|---|')

    @property
    def cha_1(self):
        return self.__cha_1

    @property
    def cha_2(self):
        return self.__cha_2

    @property
    def cha_3(self):
        return self.__cha_3

    @property
    def cha_4(self):
        return self.__cha_4

    @property
    def cha_5(self):
        return self.__cha_5

    def add_lst(self, row_list):
        row_list.append(
            [self.cha_1, self.cha_2, self.cha_3, self.cha_4, self.cha_5])
