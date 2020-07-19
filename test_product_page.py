from pages.product_page import ProductPage

import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name()
    page.should_be_correct_price()


