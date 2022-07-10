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

def orders():

    greeting = "Please type things you want to order. Type 'quit' if you want to leave."

    print(greeting)

    response = input(">")
    order_response = "** 1 orders of " + response + " have been added to your meal. **"

    print(order_response)

    pool = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado", "A Literal Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]

    counter=0

    if response in pool:
        counter+=1
        print(counter)

orders()









# print("Please type things you want to order. Type 'quit' if you want to leave")

# response = input(">")

# def orders():

#     order_response = "** 1 orders of " + response + " have been added to your meal. **"

#     if response == "quit":
#         print("See you next time!")
#     else:
#         print(order_response)
#         print(response)

# orders()    