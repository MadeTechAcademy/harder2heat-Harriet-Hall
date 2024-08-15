Feature: Property Page

  Scenario: Display page header
    Given I am on the property page
    Then the page header should be the uprn of the property
