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

Scenario: Update a product
  Given I am on the home page
  When I type "Laptop" into the search box
  And I press the Search button
  Then I should see the message "Success"
  And I should see the product name "Laptop"
  When I change the price to "899.99"
  And I press the Update button
  Then I should see the message "Success"
  When I copy the product ID
  And I clear the form
  And I paste the ID into the search box
  And I press the Retrieve button
  Then I should see the message "Success"
  And I should see the price "899.99"
  When I press the Clear button
  And I press the Search button
  Then I should see the updated product "Laptop" with price "899.99" in the results

Scenario: Delete a product
  Given I am on the home page
  When I type "Broken Pen" into the search box
  And I press the Search button
  Then I should see the message "Success"
  And I should see the product name "Broken Pen"
  When I copy the product ID
  And I clear the form
  And I paste the ID into the search box
  And I press the Delete button
  Then I should see the message "Product has been Deleted!"
  When I press the Clear button
  And I press the Search button
  Then I should NOT see "Broken Pen" in the results

Scenario: List all products
  Given I am on the home page
  When I press the Clear button
  And I press the Search button
  Then I should see the message "Success"
  And I should see "Hat" in the results
  And I should see "Shoes" in the results
  And I should see "Big Mac" in the results
  And I should see "Sheets" in the results

Scenario: Search products by category
  Given I am on the home page
  When I press the Clear button
  And I select category "Food"
  And I press the Search button
  Then I should see the message "Success"
  And I should see "Big Mac" in the results
  And I should NOT see "Laptop" in the results
  And I should NOT see "Shoes" in the results


Scenario: Search products by availability
  Given I am on the home page
  When I press the Clear button
  And I set availability to "True"
  And I press the Search button
  Then I should see the message "Success"
  And I should see "Laptop" in the results
  And I should NOT see "Broken Pen" in the results


Scenario: Search product by name
  Given I am on the home page
  When I type "Shoes" into the search box
  And I press the Search button
  Then I should see the message "Success"
  And I should see "Shoes" in the results
  And I should NOT see "Hat" in the results


