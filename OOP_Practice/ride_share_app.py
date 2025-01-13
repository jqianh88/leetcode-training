'''
Problem: Design a system for a ride-sharing app (like Uber)
Imagine you're designing a simplified version of a ride-sharing app like Uber. The app needs to:
Keep track of users (drivers and passengers).
Match passengers with drivers based on their location.
Track trips from start to finish.
Key Classes to Design:
User class (with attributes like name, location, and type: passenger or driver).
Driver class (inherits from User and has additional attributes like car details).
Passenger class (inherits from User).
Trip class (tracks the trip's start time, end time, driver, and passenger).
Requirements:
Implement these classes with appropriate methods for the app's functionality.
What type of data structures would you use to store drivers and passengers?
How would you handle cases where no drivers are available?
Follow-Up:
How would you add support for surge pricing or rating drivers and passengers?

'''
# Figure out how to do schemas

# questions to ask:
# should location be an address, zip code, lat long
# What specific car details are needed, year make model color
# Do we need to get the user
# How large of a radius should we set to match drivers to passengers
import heapq
import math

# User class representing both drivers and passengers
class User:
    def __init__(self, name: str, location: tuple, type: str, rating: float, number_of_ratings: int):
        self.name = name
        self.location = location
        self.type = type
        self.rating = rating
        self.number_of_ratings = number_of_ratings

    def get_user(self):
        return {"name": self.name, "location": self.location, "type": self.type}

    def set_rating(self, rating: float):
        current_sum = self.rating * self.number_of_ratings
        self.number_of_ratings += 1
        new_rating = math.ceil((current_sum + rating) / self.number_of_ratings)
        self.rating = new_rating

    def get_location(self):
        return self.location

    def get_ratings(self):
        return self.rating, self.number_of_ratings


# Driver class inheriting from User
class Driver(User):
    def __init__(self, name, location: tuple, rating: float, number_of_ratings: int, car_details):
        super().__init__(name=name, location=location, type="driver", rating=rating, number_of_ratings=number_of_ratings)
        self.car_details = car_details
        self.is_available = True  # Initially all drivers are available

    def set_availability(self, availability: bool):
        self.is_available = availability

    def get_car_details(self):
        return self.car_details


# Passenger class inheriting from User
class Passenger(User):
    def __init__(self, name, location: tuple, rating: float, number_of_ratings: int):
        super().__init__(name=name, location=location, type="passenger", rating=rating, number_of_ratings=number_of_ratings)

    def calculate_distance(self, location1: tuple, location2: tuple):
        lat1, lon1 = location1
        lat2, lon2 = location2
        # Simple Euclidean distance (for demo purposes, replace with Haversine for real-world applications)
        return abs(lat1 - lat2) + abs(lon1 - lon2)

    def find_driver(self, drivers: list[Driver], mile_radius: int):
        available_drivers = []
        for driver in drivers:
            if driver.is_available and self.calculate_distance(self.location, driver.get_location()) <= mile_radius:
                distance = self.calculate_distance(self.location, driver.get_location())
                heapq.heappush(available_drivers, (distance, driver))

        if available_drivers:
            nearest_driver = heapq.heappop(available_drivers)[1]
            return nearest_driver
        else:
            return "No drivers available in your area."


# Trip class to manage the ride trip
class Trip:
    def __init__(self, passenger: Passenger, driver: Driver, start_time, base_fare=10.0):
        self.passenger = passenger
        self.driver = driver
        self.start_time = start_time
        self.end_time = None
        self.base_fare = base_fare
        self.surge_factor = 1.0  # Default surge pricing
        self.final_fare = self.calculate_final_fare()

    def calculate_final_fare(self):
        # Calculate final fare based on surge pricing
        return self.base_fare * self.surge_factor

    def complete_trip(self, end_time):
        self.end_time = end_time
        self.driver.set_availability(True)  # Driver becomes available again
        self.passenger.set_rating(self.driver.rating)
        self.driver.set_rating(self.passenger.rating)
        self.driver.set_availability(True)

    def apply_surge_pricing(self, current_demand, max_demand):
        if current_demand > max_demand:  # Surge pricing applied when demand exceeds supply
            self.surge_factor = 1.5  # Example surge pricing multiplier
        self.final_fare = self.calculate_final_fare()


