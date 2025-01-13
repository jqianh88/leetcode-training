'''
Problem: Design a Parking Lot System
You need to design a Parking Lot System that:
Allows parking of different vehicle types (e.g., car, truck, motorcycle).
Tracks available and occupied spaces.
Handles parking and leaving vehicles efficiently.
Optionally, includes billing (bonus feature).

Classes:
- ParkingLot
    - spaces: list[ParkingSpace]
    - available_spaces: dict[Size, list]

    get_available_spaces(vehicle: Vehicle) -> list[ParkingSpace]
        # ParkingLot.get(vehicle.size, [])

    add_parking_space(parking_space: ParkingSpace) -> int:
        # add to spaces
        # add to available spaces

    park_vehicle(vehicle: Vehicle) -> str
        get_availabile_spaces
        pick a spot
        space.park_vehicle


    unpark_vehicle(vehicle: Vehicle, space: ParkingSpace) -> str
        self.spaces.append(space)
        self.available_spaces.get(vehicle.size, []).append(space)
- ParkingSpace
    - space_id: int # should be a uuid
    - size: Size
    - is_occupied: bool

    park_vehicle(vehicle: Vehicle) -> bool
        is it occupied
        is the size right
        flip flag
        return true

    remove_vehicle() -> bool
        is it not occupied --> return False
        flip flag
        return True

- Vehicle
    - size: Size
    - license_plate
'''

from enum import Enum

class ParkingLotException(Exception):
    pass

class AddParkingSpaceException(ParkingLotException):
    pass
class ParkVehicleException(ParkingLotException):
    pass
class UnparkVehicleException(ParkingLotException):
    pass

class Size(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class Vehicle:
    def __init__(self, size: Size, license_plate: str):
        self.size = size
        self.license_plate = license_plate

class ParkingSpace:
    def __init__(self, space_id: int, size: Size, is_occupied: bool):
        self.space_id = space_id
        self.size = size
        self.is_occupied = is_occupied

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        if self.is_occupied:
            return False
        if self.size != vehicle.size:
            return False
        self.is_occupied = True
        return True

    def remove_vehicle(self) -> bool:
        if not self.is_occupied:
            return False
        self.is_occupied = False
        return True

class ParkingLot:
    def __init__(self):
        self.spaces = []
        self.available_spaces = {
            Size.SMALL: [],
            Size.MEDIUM: [],
            Size.LARGE: [],
        }

    def get_available_spaces(self, vehicle: Vehicle) -> list[ParkingSpace]:
        return self.available_spaces.get(vehicle.size)

    def add_parking_space(self, parking_space: ParkingSpace) -> int:
        try:
            self.spaces.append(parking_space)
            self.available_spaces.get(parking_space.size).append(parking_space)
            return parking_space.space_id
        except ParkingLotException as e:
            raise AddParkingSpaceException(f"Failed to add parking space {parking_space.space_id}") from e

    def park_vehicle(self, vehicle: Vehicle) -> str:
        try:
            available_spaces = self.get_available_spaces(vehicle=vehicle)
            parking_space = available_spaces.pop()
            parking_space.park_vehicle(vehicle=vehicle)
            return f"Successfully parked {vehicle.license_plate=} into {parking_space.space_id}."
        except ParkingLotException as e:
                raise ParkVehicleException(f"Failed to park vehicle with {vehicle.license_plate=} into {parking_space.space_id}") from e


    def unpark_vehicle(self, vehicle: Vehicle, parking_space: ParkingSpace) -> str:
        try:

            parking_space.remove_vehicle()
            self.available_spaces[parking_space.size].append(parking_space)
            return f"Successfully removed {vehicle.license_plate=} from {parking_space.space_id}."

        except ParkingLotException as e:
            raise UnparkVehicleException(f"Failed to remove vehicle with {vehicle.license_plate=} from {parking_space.space_id}") from e




'''
Refinements:
Areas for Improvement
Errors in Implementation:

Logical Issues in park_vehicle:

parking_space.park_vehicle() is called without passing the vehicle object.
This would raise an error as park_vehicle() in ParkingSpace expects a vehicle.
Improper Use of add_parking_space:

In unpark_vehicle, you're calling add_parking_space to re-add a parking space to the system. Instead, it should directly add the space back to available_spaces.
Lack of Testing Time:

If you're spending all your time writing code, you may not have time left for testing, which is critical in interviews.
Redundancy:

The current design could be optimized by reducing redundant method calls, especially in park_vehicle and unpark_vehicle.
Speed:

30+ minutes is fine for now, but the goal should be under 20–25 minutes, leaving time for explanation and edge case handling.

class ParkingSpace:
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        if self.is_occupied:
            raise ParkingLotException(f"Space {self.space_id} is already occupied.")
        if self.size != vehicle.size:
            raise ParkingLotException(f"Space {self.space_id} does not fit vehicle {vehicle.license_plate}.")
        self.is_occupied = True
        return True

class ParkingLot:
    def park_vehicle(self, vehicle: Vehicle) -> str:
        try:
            available_spaces = self.get_available_spaces(vehicle)
            if not available_spaces:
                raise ParkVehicleException(f"No available spaces for {vehicle.license_plate}.")
            parking_space = available_spaces.pop()
            parking_space.park_vehicle(vehicle)
            return f"Vehicle {vehicle.license_plate} parked in space {parking_space.space_id}."
        except ParkingLotException as e:
            raise ParkVehicleException(f"Failed to park vehicle {vehicle.license_plate}.") from e

    def unpark_vehicle(self, parking_space: ParkingSpace) -> str:
        try:
            parking_space.remove_vehicle()
            self.available_spaces[parking_space.size].append(parking_space)
            return f"Vehicle removed from space {parking_space.space_id}."
        except ParkingLotException as e:
            raise UnparkVehicleException(f"Failed to unpark vehicle from space {parking_space.space_id}.") from e


'''