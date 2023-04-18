from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self.__check_if_user_exists(driving_license_number):
            return f'{driving_license_number} has already been registered to our platform.'
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f'{first_name} {last_name} was successfully registered under DLN-{driving_license_number}'

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type != 'PassengerCar' and vehicle_type != 'CargoVan':
            return f'Vehicle type {vehicle_type} is inaccessible.'
        if self.__check_if_vehicle_exists(license_plate_number):
            return f'{license_plate_number} belongs to another vehicle.'

        new_vehicle = self.__create_vehicle(vehicle_type, brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f'{brand} {model} was successfully uploaded with LPN-{license_plate_number}.'

    def allow_route(self, start_point: str, end_point: str, length: float):
        if self.__check_if_route_exists(start_point, end_point, length):
            return f'{start_point}/{end_point} - {length} km had already been added to our platform.'
        if self.__check_if_route_exists_with_less_length(start_point, end_point, length):
            return f'{start_point}/{end_point} shorter route had already been added to our platform.'
        else:
            new_route = self.__create_route(start_point, end_point, length)
            self.routes.append(new_route)
            if not new_route.is_locked:
                return f'{start_point}/{end_point} - {length} km is unlocked and available to use.'

    def make_trip(self, driving_license_number, license_plate_number, route_id,  is_accident_happened: bool):

        if self.__check_license_user(driving_license_number):
            return f'User {driving_license_number} is blocked in the platform! This trip is not allowed.'
        if self.__check_vehicle_is_damage(license_plate_number):
            return f'Vehicle {license_plate_number} is damaged! This trip is not allowed.'
        if self.__check_route_is_locked(route_id):
            return f'Route {route_id} is locked! This trip is not allowed.'
        user = self.__take_user(driving_license_number)
        vehicle = self.__take_vehicle(license_plate_number)
        if is_accident_happened and vehicle is not None:
            vehicle.is_damage = True
            user.decrease_rating()
        user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        selected_vehicles = []
        for vehicle in self.vehicles:
            if vehicle.is_damaged:
                selected_vehicles.append(vehicle)
        sorted_vehicles = sorted(selected_vehicles, key=lambda x: (x.brand, x.model))
        if len(sorted_vehicles) > count:
            taken_vehicles = self.__taken_vehicle(count, sorted_vehicles)
        taken_vehicles = sorted_vehicles
        for v in taken_vehicles:
            v.is_damaged = False
            v.battery_level = 100
        return f'{len(taken_vehicles)} vehicles were successfully repaired!'

    def users_report(self):
        result = '*** E-Drive-Rent ***'
        result_str = []
        for user in sorted(self.users, key=lambda x: (-x.rating)):
            result_str.append(user.__str__())
        result += '\n'.join(result_str)

    def __check_if_user_exists(self, driving_license_number):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return True
        return False

    def __check_if_vehicle_exists(self, license_plate_number):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return True
        return False

    def __create_vehicle(self, vehicle_type, brand, model, license_plate_number):

        if vehicle_type == 'PassengerCar':
            new_vehicle = PassengerCar(brand, model, license_plate_number)
            return new_vehicle
        elif vehicle_type == 'CargoVan':
            new_vehicle = CargoVan(brand, model, license_plate_number)
            return new_vehicle

    def __check_if_route_exists(self, start_point, end_point, length):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return True
        return False

    def __check_if_route_exists_with_less_length(self, start_point, end_point, length):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return True
        return False

    def __create_route(self, start_point, end_point, length):
        new_route_id = len(self.routes) + 1
        if self.__check_if_route_exists_with_greater_length(start_point, end_point, length):
            new_route = Route(start_point, end_point, length, new_route_id)
            new_route.is_locked = True
            return new_route

        new_route = Route(start_point, end_point, length, new_route_id)
        new_route.is_locked = False
        return new_route

    def __check_if_route_exists_with_greater_length(self, start_point, end_point, length):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                return True
        return False

    @staticmethod
    def __taken_vehicle(count, sorted_vehicles):
        return sorted_vehicles[:count]

    def __check_license_user(self, driving_license_number):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                if user.is_blocked:
                    return True
        return False

    def __check_vehicle_is_damage(self, license_plate_number):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                if vehicle.is_damaged:
                    return True
        return False

    def __take_user(self, driving_license_number):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return user
        return None

    def __take_vehicle(self, license_plate_number):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return vehicle
        return None

    def __check_route_is_locked(self, route_id):
        for route in self.routes:
            if route.route_id == route_id:
                if route.is_locked:
                    return True
        return False







