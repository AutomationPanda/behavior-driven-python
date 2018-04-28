"""
This module contains step definitions for service.feature.
It uses the default 'parse' for step parameters:
http://behave.readthedocs.io/en/latest/tutorial.html#step-parameters
"""

import requests

from behave import *


# "Constants"

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'


# Whens

@when('the DuckDuckGo API is queried for "{phrase}" in "{rformat}"')
def step_impl(context, phrase, rformat):
    context.response = requests.get(DUCKDUCKGO_API, params={'q': phrase, 'format': rformat})


# Then

@then('the response contains results for "{phrase}"')
def step_impl(context, phrase):
    assert phrase.lower() == context.response.json()['Heading'].lower()
    # A more comprehensive test would check 'RelatedTopics' for matching phrases


@then('the response status code is "{code:d}"')
def step_impl(context, code):
    assert context.response.status_code == code
