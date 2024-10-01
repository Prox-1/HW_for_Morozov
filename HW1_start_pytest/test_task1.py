import random
import pytest
from task1 import david_blaines_focus


def test_david_blaines_focus():
    for a in range(0, 100):
        for b in range(0, 100):
            n = random.randint(0, 1001)
            res = ((a + 1) * (b + 1) - a - b - (a * b)) ** n
            assert david_blaines_focus(n) == res
