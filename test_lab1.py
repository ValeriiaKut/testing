#1
import pytest
from lab1 import (
    add, subtract, multiply, divide,
    fibonacci_iterative, fibonacci_recursive,
    factorial_recursive, factorial_iterative,
    nwd_iterative, nwd_recursive, group_files)

def test_add_positive():
    assert add(1,1) == 2
    assert add(1, -2) == -1

def test_subtract_positive():
    assert subtract(1,1) == 0
    assert subtract(1,2) == -1

def test_multiply_positive():
    assert multiply(1,1) == 1
    assert multiply(1,2) == 2

def test_divide_positive():
    assert divide(1,1) == 1
    assert divide(1,2) == 0.5

def test_add_negative():
    with pytest.raises(TypeError):
        add(1,"1")

def test_subtract_negative():
    with pytest.raises(TypeError):
        subtract(1,"1")

def test_multiply_negative():
    with pytest.raises(TypeError):
        multiply(1,"1")

def test_divide_negative():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

#2
def test_fibonacci_iterative_positive():
    assert fibonacci_iterative(0) == 0
    assert fibonacci_iterative(1) == 1
    assert fibonacci_iterative(2) == 1
    assert fibonacci_iterative(5) == 5
    assert fibonacci_iterative(7) == 13

def test_fibonacci_recursive_positive():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(5) == 5
    assert fibonacci_recursive(7) == 13

def test_fibonacci_iterative_negative():
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)
    with pytest.raises(TypeError):
        fibonacci_iterative("1")

def test_fibonacci_recursive_negative():
    with pytest.raises(ValueError):
        fibonacci_recursive(-1)
    with pytest.raises(TypeError):
        fibonacci_recursive("1")
#3
def test_factorial_iterative_positive():
    assert factorial_iterative(0) == 1
    assert factorial_iterative(1) == 1
    assert factorial_iterative(2) == 2
    assert factorial_iterative(3) == 6
    assert factorial_iterative(5) == 120

def test_factorial_recursive_positive():
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(2) == 2
    assert factorial_recursive(3) == 6
    assert factorial_recursive(5) == 120

def test_factorial_iterative_negative():
    with pytest.raises(ValueError):
        factorial_iterative(-1)
    with pytest.raises(TypeError):
        factorial_iterative("1")

def test_factorial_recursive_negative():
    with pytest.raises(ValueError):
        factorial_recursive(-1)
    with pytest.raises(TypeError):
        factorial_recursive("1")

#4
def test_nwd_iterative_positive():
    assert nwd_iterative(24,36) == 12
    assert nwd_iterative(48,18) == 6
    assert nwd_iterative(7,13) == 1
    assert nwd_iterative(15,15) == 15

def test_nwd_recursive_positive():
    assert nwd_recursive(24,36) == 12
    assert nwd_recursive(48,18) == 6
    assert nwd_recursive(7,13) == 1
    assert nwd_recursive(15,15) == 15

def test_nwd_iterative_negative():
    with pytest.raises(ValueError):
        nwd_iterative(-1,2)
    with pytest.raises(TypeError):
        nwd_iterative("1", 0.5)

def test_nwd_recursive_negative():
    with pytest.raises(ValueError):
        nwd_recursive(-1,2)
    with pytest.raises(TypeError):
        nwd_recursive("1", 0.5)

#5
def test_group_files_positive():
    assert group_files("a.jpg, b.txt, c.jpg, d.txt") == {
        "jpg": ["a.jpg", "c.jpg"],
        "txt": ["b.txt", "d.txt"]
    }
    assert group_files("archive.tar.gz, script.test.py") == {
        "gz": ["archive.tar.gz"],
        "py": ["script.test.py"]
    }
    assert group_files("photo.png") == {
        "png": ["photo.png"]
    }


def test_group_files_negative():
    with pytest.raises(TypeError):
        group_files(123)



