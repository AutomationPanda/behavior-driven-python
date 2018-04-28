"""
This module contains environment controls:
http://behave.readthedocs.io/en/latest/api.html#environment-file-functions
The functions handle Selenium WebDriver setup and cleanup.
(Alternatively, fixtures could be used: http://behave.readthedocs.io/en/latest/fixtures.html)
"""

from selenium import webdriver


# Hooks

# One driver will be shared for all tests for the sake of example.
# A robust framework would likely use one driver instance per test.

# Firefox is the hard-coded browser of choice.
# Feel free to change it here.
# The correct browser and WebDriver executable must be installed on the test machine.
# A flexible framework would read the browser choice from inputs or config data.


def before_all(context):
    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(10)


def after_all(context):
    context.browser.quit()
