Feature: Home Page

  Scenario: Display browser title bar
    Given I am on the home page
    Then the browser title bar should display "Harder to Heat Homes"

  Scenario: Display main title on the home page
    Given I am on the home page
    Then the main title should be "Harder to Heat Homes"

  Scenario: Display table with property features as headers
    Given I am on the home page
    Then the homepage table should have the following headers:
      |                                         |
      | UPRN                                    |
      | Year Built                              |
      | Connectivity                            |
      | Building materials                      |
      | Size in m2                              |
      | Coordinates                             |
      | Hard To Heat Score: (easy) 0 - 3 (hard) |
      |                                         |
    And the homepage table should have 8 headers in total

  Scenario: Display table property data
    Given I am on the home page
    Then the table data should be accurate

  Scenario: Display multiple properties in the table
    Given I am on the home page
    Then the table should display more than 1 properties

  Scenario: Display "See more details" button in the table
    Given I am on the home page
    Then there should be a "See more details" button for each property
    And the button style should be "color: black; text-decoration: none;"

  Scenario: Button navigates to property page with UPRN
    Given I am on the home page
    When I click on the "See more details" button for the property with "100090062842" as its UPRN
    Then I should be navigated to the correct property page
