import pytest


def fun(x):
    return x**2


def test_meth():
    assert fun(5) == 25