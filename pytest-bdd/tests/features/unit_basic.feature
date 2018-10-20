@unit @basket
Feature: Cucumber Basket
  As a gardener,
  I want to carry cucumbers in a basket,
  So that I don't drop them all.

  # Gherkin-based automation frameworks *can* be used for unit testing.
  # However, they are better suited for integration and end-to-end testing.
  # This feature file does unit testing for the sake of illustrating Gherkin usage.

  @add
  Scenario: Add cucumbers to a basket
    Given the basket has "2" cucumbers
    When "4" cucumbers are added to the basket
    Then the basket contains "6" cucumbers

  @add @full
  Scenario: Fill the basket with cucumbers
    Given the basket is empty
    When "10" cucumbers are added to the basket
    Then the basket is full

  @add @error
  Scenario: Overfill the basket with cucumbers
    Given the basket has "8" cucumbers
    Then "3" cucumbers cannot be added to the basket

  @remove
  Scenario: Remove cucumbers from the basket
    Given the basket has "8" cucumbers
    When "3" cucumbers are removed from the basket
    Then the basket contains "5" cucumbers

  @remove @empty
  Scenario: Empty the basket of all cucumbers
    Given the basket is full
    When "10" cucumbers are removed from the basket
    Then the basket is empty

  @remove @error
  Scenario: Remove too many cucumbers from the basket
    Given the basket has "1" cucumber
    Then "2" cucumbers cannot be removed from the basket

  @add @remove
  Scenario: Add and remove cucumbers
    Given the basket is empty
    When "4" cucumbers are added to the basket
    And "6" more cucumbers are added to the basket
    But "3" cucumbers are removed from the basket
    Then the basket contains "7" cucumbers
