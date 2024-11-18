from dessert import DessertItem, Candy, Cookie, IceCream, Sundae, Order
import receipt
from typing import List, Dict

class DessertShop:
  def __init__(self):
     self.customer_db: Dict[str, Customer] = {}

  def get_create(self, customer_name: str):
     if customer_name in self.customer_db:
        return self.customer_db[customer_name]
     else:
        print("\nWelcome new customer!")
        new_customer = Customer(customer_name)
        self.customer_db[customer_name] = new_customer
        return new_customer

  # HERE IS THE CANDY INPUT
  def user_prompt_candy(self):
    '''Get input for the Candy() object: Type (str), Weight (int), Price (float)'''
    try:
        amount_1 = input("Enter the type of candy: ")
    except ValueError:
      print("Please enter a valid Candy")
    try:
        amount_2 = int(input("Enter the weight purchased: "))
    except ValueError:
      print("Please enter the proper weight")
    try:
        amount_3 = float(input("Enter the price per pound: "))
    except ValueError:
       print("Please enter the price with decimal.")

    return Candy(amount_1, amount_2, amount_3)

    # HERE IS THE COOKIE INPUT
  def user_prompt_cookie(self):
    '''Get input for the Cookie() object: Type (str), quantity (int), Price (float)'''
    try:
        amount_1 = input("Enter the type of cookie: ")
    except ValueError:
      print("Please enter a valid Cookie")
    try:
        amount_2 = int(input("Enter the quantity purchased: "))
    except ValueError:
      print("Please enter the proper quantity")
    try:
        amount_3 = float(input("Enter the price per dozen: "))
    except ValueError:
       print("Please enter the price with decimal.")

    return Cookie(amount_1, amount_2, amount_3)

    # HERE IS THE ICECREAM INPUT
  def user_prompt_icecream(self):
    '''Get input for the IceCream() object: Type (str), Scoops (int), Price (float)'''
    try:
        amount_1 = input("Enter the type of Ice Cream: ")
    except ValueError:
      print("Please enter a valid Candy")
    try:
        amount_2 = int(input("Enter the scoop count: "))
    except ValueError:
      print("Please enter the proper weight")
    try:
        amount_3 = float(input("Enter the price per scoop: "))
    except ValueError:
       print("Please enter the price with decimal.")

    return IceCream(amount_1, amount_2, amount_3)

    # HERE IS THE SUNDAE INPUT
  def user_prompt_sundae(self):
    '''Get input for the Sundae() object: Type (str), Scoop (int), Price (float), Topping (str), Topping Price (float)'''
    try:
        amount_1 = input("Enter the type of Ice Cream: ")
    except ValueError:
      print("Please enter a valid Candy")
    try:
        amount_2 = int(input("Enter the scoop count: "))
    except ValueError:
      print("Please enter the proper weight")
    try:
        amount_3 = float(input("Enter the price per scoop: "))
    except ValueError:
       print("Please enter the price with decimal.")
    try:
        amount_4 = input("Enter the topping name: ")
    except ValueError:
       print("Please enter a valid topping.")
    try:
        amount_5 = float(input("Enter the topping price: "))
    except ValueError:
       print("Please enter the price with decimal.")

    return Sundae(amount_1, amount_2, amount_3, amount_4, amount_5)
  
    #Here is the payment method
  def user_prompt_payment(self):
    """This is meant to get the payment method and add it to order"""
    payment_prompt = '\n'.join([
        "Select payment method:",
        "1: CASH",
        "2: CARD",
        "3: PHONE",
        "\nEnter your choice (1-3): "
    ])

    payment_done = False # False until given a proper payment method
    while not payment_done: # Loop begins while not given payment
        pay_choice = input(payment_prompt) # pay_choice will store the input of the selected Payment Choice
        match pay_choice:
          case '1':
            pay_choice = "CASH"
            payment_done = True
          case '2':
              pay_choice = "CARD"
              payment_done = True
          case '3':
              pay_choice = "PHONE"
              payment_done = True
          case _:
              print("Invalid Payment method, must be CASH, CARD or PHONE") # This part essentially throws an error if NOT 1, 2 or 3.
    return pay_choice # Returns either CASH, CARD or PHONE
  

