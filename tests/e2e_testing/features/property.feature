Feature: Property Page

  Scenario: Display page header
    Given I am on the property page
    Then the page header should be the uprn of the property

  Scenario: Display table with property features as headers
    Given I am on the property page
    Then the property table should have the following headers
      |                                               |   
      | OSID:                                         |
      | Year Built:                                   |
      | Year Built last updated:                                   |
      | Connectivity:                                 |
      | Building materials:                           |
      | Size in m2:                                   |
      | Coordinates:                                  |
      | Hard To Heat Score: (easy) 0 - 3 (hard)       |
      And the property table should have 8 headers in total

  Scenario: Display table property data
    Given I am on the property page
    Then the table should display valid property data

  Scenario: Home button navigates to the homepage
    Given I am on the property page
    When I click the home button
    Then I should be navigated to the homepage