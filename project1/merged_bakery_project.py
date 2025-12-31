
# ---------- Product Class ----------
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.product_id} | {self.name} | ₹{self.price}")


# ---------- Customer Class ----------
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def display(self):
        print(f"{self.customer_id} | {self.name}")


# ---------- Order Class ----------
class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def total_price(self):
        return sum(item.price for item in self.items)

    def display(self):
        print(f"\nOrder ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print("Items:")
        for item in self.items:
            print(f"- {item.name} : ₹{item.price}")
        print(f"Total Amount: ₹{self.total_price()}")


# ---------- Sample Data ----------
products = [
    Product(1, "Chocolate Cake", 500),
    Product(2, "Fresh Bread", 50),
    Product(3, "Cup Cake", 40)
]

customers = [
    Customer(1, "Rahul"),
    Customer(2, "Anjali")
]

orders = []


# ---------- Menu Functions ----------
def show_products():
    print("\nAvailable Products:")
    for p in products:
        p.display()


def show_customers():
    print("\nCustomers:")
    for c in customers:
        c.display()


def create_order():
    show_customers()
    cust_input = input("Enter Customer ID: ")

    if not cust_input.isdigit():
        print("Please enter a valid numeric Customer ID.")
        return

    cust_id = int(cust_input)
    customer = next((c for c in customers if c.customer_id == cust_id), None)

    if not customer:
        print("Invalid Customer!")
        return

    order = Order(len(orders) + 1, customer)

    while True:
        show_products()
        pid_input = input("Enter Product ID to add (0 to finish): ")




        # ✅ Exit safely
        if pid_input == "0":
            break

        # ✅ Prevent crash
        if not pid_input.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        pid = int(pid_input)
        product = next((p for p in products if p.product_id == pid), None)

        if product:
            order.add_product(product)
            print("Product added.")
        else:
            print("Invalid Product ID.")

    orders.append(order)
    print("Order created successfully!")



def show_orders():
    if not orders:
        print("\nNo orders available.")
    else:
        for order in orders:
            order.display()


# ---------- Main Menu ----------
def main():
    while True:
        print("\n====== Bakery E-Commerce System ======")
        print("1. View Products")
        print("2. View Customers")
        print("3. Create Order")
        print("4. View Orders")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_products()
        elif choice == "2":
            show_customers()
        elif choice == "3":
            create_order()
        elif choice == "4":
            show_orders()
        elif choice == "5":
            print("Thank you for using Bakery System!")
            break
        else:
            print("Invalid choice! Try again.")


# ---------- Run Program ----------
if __name__ == "__main__":
    main()
