import pytest

from classes.function import calculate_function
from classes.max import calculate_max
from classes.triang import create_sides_array

def test_calculate_function():
    results = calculate_function()
    assert results[0] == -2.0
    assert results[1] == -1.995
    assert results[2] == -1.99
    assert results[3] == -1.985
    assert results[4] == -1.98

def test_max():
    ar1 = [200, 400, 400, 400, 500, 600, 746]
    result = calculate_max(ar1)
    assert result == [746, 600, 500, 400]

def test_create_sides_array():
    array = create_sides_array()
    assert array[0] == (2, 2, 2, True)
    assert array[1] == (2, 2, 3, True)
    assert array[2] == (2, 2, 4, False)
    assert array[3] == (2, 2, 5, False)



