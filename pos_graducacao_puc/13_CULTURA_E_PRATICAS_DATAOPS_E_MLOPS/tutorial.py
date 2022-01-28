from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

url = "//www.globo.com/busca/click?q=bbb&amp;p=0&amp;r=1616986145665&amp;u=https%3A%2F%2Fgshow.globo.com%2Frealities%2Fbbb%2F&amp;syn=False&amp;key=1f252eb9fd45d63ee067995cc4be40af"
@given('que entrei no site da globo')
def step_impl(context):
    context.driver.get("https://www.globo.com/")  


@when('digitar {valor} na barra de busca')
def step_impl(context, valor):
    context.driver.find_element(By.ID, 'header-search-input').send_keys(valor)    


@when('apertei o enter')
def step_impl(context):
    context.driver.find_element(By.ID, 'header-search-input').send_keys(Keys.RETURN) 


@then('a busca será encontrado')
def step_impl(context):
    pass