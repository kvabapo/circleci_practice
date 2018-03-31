import pytest
import allure


class TestClass(object):
    @allure.step
    def test_one(self):
        x = "this"
        assert 'h' in x

    @allure.step
    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
