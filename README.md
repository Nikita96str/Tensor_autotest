# Tensor_autotest
Job done in Python 3 using the Selenium library

Description of files:
base_app.py - contains the BaseClass class, which describes methods for working with webdriver
conftest.py - a file for describing fixtures
site_page.py - contains the PageClass class, which describes methods for working with web page elements
search_test.py - first test
image_test.py - second test

First task: Yandex search
1) Go to https://ya.ru/
2) Check if there is a search field
3) Enter in the search Tensor
4) Check that a table with hints (suggest) has appeared
5) Press enter
6) Check that the search results page has appeared
7) Check 1 link leads to tensor.ru

Second task: Pictures on Yandex
1) Go to ya.ru
2) Check that the menu button is present on the page
3) Open the menu, select "Pictures"
4) Check that you have switched to the url https://yandex.ru/images/
5) Open the first category
6) Check that the category name is displayed in the search box
7) Open 1 picture
8) Check that the picture has opened
9) Press forward button
10) Check that the picture has changed
11) Press back
12) Check that the picture is left from step 8
