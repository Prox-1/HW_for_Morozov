import random
import pytest
from task2 import gorgons_machinations


def test_gorgons_machinations_errors():
    assert (
        gorgons_machinations(3, [4, 5, 90, 2], 2)
        == "The number of husbands and the number of bills do not match"
    )
    assert gorgons_machinations(41, [4, 5, 90, 2], 2) == "Too many husbands"
    assert (
        gorgons_machinations(4, [4, 5, 90, 2], 110) == "The Gorgon's bill is too high"
    )
    assert (
        gorgons_machinations(4, [4, 5, -90, 2], 10) == "Negative value is not possible"
    )


def test_gorgons_machinations_example():
    assert gorgons_machinations(2, [5, 10], 5) == 7.5
    assert gorgons_machinations(4, [4, 5, 90, 2], 2) == 47
