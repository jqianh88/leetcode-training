'''
Problem: Design an Online Food Delivery System
You need to design an online food delivery system that includes the following functionalities:

Users can browse restaurants, place orders, and track their orders.
Restaurants can add/edit their menu and update order statuses.
The system should calculate the total price of an order, including taxes and delivery fees.
Support different payment methods (e.g., credit card, PayPal).
Ensure the system adheres to SOLID principles:
Open/Closed Principle: Adding new payment methods or user types should not require modifying existing code.
Liskov Substitution Principle: Subtypes should replace their parent types seamlessly.
Dependency Inversion: High-level modules should not depend on low-level modules.
'''

# answer
'''
LLD for Food Delivery System
Key Components
User:

Attributes: user_id, name, email, address, latitude, longitude.
Methods: get_user_details(), update_address().
Restaurant:

Attributes: restaurant_id, name, menu, location, rating.
Methods: get_menu(), get_details().
Order:

Attributes: order_id, user, restaurant, items, status, total_price.
Methods: calculate_total(), update_status().
Menu:

Attributes: menu_items, where each item includes name, price, description.
Methods: get_menu_items().
Delivery:

Attributes: delivery_id, order, delivery_status, current_location.
Methods: update_location(), get_delivery_status().
Payment:

Abstract class for extensibility.
Concrete Implementations: CreditCardPayment, UPIPayment, WalletPayment.
Methods: process_payment() (abstract in parent, overridden in child).
NotificationService:

Attributes: notifications (queue).
Methods: send_notification().
FoodDeliverySystem (Main Facade):

Aggregates services like UserService, OrderService, PaymentService, and DeliveryService.

'''

from abc import ABC, abstractmethod
from typing import List, Dict
from uuid import uuid4


# --- User Class ---
class User:
    def __init__(self, user_id: str, name: str, email: str, address: str, latitude: float, longitude: float):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

    def get_user_details(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "address": self.address
        }

    def update_address(self, new_address: str, new_lat: float, new_lon: float):
        self.address = new_address
        self.latitude = new_lat
        self.longitude = new_lon


# --- Restaurant Class ---
class Restaurant:
    def __init__(self, restaurant_id: str, name: str, menu: List[Dict], location: Dict, rating: float):
        self.restaurant_id = restaurant_id
        self.name = name
        self.menu = menu  # List of menu items: [{"name": str, "price": float, "description": str}]
        self.location = location  # {"latitude": float, "longitude": float}
        self.rating = rating

    def get_menu(self):
        return self.menu

    def get_details(self):
        return {
            "restaurant_id": self.restaurant_id,
            "name": self.name,
            "rating": self.rating,
            "location": self.location
        }


# --- Order Class ---
class Order:
    def __init__(self, order_id: str, user: User, restaurant: Restaurant, items: List[Dict], status: str = "Pending"):
        self.order_id = order_id
        self.user = user
        self.restaurant = restaurant
        self.items = items  # List of items: [{"name": str, "quantity": int, "price": float}]
        self.status = status

    def calculate_total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def update_status(self, new_status: str):
        self.status = new_status


# --- Payment Abstract Class ---
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount: float):
        print(f"Processing credit card payment of ${amount}...")
        return True


class UPIPayment(Payment):
    def process_payment(self, amount: float):
        print(f"Processing UPI payment of ${amount}...")
        return True


class WalletPayment(Payment):
    def process_payment(self, amount: float):
        print(f"Processing wallet payment of ${amount}...")
        return True


# --- Delivery Class ---
class Delivery:
    def __init__(self, delivery_id: str, order: Order, delivery_status: str = "Dispatched", current_location: Dict = None):
        self.delivery_id = delivery_id
        self.order = order
        self.delivery_status = delivery_status
        self.current_location = current_location or {"latitude": 0.0, "longitude": 0.0}

    def update_location(self, new_lat: float, new_lon: float):
        self.current_location = {"latitude": new_lat, "longitude": new_lon}

    def get_delivery_status(self):
        return {
            "delivery_id": self.delivery_id,
            "order_id": self.order.order_id,
            "status": self.delivery_status,
            "current_location": self.current_location
        }


# --- Notification Service ---
class NotificationService:
    def __init__(self):
        self.notifications = []

    def send_notification(self, message: str):
        self.notifications.append(message)
        print(f"Notification sent: {message}")


# --- FoodDeliverySystem (Facade) ---
class FoodDeliverySystem:
    def __init__(self):
        self.users = {}
        self.restaurants = {}
        self.orders = {}
        self.notifications = NotificationService()

    def register_user(self, name: str, email: str, address: str, lat: float, lon: float):
        user = User(str(uuid4()), name, email, address, lat, lon)
        self.users[user.user_id] = user
        print(f"User {name} registered.")
        return user

    def add_restaurant(self, name: str, menu: List[Dict], location: Dict, rating: float):
        restaurant = Restaurant(str(uuid4()), name, menu, location, rating)
        self.restaurants[restaurant.restaurant_id] = restaurant
        print(f"Restaurant {name} added.")
        return restaurant

    def place_order(self, user_id: str, restaurant_id: str, items: List[Dict], payment_method: Payment):
        user = self.users[user_id]
        restaurant = self.restaurants[restaurant_id]
        order = Order(str(uuid4()), user, restaurant, items)
        self.orders[order.order_id] = order

        # Process payment
        total_cost = order.calculate_total()
        if payment_method.process_payment(total_cost):
            order.update_status("Confirmed")
            self.notifications.send_notification(f"Order {order.order_id} has been placed.")
        return order


# --- Example Usage ---
if __name__ == "__main__":
    system = FoodDeliverySystem()

    # Register user
    user = system.register_user("John Doe", "john@example.com", "123 Main St", 37.7749, -122.4194)

    # Add restaurant
    restaurant = system.add_restaurant(
        "Pizza Palace",
        [{"name": "Pepperoni Pizza", "price": 12.99, "description": "Classic pizza with pepperoni."}],
        {"latitude": 37.7749, "longitude": -122.4194},
        4.5
    )

    # Place an order
    items = [{"name": "Pepperoni Pizza", "quantity": 2, "price": 12.99}]
    payment_method = CreditCardPayment()
    order = system.place_order(user.user_id, restaurant.restaurant_id, items, payment_method)
    print(f"Order placed: {order.order_id}")
