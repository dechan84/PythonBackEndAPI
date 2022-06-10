# Example using BDD framework behave
Feature: Github API validation
  # Enter feature description here
@one
  Scenario: Session management check
    Given I have github credentials
    When When I hit getRepo API of github
    Then status code of response should be 200
