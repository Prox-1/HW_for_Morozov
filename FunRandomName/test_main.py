import pytest
from main import FunRandomName


# Тест на проверку работы отката в именах
def test_names_rollback():
    names_rollback_list = []
    for i in range(1, 2225):
        if i > 12:
            names_rollback_list.pop(0)
        new_value = (FunRandomName().create_funny_name()).split(" ")[-1]
        assert new_value not in names_rollback_list
        names_rollback_list.append(new_value)


# Тест на проверку работы отката в прилагательных
def test_funny_adjectives_rollback():
    funny_adjectives_rollback_list = []
    for i in range(1, 2225):
        if i > 12:
            funny_adjectives_rollback_list.pop(0)
        new_value = (FunRandomName().create_funny_name()).split(" ")[0]
        assert new_value not in funny_adjectives_rollback_list
        funny_adjectives_rollback_list.append(new_value)


# Тест на отсутствие повторяющихся значений
def test_funny_names_rollback():
    funny_names_rollback_list = []
    for i in range(1, 2225):
        if i > 12:
            funny_names_rollback_list.pop(0)
        new_value = FunRandomName().create_funny_name()
        assert new_value not in funny_names_rollback_list
        funny_names_rollback_list.append(new_value)
