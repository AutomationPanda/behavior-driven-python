"""
This module contains step definitions for unit_outline.feature.
Note that the step decorators must be different than for regular steps.
Scenarios must be given an example_converters dict, too.
"""

from cucumbers import CucumberBasket
from pytest_bdd import scenarios, given, when, then


# Scenarios

CONVERTERS = {
    'initial': int,
    'some': int,
    'total': int,
}

scenarios('../features/unit_outlines.feature', example_converters=CONVERTERS)


# Given Steps

@given('the basket has "<initial>" cucumbers', target_fixture='basket')
def basket(initial):
    return CucumberBasket(initial_count=initial)


# When Steps

@when('"<some>" cucumbers are added to the basket')
def add_cucumbers(basket, some):
    basket.add(some)


@when('"<some>" cucumbers are removed from the basket')
def remove_cucumbers(basket, some):
    basket.remove(some)


# Then Steps

@then('the basket contains "<total>" cucumbers')
@then('the basket contains "<leftover>" cucumbers')
def basket_has_total(basket, total):
    assert basket.count == total
