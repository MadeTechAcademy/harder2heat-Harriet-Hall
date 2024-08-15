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
      | Updated on:                                   |
      | Connectivity:                                 |
      | Building materials:                           |
      | Size in m2:                                   |
      | Coordinates:                                  |
      | Hard To Heat Score: (easy) 0 - 3 (hard)       |
     