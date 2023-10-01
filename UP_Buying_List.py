"""
The friendly shopping cart.

This programam was made to help the users with their daily shoppings, alowing the user to add as many items as he want, see all those items with their prices in a friendly format,
and sum all the values, it have also comands to delete an item of the list or exclude all the lists as well. It was made to help the user to keep a financial control,
so you know how much your spending and on what your spending.

Usage:

- Select the options from the menu to interact with the cart.
- Users can add items, show the list, edit an item, exclude an item, empty the cart and sum all the values.
- The program handles input validation to ensure data integrity.

Author: Holzmann, Vinicius.
Date: 26/09/2023
"""

def print_cart(items, prices):  # Defining a function to print the cart content.
    if not items:
        print("Cart is empty. ") # Showing to the user that the cart it's empty if there is no cotent on the list.
    else:
        for x, item in enumerate(items): # Iterating through all items of the list
            print(f"{x + 1} - {item.capitalize()} price is R${prices[x]}")  # Showing all the content of the cart to the user using 'F' string, using captalize for a better look.


def valid_price(price): # Defining a function to check if the price given by the user is valid.
    try:
        price = float(price)   # Trying to convert the input given by the user into a float.
        return True
    except ValueError: 
        return False  # Return a false value if it can't be possible to convert the input into a float.


def add_to_cart(items,prices) : #Defining a function to add items on the cart.
    item = input("Wich item are you buying ? \n") #Asking the user to insert the items he's buying.
    price = input( f"How much for {item.capitalize()} are you paying ? \n")  # Using captalize method to captalize the first letter of the user input, to creat a better look
    price = price.replace(",", ".")  # Preventing errors from the user with the replace() to keep all prices as floats.
    print("Item added to the cart !!!")   #Confirming to the user that the item was added.

    if not valid_price(price):  #Using a function inside a fucntion to check if the price given by user is valid.
        print("Invalid price !!! Product not added .")  #User friendly, showing to the user that if the price given it's not a valid a number it won't be added to the list, the price also the item.
        return

    price = float(price)   #Converting the price into a float
    items.append(item)      #Only appending "item" to items = [] at the end of the function to prevent any kind of error to the user.
    prices.append(price)   #Only appending "price" to prices  = [] at the end of the function to prevent any kind of error to the user.


def edit_cart(items, prices): # Defining a function to edit the items of the cart.
    print("Showing content ... ")
    print_cart(items, prices)  # Showing to the user the items that are on the cart.

    while True:
        item_edit = input("Wich item do you want to edit ? (Enter the item number or press '0' to return to main menu.). \n ")  #Asking the user to put the number of the item he wants to edit or press 0 to return
        try:
            item_edit = int(item_edit )    # Trying to convert the input given by the user into a Int.
            if item_edit == 0: # Creating an exit for the user
                return
            if item_edit >= 1 and item_edit <= len(items): # Successfully converting the number int a int, now it checks if this number is in the list
                break    #Breaking the loop if the condition its true.
            else:
                print("Invalid item number. Please choose a valid item. \n") # Show the user that the given number wasn't correct and asking him for a valid one.
                print_cart(items, prices)  # Using the function to print the list for the user.
        except ValueError:
            print("Enter a valid number format. \n")    #This message will show if the user puts anything but a number(int) on the input.
            print_cart(items, prices)   # Using the function to print the list for the user

    item_index = item_edit - 1  # Creating a variable for the index of the item wich the user want to edit.

    new_item = input("Digit the new item: \n") # Asking the user to input the new item.
    new_price = input(f"Digit the {new_item.capitalize()} price: \n")  # Asking the user to input the new price.
    new_price = new_price.replace(",", ".")   # Using the replace method to prevent errors.

    if not valid_price(new_price):  # Using another function inside of this to validate the new price given by the user.
        print("Invalid format number. Item not modified !!!")
        return

    new_price = float(new_price)
    # The program only save the modified info if all the values given by the user are valid, preveting errors.
    items[item_index] = new_item
    prices[item_index] = new_price
    print("Item replaced !!! ")   # Confirming to the user that the changes were made, making more user friendly.


def delete_item(items, prices):  # Creating a function to delete an item of the list.
    print("Showing list to remove ... ")
    print_cart(items, prices)       # Using the function to print the cart content

    while True:
        item_exc = input("Wich item do you want to exclude ? (Enter the item number or press '0' to return to main menu.). \n")  #Asking the user to put the number of the item he wants to delete or press 0 to return
        try:
            item_exc = int(item_exc)  # Trying to convert the input given by the user into a Int.
            if item_exc == 0: # Creating an exit for the user
              return
            if item_exc >= 1 and item_exc <= len(items): # Successfully converting the number int a int, now it checks if this number is in the list
                break #Breaking the loop if the condition its true.
            else:
                print("Invalid item number. Please choose a valid item. \n") # Show the user that the given number wasn't correct and asking him for a valid one.
                print_cart(items, prices) #Using the function to print the list for the user.
        except ValueError:
            print("Enter a valid number format. \n") #This message will show if the user puts anything but a number(int) on the input.
            print_cart(items, prices)   #Using the function to print the list for the user.

    item_exc = item_exc - 1 # Friendly user to access the user choice of item.
    # Using the del function to delete both item and price selected by the user from the list.
    del items[item_exc]
    del prices[item_exc]

    print( "The selected item was excluded and the list is now updated ... ")  # Confirming to the user his change was made succesfully.


def empty_cart(items, prices): #Defining a function to empty the cart for the user.
    answer = input("Do you really want to empty your cart ? \n"
                   "1 - YES"    "         "    "2 - NO \n")  # Asking the user to confirm that he want to empty the cart.

    if answer == "1":
        prices = []  # Erasing the existent list by creating an empty one.
        items = []  # Erasing the existent list by creating an empty one.
        print("Your cart is now empty ")  # Confirmng to user his change was made.
    elif answer == "2":
        print("Your cart still the same ... ")  # Confirming to user nothing has changed.
    else:
        print("Invalid command !!! Returning to main menu. ") # Showing to the user that the chosen comand was invalid.


def total_cart(items, prices): # Defining a function to sum all the content of the cart,
    print("Here is your list ... ")
    print_cart(items, prices)  # Showing to the user the existing items on the  list.

    total = sum(prices)  #With all prices already converted to floats the program just sum all the values on the prices = [list]
    print(f"The total amount of your cart is R${total: .2f}")  # Showing after the very total amount of the cart, along with the list with all items at the top.


# Starting with two empty lists for user's input
items = []
prices = []
# Creating a Loop for the user choice.
while True:
    user_choice = input("Select one option : \n"
                        "1 - Add to cart. \n"
                        "2 - List cart. \n"
                        "3 - Edit cart. \n"
                        "4 - Delete item. \n"
                        "5 - Empty cart. \n"
                        "6 - Total \n"
                        "7 - Finish shopping. \n")
    match user_choice:
        case "1":
            add_to_cart(items, prices) #Using a created function to deal with the data given by the user.
        case "2":
            print_cart(items, prices)  # Printing the cart-list using a defined function, atop of the code.
        case "3":
            edit_cart(items,prices) # Using a created function for the user to edit the cart.
        case "4":
            delete_item(items, prices) # Using a created function for the user to delete items of the list.
        case "5":
           empty_cart(items, prices) # Using a created function for the user to empty the cart.
        case "6":
           total_cart(items, prices) # Using a created function for the  user to sum all the values of the list.
        case "7":
            print("Thanks for using the cart. !!!  ") # Finishing the application and thanking the user.
            break
