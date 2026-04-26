Feature: Product Management

  Background:
    Given the following products
      | name       | category     | price | availability |
      | Laptop     | Electronics  | 999.99 | true        |
      | Notebook   | Stationery   | 2.50   | true        |
      | Broken Pen | Stationery   | 0.50   | false       |

  Scenario: Read a product
    When I visit the "Home Page"
    And I click the "Laptop" product
    Then I should see the product details

  Scenario: Update a product
    When I edit the "Notebook" product
    And I change the price to "3.00"
    Then the price should be "3.00"

  Scenario: Delete a product
    When I delete the "Broken Pen" product
    Then the product should no longer exist

  Scenario: List all products
    When I go to the products list
    Then I should see 3 products

  Scenario: Search by name
    When I search for "Laptop"
    Then I should see exactly 1 product named "Laptop"

  Scenario: Search by category
    When I filter by category "Stationery"
    Then I should see 2 products

  Scenario: Search by availability
    When I filter by availability "true"
    Then I should see 2 available products
