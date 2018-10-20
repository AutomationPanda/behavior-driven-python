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
**{TODO: ADD EXPLANATION FOR HOW IMPORT WORKS}**

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
There are 3 feature files that showcase how to use `pytest-bdd` in various ways:

1. `unit_basic.feature`
   * Contains unit test scenarios for a cucumber basket.
   * Tests that cucumbers can be added and removed within limits.
2. `service.feature`
   * Contains service test scenarios for the DuckDuckGo Instant Answer API.
   * Uses [requests](http://docs.python-requests.org/) to make REST API calls.
3. `web.feature`
   * Contains Web test scenarios for the DuckDuckGo home page.
   * Uses [Selenium WebDriver](https://www.seleniumhq.org/projects/webdriver/)
     to interact with the site through Firefox.
   * Uses **{TODO: EXPLAIN HOOKS}** hooks for WebDriver setup and cleanup.

Every feature and scenario is tagged according to coverage area.

### Test Execution
**{TODO}**

```bash
# run all tests

# filter tests by feature file

# filter tests by tags

# print JUnit report
```

**{TODO: outline scenarios have warnings, use --disable-pytest-warnings}**

### Helpful Links

* [Automation Panda blog](https://automationpanda.com/)
* Python Testing 101: pytest-bdd (forthcoming)
* [Python Testing 101: pytest](https://automationpanda.com/2017/03/14/python-testing-101-pytest/)
* [pytest-bdd on GitHub](https://github.com/pytest-dev/pytest-bdd)
* [pytest Docs](https://docs.pytest.org/)
* bdp-pytest-bdd.pdf (Slides from PyCon 2018 Talk) (forthcoming)
