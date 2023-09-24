import pytest
from selene import be, have, browser


@pytest.fixture()
def browser_settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
