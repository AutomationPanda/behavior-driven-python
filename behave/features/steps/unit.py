"""
This module contains step definitions for unit.feature.
It uses the default 'parse' for step parameters:
http://behave.readthedocs.io/en/latest/tutorial.html#step-parameters
"""


from behave import *
from cucumbers import CucumberBasket


# Givens

@given('the basket has "{initial:d}" cucumber')
@given('the basket has "{initial:d}" cucumbers')
def step_impl(context, initial):
    context.basket = CucumberBasket(initial_count=initial)


@given('the basket is empty')
def step_impl(context):
    context.basket = CucumberBasket()


@given('the basket is full')
def step_impl(context):
    context.basket = CucumberBasket(initial_count=10)


# Whens

@when('"{some:d}" more cucumbers are added to the basket')
@when('"{some:d}" cucumbers are added to the basket')
def step_impl(context, some):
    context.basket.add(some)


@when('"{some:d}" cucumbers are removed from the basket')
def step_impl(context, some):
    context.basket.remove(some)


# Thens

@then('the basket contains "{total:d}" cucumbers')
def step_impl(context, total):
    assert context.basket.count == total


@then('the basket is empty')
def step_impl(context):
    assert context.basket.empty


@then('the basket is full')
def step_impl(context):
    assert context.basket.full


@then('"{some:d}" cucumbers cannot be added to the basket')
def step_impl(context, some):
    count = context.basket.count
    try:
        context.basket.add(some)
    except ValueError as e:
        assert str(e) == "Attempted to add too many cucumbers"
        assert count == context.basket.count, "Cucumber count changed despite overflow"
    except:
        assert False, "Exception raised for basket overflow was not a ValueError"
    else:
        assert False, "ValueError was not raised for basket overflow"


@then('"{some:d}" cucumbers cannot be removed from the basket')
def step_impl(context, some):
    count = context.basket.count
    try:
        context.basket.remove(some)
    except ValueError as e:
        assert str(e) == "Attempted to remove too many cucumbers"
        assert count == context.basket.count, "Cucumber count changed despite overdraw"
    except:
        assert False, "Exception raised for basket overdraw was not a ValueError"
    else:
        assert False, "ValueError was not raised for basket overdraw"
