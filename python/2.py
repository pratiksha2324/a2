class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            raise ValueError("Insufficient stock available")


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def item_total_price(self):
        return self.product.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items.append(CartItem(product, quantity))
            product.reduce_stock(quantity)
        else:
            print(f"Insufficient stock for {product.name}. Available: {product.stock}")

    def remove_item(self, product_name):
        for item in self.items:
            if item.product.name == product_name:
                self.items.remove(item)
                print(f"{product_name} removed from cart.")
                return
        print(f"{product_name} not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("Items in Cart:")
            for item in self.items:
                print(f"{item.product.name}: {item.quantity} pcs @ {item.product.price} each")
            print(f"Total Price: ${self.calculate_total()}")

    def calculate_total(self):
        return sum(item.item_total_price() for item in self.items)

    def checkout(self):
        total_price = self.calculate_total()
        if total_price == 0:
            print("No items in the cart to checkout.")
        else:
            print(f"Checkout successful. Total Price: ${total_price}")
            self.items.clear()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.cart.add_item(product, quantity)

    def remove_from_cart(self, product_name):
        self.cart.remove_item(product_name)

    def view_cart(self):
        self.cart.view_cart()

    def checkout(self):
        self.cart.checkout()


# Example usage:
# Creating some products
product1 = Product("Laptop", 1200, 10)
product2 = Product("Headphones", 150, 5)

# Creating a user
user = User("john_doe", "password123")

# User adds items to the cart
user.add_to_cart(product1, 1)
user.add_to_cart(product2, 2)

# User views the cart
user.view_cart()

# User checks out
user.checkout()

# View the cart again (it should be empty after checkout)
user.view_cart()
