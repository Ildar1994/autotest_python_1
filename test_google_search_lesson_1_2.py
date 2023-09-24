import pytest
from selene import be, have, browser



def test_positiv_search(browser_settings):
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Releases · yashaka/selene'))
    print('Позитивный кейс пройден.Информация найдена')


def test_negativ_search(browser_settings):
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').type('sscццуцуууукапаийййqqqqq34565').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('Негативный кейс не пройден.Информация не найдена')