# Customer Class and all it's functionalities
class Customer:
  id: int = 0

  def __init__(self, customer_name: str):
     self.customer_name: str = customer_name
     self.order_history: List[Order] = []
     self.customer_id: int = 0
     Customer.id += 1

  def add2history(self, order:Order)-> "Customer":
    self.order_history.append(order)
    return self



# Main function
def main():
    '''Create Order instance, pass DessertItem list of objects, return names and amount from order.'''
    shop = DessertShop() 

    while True: # Begin the order loop here.
      order = Order()
      '''
      order.add(Candy('Candy Corn', 1.5, 0.25))
      order.add(Candy('Gummy Bears', 0.25, 0.35))
      order.add(Cookie('Chocolate Chip', 6, 3.99))
      order.add(IceCream('Pistachio', 2, 0.79))
      order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
      order.add(Cookie('Oatmeal Raisin', 2, 3.45))
      '''
      # boolean done = false
      done: bool = False
      # build the prompt string once
      prompt = '\n'.join([ '\n',
              '1: Candy',
              '2: Cookie',            
              '3: Ice Cream',
              '4: Sunday',
              '5: Admin Module'
              '\nWhat would you like to add to the order? (1-4, Enter for done): '
        ])

      while not done:
        choice = input(prompt) # This choice is for the order items, unless ''. Which will call the shop.user_prompt_payment()
        match choice:
          case '':
            #Ask for customer name BEFORE payment.
            customer_name = input("Please Enter your name: ")
            customer = shop.get_create(customer_name)
            customer.add2history(order)

            payment = shop.user_prompt_payment() # This calls the DessertShop Object for the payment Method
            order.set_pay_type(payment) # This sets the payment method in the order method in dessert.py
            done = True # This stops the loop
            print("Here's your receipt!") 
          case '1':            
            item = shop.user_prompt_candy()
            order.add(item)
            print(order)
          case '2':            
            item = shop.user_prompt_cookie()
            order.add(item)
            print(order)
          case '3':            
            item = shop.user_prompt_icecream()
            order.add(item)
            print(order)
          case '4':            
            item = shop.user_prompt_sundae()
            order.add(item)
            print(order)
          case _:            
            print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')
      print()

      new_order = input("\n Start a new order? Press Y for Yes.")
      if new_order.lower() != 'y':
         print("Enjoy!")
         break

      #
      #add your code below here to print the PDF receipt as the last thing in main()
      #


    # Sort the orders based on price
    order.sort()

    # List of Lists Column names
    DATA = [
        ["Name", "Quantity", "Unit Price","Item Cost", "Tax"],
        [f"Customer Name: {customer_name}"],
        [f"Customer ID: {customer.customer_id}"],
        [f"Total Orders: {len(customer.order_history)}"],
        ["---------------------------"],
    ]

    # Loop through each items cost and taxes and append them according to their row
    total_cost = 0.0
    total_tax = 0.0
    for item in order.order:
        item_cost = round(item.calculate_cost(), 2)
        item_tax = round(item.calculate_tax(), 2)
        DATA.append(
           [
            f"{item.name} ({item.packaging})", 
            item.quantity, 
            item.unit_price,
            f"${item_cost:.2f}", 
            f"${item_tax:.2f}"
            ]
           )
        total_cost += item_cost
        total_tax += item_tax
    DATA.append(["---------------------------"])

    # Appending the Subtotals, Total & Magnitude of the cart
    DATA.append([f"Total items in the order:", f"{len(order)}", ""])
    DATA.append(["Order Subtotals", "", "", f"${total_cost:.2f}", f"${total_tax:.2f}"])
    DATA.append(["Order Total", "", "", "",f"${total_cost + total_tax:.2f}"])

    # Make Payment Method on receipt
    DATA.append(["---------------------------"])
    DATA.append([f'Paid with {payment}', "", "", ""])


    # Calling the receipt module to get the PDF receipt
    receipt.make_receipt(DATA, 'receipt.pdf')



if __name__ == "__main__":
   main()