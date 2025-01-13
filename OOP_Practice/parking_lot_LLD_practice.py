class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ParkingGarage:
    def __init__(self, longitude, latitude, number_of_levels, parking_space_map):
        self.longitude = longitude
        self.latitude = latitude
        self.number_of_levels = number_of_levels
        self.parking_space_map = parking_space_map
        self.spaces_available = Node()

    def get_garage(self, longitude, latitude):
        # Find the closest garage based on distance
        # Call the db to get the list of garages
        # Calculate the distance between the vehicle and the garage
        pass



class Vehicle:
    def __init__(self):
        self.size = ""
        self.license_plate = ""

class Car(Vehicle):
    def __init__(self, size):
        super().__init__(size)
        self.size = "car"

class Truck(Vehicle):
    def __init__(self, size):
        super().__init__(size)
        self.size = "truck"

class Motorcycle(Vehicle):
    def __init__(self, size):
        super().__init__(size)
        self.size = "motorcycle"


class ParkingSpace:
    def __init__(self, garage_id, level, parking_space_id, is_occupied, size):
        self.garage_id = garage_id
        self.level = level
        self.parking_space_id = parking_space_id
        self.is_occupied = is_occupied
        self.size = size

    def park_vehicle(self, ):
        # update the parking space that it is now occupied
        # remove it from the linked list of available parking spots
        # update the spaces_available in the parking garage to remove it
        pass

    def remove_vehicle(self):
        # update the parking space that it is now vacant
        # add it to the linked list of available parking spots
        # update the spaces_available in the parking garage to add it back in
        pass

class Reservations:
    def __init__(self, start_time, end_time, billing_address, cost):
        self.start_time = start_time
        self.end_time = end_time
        self.billing_address = billing_address
        self.cost = cost

    def get_reservation(self):
        return f"Your reservation lasted from {self.start_time} to {self.end_time} and cost a total of {self.cost}."
