
class Product:
    def __init__(self, name, price, stock_quantity):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")

        self.__name = name
        self.__price = price
        self.__stock_quantity = stock_quantity

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock_quantity(self):
        return self.__stock_quantity

    def reduce_stock(self, quantity):
        if quantity > self.__stock_quantity:
            raise ValueError("Not enough stock available.")
        self.__stock_quantity -= quantity


class CartItem:
    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise ValueError("Invalid product.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > product.stock_quantity:
            raise ValueError("Quantity exceeds stock available.")

        self.__product = product
        self.__quantity = quantity

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    def total_price(self):
        return self.__product.price * self.__quantity

    def update_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.__product.stock_quantity:
            raise ValueError("Quantity exceeds stock available.")
        self.__quantity = quantity


class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_product(self, product, quantity):
        for item in self.__items:
            if item.product == product:
                item.update_quantity(item.quantity + quantity)
                return
        self.__items.append(CartItem(product, quantity))

    def remove_product(self, product_name):
        for item in self.__items:
            if item.product.name == product_name:
                self.__items.remove(item)
                return
        raise ValueError("Product not found in cart.")

    def view_cart(self):
        if not self.__items:
            print("Your cart is empty.")
        else:
            for item in self.__items:
                print(f"{item.product.name}: {item.quantity} @ {item.product.price} each")
        print(f"Total Price: {self.total_price()}")

    def total_price(self):
        total = sum(item.total_price() for item in self.__items)
        return total

    def checkout(self):
        if not self.__items:
            print("Your cart is empty.")
            return

        for item in self.__items:
            item.product.reduce_stock(item.quantity)

        print(f"Total amount to be paid: {self.total_price()}")
        self.__items = []  # Clear the cart after checkout

    def is_empty(self):
        return len(self.__items) == 0


class User:
    def __init__(self, username, password):
        if not username or not password:
            raise ValueError("Username and password cannot be empty.")
        self.__username = username
        self.__password = password
        self.__shopping_cart = ShoppingCart()

    @property
    def username(self):
        return self.__username

    @property
    def shopping_cart(self):
        return self.__shopping_cart

    def validate_password(self, password):
        return self.__password == password


def display_menu():
    print("\n1. Add product to cart")
    print("2. Remove product from cart")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")


def main():
    # Create some products
    product_catalog = [
        Product("Laptop", 1500, 10),
        Product("Phone", 800, 5),
        Product("Headphones", 150, 0),  # Stock is 0
        Product("Mouse", 50, 15),
    ]

    # Create a user
    print("Welcome to the Shopping Cart System")
    username = input("Enter username: ")
    password = input("Enter password: ")  # Password is now invisible
    user = User(username, password)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            # Add product to cart
            print("\nAvailable products:")
            available_products = [
                (i, product) for i, product in enumerate(product_catalog) if product.stock_quantity > 0
            ]
            
            if not available_products:
                print("No products are available at the moment.")
                continue

            for i, product in available_products:
                print(f"{i + 1}. {product.name} - {product.price} Rs  (Stock: {product.stock_quantity})")

            try:
                product_choice = int(input("Enter the product number to add to the cart: ")) - 1
                if product_choice < 0 or product_choice >= len(available_products):
                    raise ValueError("Invalid product choice.")
                quantity = int(input(f"Enter quantity for {available_products[product_choice][1].name}: "))
                user.shopping_cart.add_product(available_products[product_choice][1], quantity)
                print(f"Added {quantity} {available_products[product_choice][1].name}(s) to the cart.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            # Remove product from cart
            if user.shopping_cart.is_empty():
                print("Your cart is empty. Nothing to remove.")
            else:
                try:
                    product_name = input("Enter the product name to remove from the cart: ")
                    user.shopping_cart.remove_product(product_name)
                    print(f"Removed {product_name} from the cart.")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == "3":
            # View cart
            user.shopping_cart.view_cart()

        elif choice == "4":
            # Checkout
            user.shopping_cart.checkout()

        elif choice == "5":
            print("Thank you for using the Shopping Cart System. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
