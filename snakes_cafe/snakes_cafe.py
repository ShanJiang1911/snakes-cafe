menu = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""

print(menu)

print("Please type things you want to order. Type 'quit' if you want to leave")

response = input(">")

def orders():

    order_response = "**1 orders of " + response + " have been added to your meal.**"

    if response == "quit":
        print("See you next time!")
    else:
        print(order_response)

orders()    