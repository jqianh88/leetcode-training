'''
Problem: Design a Parking Lot System
You need to design a Parking Lot System that:
Allows parking of different vehicle types (e.g., car, truck, motorcycle).
Tracks available and occupied spaces.
Handles parking and leaving vehicles efficiently.
Optionally, includes billing (bonus feature).

Classes:
- ParkingLot
    - available_spaces: dict(string, list)   {"small": [], "medium": []...}
    - spaces: list
- ParkingSpaces
    - size
    - is_occupied
- Vehicle
    - size
    - license_plate

Methods:
    ParkingLot
    - get_available_spaces() -> list
    - park_vehicle(vehicle: Vehicle) -> string
        - get_availabile_spaces -> returns a list based on size
        - choose the last one from the list -> ParkingSpace
            - parking_space.park_vehicle

    - unpark_vehicle(vehicle: Vehicle, parking_space: ParkingSpace) -> string
        - get_available_spaces
        - add the spot back into the list
        - parking_space.remove_vehicle()
    ParkingSpace
    - park_vehicle() -> bool
        - check is the spot occupied
        - check if the vehicle size and the parking space size match
        - flip is_occupied flag to True
        - return True
    - remove_vehicle -> bool:
        - check if the spot is not occupied
        - Return False becuase you can't remove an unnoccupied spot
        - flip is_occupied flag to False
        - return False
'''



class Vehicle:
    def __init__(self, size, license_plate):
        self.size = size
        self.license_plate = license_plate

class ParkingSpaces:
    def __init__(self, size, is_occupied, space_id):
        self.size = size
        self.is_occupied = is_occupied
        self.space_id = space_id

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        if self.is_occupied:
            return False
        if vehicle.size != self.size:
            return False
        self.is_occupied = True
        return True

    def remove_vehicle(self) -> bool:
        if not self.is_occupied:
            return False
        self.is_occupied = False
        return False

class ParkingLot:
    def __init__(self, spaces, available_spaces: ParkingSpaces):
        self.spaces = spaces
        self.available_spaces = available_spaces

    def get_available_spaces(self, vehicle: Vehicle) -> list[ParkingSpaces]:
        return self.available_spaces[vehicle.size]

    def park_vehicle(self, vehicle: Vehicle) -> str:
        try:
            available_spaces = self.get_available_spaces(vehicle=vehicle)
            parking_space = available_spaces.pop()
            parking_space.park_vehicle(vehicle=vehicle)

            return f"Successfully parked {vehicle.license_plate} into {parking_space.space_id}."
        except Exception as e:
            raise f"Unable to park {vehicle.license_plate} into {parking_space.space_id}." from e

    def unpark_vehicle(self, vehicle: Vehicle, parking_space: ParkingSpaces) -> str:
        try:
            available_spaces = self.get_available_spaces(vehicle=vehicle)
            parking_space.remove_vehicle()
            available_spaces.append(parking_space)
            return f"Successfully unparked {vehicle.license_plate} and left the parking space {parking_space.space_id}."
        except Exception as e:
            raise f"Unable to unpark {vehicle.license_plate} from parking space {parking_space.space_id}." from e