# RideSharingSystem class to manage overall functionality
class RideSharingSystem:
    def __init__(self):
        self.drivers = []
        self.passengers = []
        self.current_demand = 0
        self.max_demand = 5  # Threshold for surge pricing

    def add_driver(self, driver):
        self.drivers.append(driver)

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def request_ride(self, passenger, mile_radius):
        # Find nearest available driver for the passenger
        driver = passenger.find_driver(self.drivers, mile_radius)

        if isinstance(driver, Driver):
            self.current_demand += 1
            ride = Trip(passenger, driver, "2024-01-01T10:00:00")  # example start time
            ride.apply_surge_pricing(self.current_demand, self.max_demand)
            driver.set_availability(False)  # Mark driver as unavailable during the trip
            print(f"Ride confirmed with {driver.name}, fare: ${ride.final_fare}")
            return ride
        else:
            print(driver)  # "No drivers available" message
            return None


if __name__ == '__main__':
    # Example Usage:

    # Create ride-sharing system
    system = RideSharingSystem()

    # Add drivers
    driver1 = Driver("John", (40.7128, -74.0060), 4.7, 100, {"make": "Toyota", "model": "Camry"})
    driver2 = Driver("Sarah", (40.730610, -73.935242), 4.8, 50, {"make": "Honda", "model": "Civic"})
    system.add_driver(driver1)
    system.add_driver(driver2)

    # Add passenger
    passenger = Passenger("Alice", (40.730610, -73.935242), 4.9, 20)
    system.add_passenger(passenger)

    # Passenger requests a ride
    ride = system.request_ride(passenger, mile_radius=5)

    # Complete the ride and provide feedback
    if ride:
        ride.complete_trip("2024-01-01T10:30:00")  # example end time
        print(f"Feedback: Driver's new rating: {driver1.rating}, Passenger's new rating: {passenger.rating}")


'''
Finding Nearby Drivers and Matching
To find nearby drivers, you could indeed use a heap queue (or priority queue) for efficiently selecting the closest available driver based on distance. Here's how we can approach it:

Location of Users: You can assume that the location is represented as a set of coordinates (latitude, longitude), which will allow us to compute the distance between the passenger and the drivers.
Distance Calculation: You can calculate the distance between two points (i.e., the passenger and a driver) using the Haversine formula to get the great-circle distance.
For efficiency, you'd want to sort the drivers based on distance. A min-heap (priority queue) would be suitable for this. Here's how you could handle the matching:

Data Structure:
Min-heap: A min-heap will allow you to efficiently extract the nearest driver to a passenger based on distance. Each element in the heap would be a tuple containing the distance to the passenger and the driver object.
Steps to Implement:
Store the available drivers.
For each driver, calculate the distance to the passenger.
Insert each driver into a min-heap with the distance as the priority.
When a passenger requests a driver, extract the nearest driver from the heap.
If no drivers are available, return a message.


Surge Pricing
Surge Pricing usually involves increasing the fare during times of high demand (e.g., more passengers than available drivers). You can adjust the price based on factors like:

Demand vs Supply: If the number of passengers is higher than available drivers, surge pricing can be applied.
Time of Day: Certain hours might have higher pricing, such as during peak commute times.
Steps to Implement Surge Pricing:
Demand Calculation: Track the number of passengers requesting rides and the number of available drivers.
Dynamic Fare Adjustment: If demand exceeds supply, increase the base fare by a multiplier.
Apply Surge Factor: When creating a trip, check the current surge factor and adjust the fare accordingly.

Here’s a complete solution to your ride-sharing system that includes:

Driver matching using a min-heap based on proximity (distance).
Surge pricing based on demand.
Driver availability (drivers can be marked as available or unavailable).
Dynamic fare calculation based on surge pricing.
Feedback system where both drivers and passengers can rate each other.
The solution will allow for:

Matching passengers to available drivers.
Handling surge pricing during high demand.
Calculating and adjusting fare dynamically.
Allowing passengers and drivers to rate each other.


Key Features Implemented:
Driver Availability: Drivers can be marked as available or unavailable based on whether they are currently in a ride.

set_availability() marks drivers as unavailable when they are booked and available after completing a trip.
Driver Matching:

find_driver() in the Passenger class matches the passenger with the nearest available driver within a specified radius (5 miles in the example).
A min-heap is used to efficiently find the nearest driver based on their location.
Surge Pricing:

The Trip class applies surge pricing if demand exceeds supply (current_demand > max_demand).
Surge pricing is represented as a surge_factor that modifies the base fare.
Feedback System:

Both drivers and passengers can rate each other at the end of the trip, and their ratings are updated accordingly.
set_rating() updates the average rating based on feedback.
Fare Calculation:

The final fare for a ride includes the base fare and any surge pricing.
How to Extend the System:
Multiple Trips per Driver: If you want to handle multiple trips per driver and track their schedule, you can implement a queue for each driver to track upcoming trips.
More Complex Surge Pricing: You can model surge pricing based on more factors such as time of day (e.g., higher prices during rush hour).
Route Optimization: Use graph-based algorithms to calculate the most efficient route for drivers, especially in large cities.
'''