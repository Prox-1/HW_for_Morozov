import random


class FunRandomName:
    __funny_adjectives = {
        "Чудесный": 0,
        "Неприличный": 0,
        "Бесполезный": 0,
        "Забавный": 0,
        "Облачный": 0,
        "Смешной": 0,
        "Безумный": 0,
        "Вкусный": 0,
        "Мягкий": 0,
        "Пухлый": 0,
        "Дразнящий": 0,
        "Шумный": 0,
        "Фантастический": 0,
        "Игривый": 0,
        "Поджаренный": 0,
        "Пурпурный": 0,
        "Прыгучий": 0,
        "Радужный": 0,
        "Сверкающий": 0,
        "Кривой": 0,
    }
    __names = {
        "слон слониха": 0,
        "тигр тигрица": 0,
        "медведь медведица": 0,
        "бобр бобриха": 0,
        "козел коза": 0,
        "крокодил утка": 0,
        "горилла обезьяна": 0,
        "единорог оса": 0,
        "кит пиранья": 0,
        "дельфин акула": 0,
        "волк волчица": 0,
        "лис лиса": 0,
        "голубь птица": 0,
        "муравей букашка": 0,
        "кот кошка": 0,
        "хорек свинка": 0,
        "змей змея": 0,
        "ленивец коала": 0,
        "сервал зебра": 0,
        "кенгуру грибница": 0,
    }

    # Назначение отката на использованные значения прилагательных и имен
    def __rollback(self, adj, name):
        FunRandomName.__funny_adjectives[adj] = 12
        FunRandomName.__names[name] = 12

    # Уменьшение отката при создании нового имени
    def __rollback_reductions(self, dict_: dict):
        def rollback_reduction(value):
            return value - 1 if value != 0 else value

        reduced_dict = dict(
            map(lambda item: (item[0], rollback_reduction(item[1])), dict_.items())
        )
        return reduced_dict

    # Функция которую вставим в filter() для отбрасывания значений у которых есть откат
    def __filter_func(self, x):
        if x in list(FunRandomName.__funny_adjectives.keys()):  # костыль
            dict_ = FunRandomName.__funny_adjectives
        else:
            dict_ = FunRandomName.__names

        if dict_[x] == 0:
            return True
        else:
            False

    # Создание списка значений
    def __create_lists_of_available_values(self):
        available_list_adjs = filter(
            self.__filter_func, FunRandomName.__funny_adjectives
        )
        available_list_names = filter(self.__filter_func, FunRandomName.__names)
        return list(available_list_adjs), list(available_list_names)

    # Получение элемента из прилагательных
    def __get_elem_adj(self, list_: list, n: int):
        FunRandomName.__funny_adjectives = self.__rollback_reductions(
            FunRandomName.__funny_adjectives
        )
        return list_[n]

    # Получение элемента из имен
    def __get_elem_name(self, list_: list, n: int):
        FunRandomName.__names = self.__rollback_reductions(FunRandomName.__names)
        return list_[n]

    def create_funny_name(self):
        available_list_adjs, available_list_names = (
            self.__create_lists_of_available_values()
        )
        l_names = len(available_list_names)
        l_adjs = len(available_list_adjs)
        n_of_random_name = random.randint(0, l_names - 1)
        n_of_random_adj = random.randint(0, l_adjs - 1)
        adj = self.__get_elem_adj(available_list_adjs, n_of_random_adj)
        name = self.__get_elem_name(available_list_names, n_of_random_name)
        self.__rollback(adj, name)
        if random.randint(0, 1) == 1:
            return f"{adj[:-2]+'ая'} {name.split()[1]}"
        else:
            return f"{adj} {name.split()[0]}"


print(FunRandomName().create_funny_name())
