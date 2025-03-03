import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mian import add

def test_add_success():
    assert add(1, 2) == 3

def test_add_fail():
    assert add(1, 2) == 4