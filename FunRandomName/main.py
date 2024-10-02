import random


class FunRandomName:
    __funny_adjectives = {  # [пол, откат]
        "Чудесный": [0, 0],
        "Неприличная": [1, 0],
        "Бесполезный": [0, 0],
        "Забавная": [1, 0],
        "Облачный": [0, 0],
        "Смешная": [1, 0],
        "Безумный": [0, 0],
        "Вкусная": [1, 0],
        "Мягкий": [0, 0],
        "Пухлая": [1, 0],
        "Дразнящий": [0, 0],
        "Шумная": [1, 0],
        "Фантастический": [0, 0],
        "Игривая": [1, 0],
        "Поджаренный": [0, 0],
        "Пурпурная": [1, 0],
        "Прыгучий": [0, 0],
        "Радужная": [1, 0],
        "Сверкающий": [0, 0],
        "Кривая": [1, 0],
    }

    __names = {
        "кот": [0, 0],
        "пес": [0, 0],
        "кролик": [0, 0],
        "конь": [0, 0],
        "попугай": [0, 0],
        "жираф": [0, 0],
        "слон": [0, 0],
        "тигрица": [1, 0],
        "медведь": [0, 0],
        "овца": [1, 0],
        "лиса": [1, 0],
        "коза": [1, 0],
        "жук": [0, 0],
        "курица": [1, 0],
        "бобриха": [1, 0],
        "петух": [0, 0],
        "медуза": [1, 0],
        "акула": [1, 0],
        "ара": [1, 0],
        "верблюд": [0, 0],
    }

    def __get_gender(self):
        return random.randint(0, 1)

    def __create_available_list(self, gender: int, dict_: dict):
        return [
            key
            for key in list(dict_.keys())
            if dict_[key][0] == gender and dict_[key][1] == 0
        ]

    def __rollback(self, adjective: str, name: str):
        FunRandomName.__funny_adjectives[adjective][1] = 7
        FunRandomName.__names[name][1] = 7

    def __rollback_reductions(self, dict_: dict):
        def rollback_reduction(value: tuple):
            if value[1] != 0:
                value[1] -= 1
            return value

        reduced_dict = dict(
            map(lambda item: (item[0], rollback_reduction(item[1])), dict_.items())
        )
        return reduced_dict

    def __change_random_elem(self, list_: list):
        return list_[random.randint(0, len(list_) - 1)]

    def __create_funny_name(self, adjectives_list: list, names_list: list):
        FunRandomName.__funny_adjectives = self.__rollback_reductions(
            FunRandomName.__funny_adjectives
        )
        FunRandomName.__names = self.__rollback_reductions(FunRandomName.__names)
        return self.__change_random_elem(adjectives_list), self.__change_random_elem(
            names_list
        )

    def __check_gender(self, gender):
        try:
            if gender == "random":
                gender = self.__get_gender()
            elif gender == "male":
                gender = 0
            elif gender == "female":
                gender = 1
            else:
                raise ValueError("Invalid gender value provided.")
        except ValueError:
            print('Введите значение gender из ["random", "male", "female"]')
        return gender

    def get_funny_name(self, gender="random"):
        gender = self.__check_gender(gender)
        adjectives_list = self.__create_available_list(
            gender, FunRandomName.__funny_adjectives
        )
        names_list = self.__create_available_list(gender, FunRandomName.__names)
        adjective, name = self.__create_funny_name(adjectives_list, names_list)
        self.__rollback(adjective, name)
        return f"{adjective} {name}"
