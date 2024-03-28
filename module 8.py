from datetime import datetime
today = datetime.today()
today = today.strftime('%B %d, %Y')

class ItemToPurchase:
    def __init__(self, item_name = 'none', description=str(), item_price = float(0), item_quantity = int(0)):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = description
    
    def print_item_cost(self):
        item_total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${item_total}")
        return item_total
    
    def print_descriptions(self):
        print(f"{self.item_name}: {self.item_description}")
    
    def get_quantity(self):
        return self.item_quantity


class ShoppingCart:
    def __init__(self, customer_name, date=today):
        self.customer_name = customer_name
        self.date = date
        self.cart_items = []
        
    def add_item(self, item):
        self.cart_items.append(item)
    
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name.lower() == item_name.lower():
                found = True
                new_name = input("Enter the new name of the item: ")
                new_description = input("Enter the new description of the item: ")
                new_price = float(input("Enter the new price of the item: "))
                new_quantity = int(input("Enter the new quantity of the item: "))
                item.item_name = new_name
                item.item_description = new_description
                item.item_price = new_price
                item.item_quantity = new_quantity
                break

        if not found:
            print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        return len(self.cart_items)
    
    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total = total + item.print_item_cost()
        return total
    def print_total(self):
        total = 0
        total_quantity = 0
        print(f"{self.customer_name}'s Shopping Cart - {self.date}")
        for item in self.cart_items:
            total_quantity = total_quantity + item.get_quantity()
        print('Number of Items: ' + str(total_quantity))
        if len(self.cart_items) > 0:
            for item in self.cart_items:
                total = total + item.print_item_cost()
            print('Total: $' + str(total))
        else:
            print('SHOPPING CART IS EMPTY')
    def print_descriptions(self):
        if len(self.cart_items) > 0:
            print(f"{self.customer_name}'s Shopping Cart - {self.date}")
            print('Item Descriptions')
            for item in self.cart_items:
                item.print_descriptions()
        else:
            print('SHOPPING CART IS EMPTY')
            

def print_menu(shopping_cart):
    menu_options = ['a', 'r', 'c', 'i', 'o', 'q']

    while True:
        print('')
        print('Menu')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print("i - Output items' descriptions")
        print('o - Output shopping cart')
        print('q - Quit')
        response = str(input('Choose an option: '))
        print('')
        if response not in menu_options:
            print('Please choose a valid response.')
        elif response == 'a':
            item_name = str(input(f'What is the name of the item: '))
            item_description = str(input(f'What is the description of the item : '))
            item_price = float(input(f'What is the price of the item: '))
            item_quantity = int(input(f'What is the quantity of the item: '))
            item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item)
        elif response == 'r':
            item_name = str(input('What is the name of the item you want to remove: '))
            shopping_cart.remove_item(item_name)
        elif response == 'c':
            item_name = str(input('What is the name of the item you want to modify: '))
            shopping_cart.modify_item(item_name)
        elif response == 'i':
            shopping_cart.print_descriptions()
        elif response == 'o':
            shopping_cart.print_total()
        else:
            break
#MAIN
#milestone1 test code
shopping_list = []
number_of_items = int(input("How many items are on the list: "))
for i in range(number_of_items):
    item_name = str(input(f'What is the name of item number {i + 1}: '))
    item_desc = str(input(f'What is the description of item number {i +1}: '))
    item_price = float(input(f'What is the price of item number {i + 1}: '))
    item_quantity = int(input(f'What is the quantity of item number {i + 1}: '))
    item = ItemToPurchase(item_name, item_desc, item_price, item_quantity)
    shopping_list.append(item)
print('TOTAL COST')
total = 0
for item in shopping_list:
    total = total + item.print_item_cost()
print('Total: $' + str(total))
print('')
#milestone 2/final test code
name = input('What is your name: \n')
date = input("What is today's date: \n")
print('Customer Name: ', name)
print("Today's date: ", date)
print('')

cart = ShoppingCart(name, date)

print_menu(cart)


