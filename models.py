from enum import Enum

class Role(Enum):
    ADMIN = "Admin"
    CUSTOMER = "Customer"
    RIDER = "Rider"

class User:
    def __init__(self, username, password, role: Role):
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f"{self.role.value}: {self.username}"

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, Role.ADMIN)

class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password, Role.CUSTOMER)
        self.order_history = []

class Rider(User):
    def __init__(self, username, password):
        super().__init__(username, password, Role.RIDER)
        self.assigned_orders = []

class Product:
    def __init__(self, pid, name, price, stock):
        self.id = pid
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"[{self.id}] {self.name} - ${self.price} (Stock: {self.stock})"

class OrderStatus(Enum):
    PENDING = "Pending"
    ASSIGNED = "Assigned"
    DELIVERED = "Delivered"

class Order:
    def __init__(self, oid, customer: Customer, items):
        self.id = oid
        self.customer = customer
        self.items = items  # list of (Product, qty)
        self.status = OrderStatus.PENDING
        self.assigned_rider = None

    def __str__(self):
        items_str = ", ".join([f"{p.name} x{q}" for p, q in self.items])
        rider = self.assigned_rider.username if self.assigned_rider else "None"
        return f"Order {self.id} | {self.customer.username} | {items_str} | {self.status.value} | Rider: {rider}"
