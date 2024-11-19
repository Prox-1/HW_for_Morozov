import pytest
import random
from binary_search import binary_search
from sorted_class import Sorts
sorts = Sorts()
# ----------Тесты для бинарного поиска------------
def test_correct_search():
    array = [1,2,3,4,5,6,7,8,9,10,77]
    for i in range(len(array)):
        assert binary_search(array, array[i]) == i

def test_correct_exit_from_the_loop():
    array = [1,2,3,4,5,6,7,8,9,10,77]
    check_nums = [11,22,33,656,23,98,12,433,66,99]
    for i in range(len(check_nums)):
        assert binary_search(array, check_nums[i]) == -1

# ----------Тесты для сортировок------------

def test_bubble_sort():
    for i in range(100):
        random_array = random.sample(range(1, 101), 10)
        assert sorts.bubble_sort(random_array) == sorted(random_array)

def test_selection_sort():
    for i in range(100):
        random_array = random.sample(range(1, 101), 10)
        assert sorts.selection_sort(random_array) == sorted(random_array)

def test_insertion_sort():
    for i in range(100):
        random_array = random.sample(range(1, 101), 10)
        assert sorts.insertion_sort(random_array) == sorted(random_array)

def test_quick_sort():
    for i in range(100):
        random_array = random.sample(range(1, 101), 10)
        assert sorts.quick_sort(random_array) == sorted(random_array)