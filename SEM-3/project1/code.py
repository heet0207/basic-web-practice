class FoodStore:
    def __init__(self):
        self.products = {
            1: {"name": "Pizza", "price": 250},
            2: {"name": "Burger", "price": 120},
            3: {"name": "Pasta", "price": 180},
            4: {"name": "Dabeli", "price": 50},
            5: {"name": "Drink", "price": 20}
        }
        self.cart = {}

    def display_products(self):
        print("\n--- Food Menu ---")
        print("ID\tItem\t\tPrice")
        for pid, item in self.products.items():
            print(f"{pid}\t{item['name']}\t\t₹{item['price']}")

    def add_to_cart(self):
        pid = int(input("Enter Product ID to add: "))
        if pid in self.products:
            qty = int(input("Enter quantity: "))
            if pid in self.cart:
                self.cart[pid]["qty"] += qty
            else:
                self.cart[pid] = {
                    "name": self.products[pid]["name"],
                    "price": self.products[pid]["price"],
                    "qty": qty
                }
            print("Item added to cart.")
        else:
            print("Invalid Product ID.")

    def remove_from_cart(self):
        pid = int(input("Enter Product ID to remove: "))
        if pid in self.cart:
            del self.cart[pid]
            print("Item removed from cart.")
        else:
            print("Item not found in cart.")

    def view_cart(self):
        if not self.cart:
            print("\nCart is empty.")
            return

        print("\n--- Your Cart ---")
        print("Item\tQty\tPrice\tTotal")
        total = 0
        for item in self.cart.values():
            item_total = item["qty"] * item["price"]
            total += item_total
            print(f"{item['name']}\t{item['qty']}\t₹{item['price']}\t₹{item_total}")
        print(f"Grand Total: ₹{total}")

    def checkout(self):
        if not self.cart:
            print("Cart is empty. Cannot checkout.")
            return
        self.view_cart()
        print("\nOrder placed successfully! 🍽️")
        self.cart.clear()

    def menu(self):
        while True:
            print("""
--- eCommerce Food Store ---
1. View Food Menu
2. Add to Cart
3. Remove from Cart
4. View Cart
5. Checkout
6. Exit
""")
            choice = input("Enter choice: ")

            if choice == "1":
                self.display_products()
            elif choice == "2":
                self.display_products()
                self.add_to_cart()
            elif choice == "3":
                self.remove_from_cart()
            elif choice == "4":
                self.view_cart()
            elif choice == "5":
                self.checkout()
            elif choice == "6":
                print("Thank you for visiting our Food Store! 😊")
                break
            else:
                print("Invalid choice. Try again.")


# Run the program
store = FoodStore()
store.menu()
