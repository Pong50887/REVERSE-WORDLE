import json


class Player:

    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    @property
    def name(self):
        return self.__name

    @property
    def password(self):
        return self.__password

    def create_data(self):
        try:
            with open('player_data.json', 'r') as data_file:
                data = json.load(data_file)
                try:
                    if data[self.__name]['name'] != self.__name:
                        data[self.__name] = {"name": self.__name,
                                             "password": self.__password,
                                             "score": 0}
                        print('Data Created')
                    else:
                        print('The user already existed')
                        pass
                except KeyError:
                    data[self.__name] = {"name": self.__name,
                                         "password": self.__password,
                                         "score": 0}
                    print('Data Created')
            with open('player_data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open('player_data.json', 'w') as data_file:
                l_list = {self.__name: {"name": self.__name,
                                        "password": self.__password,
                                        "score": 0}}
                json.dump(l_list, data_file, indent=4)
                print('Data Created')

    def check_password(self):
        with open('player_data.json', 'r') as data_file:
            data = json.load(data_file)
            try:
                if data[self.__name]['name'] == self.__name:
                    if data[self.__name]['password'] == self.__password:
                        return True
                    else:
                        print(f'Please input a correct password')
                        return False
                else:
                    print(f'There is no data name {self.__name}')
                    return False
            except KeyError:
                print(f'There is no data name {self.__name}')
                return False
