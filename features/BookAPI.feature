# Example using BDD framework behave
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here

  @library
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library with ID 1111222
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And  status code of response should be 200

    # Arrows in the description means that there should be a parameters to look in the Examples
  # Parameters are added in the feature in the example part
  @library
  Scenario Outline: Verify AddBook API functionality with parameters
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
    Examples:
      |isbn |aisle |
      |ffff |9499  |
      |powr |43434 |

