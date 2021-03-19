import allure
import pytest


class TestHello:

    @allure.severity(allure.severity_level.BLOCKER)
    def test_hello1(self):
        assert True


    def test_hello2(self):
        assert True

    @allure.severity(allure.severity_level.BLOCKER)
    def test_hello3(self):
        assert False

    def test_hello4(self):
        assert False
