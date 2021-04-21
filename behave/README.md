# behavior-driven-python/behave

### Purpose
This project shows how to do [BDD](https://automationpanda.com/bdd/)
in [Python](https://automationpanda.com/python/)
using [behave](http://behave.readthedocs.io/en/latest/index.html).
It exhibits the basics of the `behave` test framework
with simple unit-, service-, and web-level tests.
Tests are meant to highlight `behave` features,
*not* to necessarily show testing best practices for scalable solutions.

This project is a companion to the PyCon 2018 talk
[Behavior-Driven Python](https://automationpanda.com/2018/05/28/behavior-driven-python/)
and the *Automation Panda* article
[Python Testing 101: behave](https://automationpanda.com/2018/05/11/python-testing-101-behave/).

### Setup
This project uses
[Python 3](https://automationpanda.com/2017/02/07/which-version-of-python-should-i-use/).
Dependencies are listed in `requirements.txt`.
Use [venv](https://docs.python.org/3/tutorial/venv.html)
to create a virtual environments for dependencies.

The unit tests use the `cucumbers.py` module from the parent directory.
The `features/steps/__init__.py` file automatically appends this path
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
There are 3 feature files that showcase how to use `behave` in various ways:

1. `unit.feature`
   * Contains unit test scenarios for a cucumber basket.
   * Tests that cucumbers can be added and removed within limits.
2. `service.feature`
   * Contains service test scenarios for the DuckDuckGo Instant Answer API.
   * Uses [requests](http://docs.python-requests.org/) to make REST API calls.
3. `web.feature`
   * Contains Web test scenarios for the DuckDuckGo home page.
   * Uses [Selenium WebDriver](https://www.seleniumhq.org/projects/webdriver/)
     to interact with the site through Firefox.
   * Uses `environment.py` hooks for WebDriver setup and cleanup.

Every feature and scenario is tagged according to coverage area.

### Test Execution
To run all tests from the root directory, run `behave`.
Use [command line options](http://behave.readthedocs.io/en/latest/behave.html)
for filtering and other controls.
Options may also be put inside the `behave.ini`
[configuration file](http://behave.readthedocs.io/en/latest/behave.html#configuration-files).
Below are some common options:

```bash
# run all tests
behave

# filter tests by feature file
behave features/unit.feature
behave features/service.feature
behave features/web.feature

# filter tests by tags
behave --tags-help
behave --tags @unit
behave --tags @service
behave --tags @web
behave --tags @duckduckgo
behave --tags ~@unit
behave --tags @basket --tags @add

# print JUnit report
behave --junit
```

### Helpful Links

* [Automation Panda blog](https://automationpanda.com/)
* [Python Testing 101: behave](https://automationpanda.com/2018/05/11/python-testing-101-behave/)
* [Official Behave Docs](https://behave.readthedocs.io/en/latest/)
* [Behave on GitHub](https://github.com/behave/behave)
* [Behave Examples on GitHub](https://github.com/behave/behave.example)
* bdp-behave.pdf (Slides from PyCon 2018 Talk)
