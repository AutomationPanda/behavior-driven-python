# behavior-driven-python/pytest-bdd

### Purpose
This project shows how to do [BDD](https://automationpanda.com/bdd/)
in [Python](https://automationpanda.com/python/)
using [pytest-bdd](https://github.com/pytest-dev/pytest-bdd), a plugin
for the [pytest](https://docs.pytest.org/) test automation framework.
It exhibits the basics of `pytest-bdd`
with simple unit-, service-, and web-level tests.
Tests are meant to highlight `pytest-bdd` features,
*not* to necessarily show testing best practices for scalable solutions.

This project is a companion to the PyCon Canada 2018 talk
["Behavior-Driven Python with pytest-bdd"](https://2018.pycon.ca/talks/talk-PC-51575/)
and the *Automation Panda* article
"Python Testing 101: pytest-bdd" (forthcoming).

### Setup
This project uses
[Python 3](https://automationpanda.com/2017/02/07/which-version-of-python-should-i-use/)
with
[pipenv](https://automationpanda.com/2018/04/16/pipenv-python-packagement-for-champions/).
Clone the project from GitHub and `pipenv install` the dependencies.

The unit tests use the `cucumbers.py` module from the parent directory.
The `tests/step_defs/__init__.py` file automatically appends this path
for import lookup using `sys.path.append`.

The Web tests use
[Selenium WebDriver](https://www.seleniumhq.org/projects/webdriver/)
to interact with live pages in real browsers.
The hard-coded browser choice is
[Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/).
These tests require
[geckodriver](https://github.com/mozilla/geckodriver/releases)
to be installed locally on the test machine and accessible from the system path.
Typically, they should run fine on any OS with the latest versions of Firefox and geckodriver.
They have been verified on macOS 10.13.4, Firefox 59.0.2, and geckodriver 0.20.1.

### Features
There are 4 feature files that showcase how to use `pytest-bdd` in various ways:

1. `unit_basic.feature`
   * Contains unit test scenarios for a cucumber basket.
   * Tests that cucumbers can be added and removed within limits.
2. `unit_outlines.feature`
   * Contains cucumber basket tests written as scenario outlines.
3. `service.feature`
   * Contains service test scenarios for the DuckDuckGo Instant Answer API.
   * Uses [requests](http://docs.python-requests.org/) to make REST API calls.
4. `web.feature`
   * Contains Web test scenarios for the DuckDuckGo home page.
   * Uses [Selenium WebDriver](https://www.seleniumhq.org/projects/webdriver/)
     to interact with the site through Firefox.
   * Uses a custom pytest fixture for WebDriver setup and cleanup.

Every feature and scenario is tagged according to coverage area.

### Test Execution
To run all tests from the root directory, run `pipenv run pytest`.
All the standard
[pytest command line options](https://docs.pytest.org/en/latest/usage.html)
work.
Use [command line options](http://behave.readthedocs.io/en/latest/behave.html)
for filtering and other controls.
Options may also be put inside the `pytest.ini`
[configuration file](https://docs.pytest.org/en/latest/reference.html#configuration-options).
Below are some common options (just remember to use `pipenv`):

```bash
# run all tests
pytest

# filter tests by test module
# note: feature files cannot be run directly
pytest tests/step_defs/test_unit_basic.py
pytest tests/step_defs/test_unit_outlines.py
pytest tests/step_defs/test_unit_service.py
pytest tests/step_defs/test_unit_web.py

# filter tests by tags
# running by tag is typically better than running by path
pytest -k "unit"
pytest -k "service"
pytest -k "web"
pytest -k "add or remove"
pytest -k "unit and not outline"

# print JUnit report
pytest -junitxml=<path>
```

`pytest-bdd` tests can be executed and filtered together with regular `pytest` tests.
Tests can all be located within the same directory.
Tags work just like [pytest.mark](https://docs.pytest.org/en/latest/example/markers.html).
All other `pytest` plugins should work, too. For example:

* Run tests in parallel with [pytest-xdist](https://docs.pytest.org/en/3.0.0/xdist.html)
* Generate code coverage reports with [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
* Integrate with popular frameworks using [pytest-django](https://pytest-django.readthedocs.io/en/latest/),
  [pytest-flask](https://pytest-flask.readthedocs.io/en/latest/),
  or other similar plugins

*Warning: Scenario outlines cause deprecation warnings when executed.
`pytest.ini` includes options to skip deprecation warnings.
Alternatively, use the --disable-pytest-warnings command line option.*

### Helpful Links

* [Automation Panda blog](https://automationpanda.com/)
* [Python Testing 101: pytest-bdd](https://automationpanda.com/2018/10/22/python-testing-101-pytest-bdd/)
* [Python Testing 101: pytest](https://automationpanda.com/2017/03/14/python-testing-101-pytest/)
* [pytest-bdd on GitHub](https://github.com/pytest-dev/pytest-bdd)
* [pytest Docs](https://docs.pytest.org/)
* bdp-pytest-bdd.pdf (Slides from PyCon Canada 2018 Talk)
