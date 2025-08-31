from services import *
from models import OrderStatus

def main_menu():
    while True:
        print("\n=== QuickCart ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            role = input("Role (Admin/Customer/Rider): ").title()
            username = input("Username: ")
            password = input("Password: ")
            user = register_user(username, password, role)
            print("Registered:", user)

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            user = login(username, password)
            if user:
                print(f"Welcome {user.username} ({user.role.value})")
                if user.role.value == "Admin":
                    admin_menu(user)
                elif user.role.value == "Customer":
                    customer_menu(user)
                else:
                    rider_menu(user)
            else:
                print("Invalid login!")

        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def admin_menu(admin):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Product")
        print("2. View Orders")
        print("3. Logout")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Product name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            product = add_product(name, price, stock)
            print("Added:", product)

        elif choice == "2":
            for order in store.orders:
                print(order)

        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def customer_menu(customer):
    while True:
        print("\n--- Customer Menu ---")
        print("1. Browse Products")
        print("2. Place Order")
        print("3. View History")
        print("4. Logout")
        choice = input("Choose: ")

        if choice == "1":
            for product in store.products:
                print(product)

        elif choice == "2":
            items = []
            while True:
                pid = int(input("Product ID (0 to finish): "))
                if pid == 0: break
                qty = int(input("Quantity: "))
                product = next((p for p in store.products if p.id == pid), None)
                if product and product.stock >= qty:
                    product.stock -= qty
                    items.append((product, qty))
                else:
                    print("Invalid or insufficient stock!")
            if items:
                order = place_order(customer, items)
                print("Order placed:", order)

        elif choice == "3":
            for order in customer.order_history:
                print(order)

        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def rider_menu(rider):
    while True:
        print("\n--- Rider Menu ---")
        print("1. View Pending Orders")
        print("2. Accept Order")
        print("3. Update Delivery Status")
        print("4. Logout")
        choice = input("Choose: ")

        if choice == "1":
            for order in store.orders:
                if order.status == OrderStatus.PENDING:
                    print(order)

        elif choice == "2":
            oid = int(input("Order ID to accept: "))
            order = next((o for o in store.orders if o.id == oid), None)
            if order and assign_order(order, rider):
                print("Order accepted:", order)
            else:
                print("Invalid order!")

        elif choice == "3":
            oid = int(input("Order ID: "))
            order = next((o for o in rider.assigned_orders if o.id == oid), None)
            if order:
                update_order_status(order, OrderStatus.DELIVERED)
                print("Updated:", order)
            else:
                print("Not your order!")

        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
