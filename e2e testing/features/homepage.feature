Feature: Home Page

  Scenario: Display browser title bar
    Given I am on the home page
    Then the browser title bar should display "Harder to Heat Homes"

  Scenario: Display main title on the home page
    Given I am on the home page
    Then the main title should be "Harder to Heat Homes"
