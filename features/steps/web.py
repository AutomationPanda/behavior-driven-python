"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled in environment.py
For a real test automation project,
use Page Object Model or Screenplay Pattern to model web interactions.
"""

from behave import *
from selenium.webdriver.common.keys import Keys


# "Constants"

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# Givens

@given('the DuckDuckGo home page is displayed')
def step_impl(context):
    context.browser.get(DUCKDUCKGO_HOME)


# Whens

@when('the user searches for "{phrase}"')
def step_impl(context, phrase):
    search_input = context.browser.find_element_by_name('q')
    search_input.send_keys(phrase + Keys.RETURN)


# Thens

@then('results are shown for "{phrase}"')
def step_impl(context, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = context.browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase
    search_input = context.browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase
