import pytest
from app import soma, subtracao, multiplicacao, divisao

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(1, 2) == -1
    assert subtracao(0, 0) == 0

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-1, 5) == -5
    assert multiplicacao(0, 10) == 0

def test_divisao():
    assert divisao(6, 3) == 2
    assert divisao(7, 2) == 3.5
    with pytest.raises(ValueError):
        divisao(10, 0)
