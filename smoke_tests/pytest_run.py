import pytest
import allure


class TestClass(object):

    @allure.step("test 1")
    def test_one(self):
        x = "this"
        assert 'h' in x

    @allure.step("test 2")
    def test_two(self):
        x = "hello"
        assert x = 'hello'
