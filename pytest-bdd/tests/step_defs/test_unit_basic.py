"""
This module contains step definitions for unit_basic.feature.
Decorators for step definition functions are simplified using partials.
"""

from cucumbers import CucumberBasket
from functools import partial
from pytest_bdd import scenarios, given, when, then, parsers


# Partial Step Helpers

CONVERTERS = {
    'initial': int,
    'some': int,
    'total': int,
}

given_basket = partial(given, target_fixture='basket', converters=CONVERTERS)
when_cukes = partial(when, converters=CONVERTERS)
then_cukes = partial(then, converters=CONVERTERS)


# Scenarios

scenarios('../features/unit_basic.feature')


# Given Steps

@given_basket(parsers.re(r'the basket has "(?P<initial>\d+)" cucumber(s?)'))
def basket_init(initial):
    return CucumberBasket(initial_count=initial)


@given_basket('the basket is empty')
def basket_empty():
    return CucumberBasket()


@given_basket('the basket is full')
def basket_full():
    return CucumberBasket(initial_count=10)


# When Steps

@when_cukes(parsers.re(r'"(?P<some>\d+)"( more)? cucumber(s?) are added to the basket'))
def add_cucumbers(basket, some):
    basket.add(some)


@when_cukes(parsers.re(r'"(?P<some>\d+)"( more)? cucumber(s?) are removed from the basket'))
def remove_cucumbers(basket, some):
    basket.remove(some)


# Then Steps

@then_cukes(parsers.re(r'the basket contains "(?P<total>\d+)" cucumbers'))
def basket_has_total(basket, total):
    assert basket.count == total


@then_cukes('the basket is empty')
def basket_is_empty(basket):
    assert basket.empty


@then_cukes('the basket is full')
def basket_is_full(basket):
    assert basket.full


@then_cukes(parsers.re(r'"(?P<some>\d+)" cucumbers cannot be added to the basket'))
def cannot_add_more(basket, some):
    count = basket.count
    try:
        basket.add(some)
    except ValueError as e:
        assert str(e) == "Attempted to add too many cucumbers"
        assert count == basket.count, "Cucumber count changed despite overflow"
    except:
        assert False, "Exception raised for basket overflow was not a ValueError"
    else:
        assert False, "ValueError was not raised for basket overflow"


@then_cukes(parsers.re(r'"(?P<some>\d+)" cucumbers cannot be removed from the basket'))
def cannot_remove_more(basket, some):
    count = basket.count
    try:
        basket.remove(some)
    except ValueError as e:
        assert str(e) == "Attempted to remove too many cucumbers"
        assert count == basket.count, "Cucumber count changed despite overdraw"
    except:
        assert False, "Exception raised for basket overdraw was not a ValueError"
    else:
        assert False, "ValueError was not raised for basket overdraw"

