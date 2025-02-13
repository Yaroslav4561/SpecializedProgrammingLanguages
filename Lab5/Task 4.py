class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price 
        self.quantity = quantity  

    @property
    def total_price(self):
        return self.price * self.quantity


class Order:
    def __init__(self):
        self._items = []  
        self._total_price = 0 


    def add_item(self, item):
        self._items.append(item)
        self._total_price += item.total_price

    @property
    def total_price(self):
        return self._total_price

    def print_order_details(self):
        print("Order details:")
        for item in self._items:
            print(f"{item.name} - {item.quantity} x {item.price} = {item.total_price}")
        print(f"Total Price: {self._total_price}")


class Customer:
    def __init__(self, name, email):
        self.name = name  
        self.email = email 

    def place_order(self):
        return Order()


class OrderProcessor:
    def process_order(self, order):
        print("Processing your order...")
        total_price = order.total_price
        print(f"The total price of your order is: {total_price}")
        order.print_order_details()


customer = Customer("John Doe", "johndoe@example.com")


order = customer.place_order()


order.add_item(Item("Laptop", 1000, 1))
order.add_item(Item("Mouse", 50, 2))
order.add_item(Item("Keyboard", 150, 1))

processor = OrderProcessor()
processor.process_order(order)
