@when('I press the Search button')
def step_impl(context):
    search_btn = context.driver.find_element(By.ID, "search")
    search_btn.click()

@when('I press the Update button')
def step_impl(context):
    update_btn = context.driver.find_element(By.ID, "update")
    update_btn.click()

@when('I press the Delete button')
def step_impl(context):
    delete_btn = context.driver.find_element(By.ID, "delete")
    delete_btn.click()

@when('I press the Clear button')
def step_impl(context):
    clear_btn = context.driver.find_element(By.ID, "clear")
    clear_btn.click()

@when('I press the Retrieve button')
def step_impl(context):
    retrieve_btn = context.driver.find_element(By.ID, "retrieve")
    retrieve_btn.click()

//7b
@then('I should see "{text}" in the results')
def step_impl(context, text):
    assert text in context.driver.page_source

//7c
@then('I should see "{text}" in the results')
def step_impl(context, text):
    assert text in context.driver.page_source


//7d 

@then('I should see the message "{message}"')
def step_impl(context, message):
    assert message in context.driver.page_source
