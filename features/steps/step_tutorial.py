# file:features/steps/step_tutorial01.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('we have behave installed')
def step_impl(context):
    print("1")


@when('we implement a test')
def step_impl(context):
    print("2")
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    print("3")
    assert context.failed is False
