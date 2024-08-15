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
