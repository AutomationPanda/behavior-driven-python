@unit @basket
Feature: Cucumber Basket
  As a gardener,
  I want to carry cucumbers in a basket,
  So that I can carry many more cucumbers than I could by hand.

  # The scenario outlines below are overkill for testing basket counts.
  # Nevertheless, they illustrate proper usage.

  @add
  Scenario Outline: Add cucumbers to a basket
    Given the basket has "<initial>" cucumbers
    When "<some>" cucumbers are added to the basket
    Then the basket contains "<total>" cucumbers

    Examples:
      | initial | some | total |
      | 0       | 3    | 3     |
      | 2       | 4    | 6     |
      | 5       | 5    | 10    |

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
  Scenario Outline: Remove cucumbers from the basket
    Given the basket has "<initial>" cucumbers
    When "<some>" cucumbers are removed from the basket
    Then the basket contains "<leftover>" cucumbers

    Examples:
      | initial | some | leftover |
      | 8       | 3    | 5        |
      | 10      | 4    | 6        |
      | 7       | 0    | 7        |

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
    When "5" cucumbers are added to the basket
    And "3" cucumbers are removed from the basket
    But "6" more cucumbers are added to the basket
    Then the basket contains "8" cucumbers
