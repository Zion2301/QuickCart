from models import Admin, Customer, Rider, Product, Order, OrderStatus
import data_store as store

def register_user(username, password, role):
    if role == "Admin":
        user = Admin(username, password)
    elif role == "Customer":
        user = Customer(username, password)
    elif role == "Rider":
        user = Rider(username, password)
    else:
        return None
    store.users.append(user)
    return user

def login(username, password):
    for user in store.users:
        if user.username == username and user.password == password:
            return user
    return None

def add_product(name, price, stock):
    pid = len(store.products) + 1
    product = Product(pid, name, price, stock)
    store.products.append(product)
    return product

def place_order(customer, items):
    oid = len(store.orders) + 1
    order = Order(oid, customer, items)
    store.orders.append(order)
    customer.order_history.append(order)
    return order

def assign_order(order, rider):
    if order.status == OrderStatus.PENDING:
        order.status = OrderStatus.ASSIGNED
        order.assigned_rider = rider
        rider.assigned_orders.append(order)
        return True
    return False

def update_order_status(order, status):
    if status in [OrderStatus.ASSIGNED, OrderStatus.DELIVERED]:
        order.status = status
        return True
    return False
