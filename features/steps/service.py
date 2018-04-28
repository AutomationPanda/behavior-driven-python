"""
This module contains step definitions for service.feature.
It uses the requests package:
http://docs.python-requests.org/
"""

import requests

from behave import *


# "Constants"

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'


# Whens

@when('the DuckDuckGo API is queried with')
def step_impl(context):
    first_row = context.table[0]
    params = {'q': first_row['phrase'], 'format': first_row['format']}
    context.response = requests.get(DUCKDUCKGO_API, params=params)


# Thens

@then('the response contains results for "{phrase}"')
def step_impl(context, phrase):
    # A more comprehensive test would check 'RelatedTopics' for matching phrases
    assert phrase.lower() == context.response.json()['Heading'].lower()


@then('the response status code is "{code:d}"')
def step_impl(context, code):
    assert context.response.status_code == code
