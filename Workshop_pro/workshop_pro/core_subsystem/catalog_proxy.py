"""
This module has a singleton implementation of a catalog including the 
addition of decorators.

Author: Carlos Andrés Sierra <cavirguezs@udistrital.edu.co>
"""

from ..catalog_subsystem import Catalog, TimeDecorator, MemoryDecorator
from ..observability_subsystem import Observability


class CatalogProxy:
    """This class is a proxy for the catalog class."""

    _instance = None
    __vehicle_name = []
    __vehicle_price = []
    __vehicle_speed = []
    __price = []
    __speed = []

    def __new__(cls, *args, **kwargs):
        """
        Ensures only one instance of CatalogProxy is created (Singleton pattern).
        """
        if not cls._instance:
            cls._instance = super(CatalogProxy, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Initializes the CatalogProxy with a catalog instance and decorators.
        """
        self.__catalog = Catalog()
        self.__catalog = TimeDecorator(self.__catalog)
        self.__catalog = MemoryDecorator(self.__catalog)

    def clear_memory(self):
        """
        Clears the memory attributes.
        """
        self.__vehicle_name = []
        self.__vehicle_price = []
        self.__vehicle_speed = []
        self.__price = []
        self.__speed = []

    def add_vehicle(self, username: str):
        """
        This method adds a vehicle to the catalog.

        Args:
            username (str): The username of the user who is adding the vehicle.
        """
        print(
            "Vehicle Types:\n\
            1. Car\n\
            2. Motorcycle\n\
            3. Truck\n\
            4. Yacht\n\
            5. Scooter\n\
            6. Helicopter\n"
        )
        vehicle_type = input("Vehicle type: ")
        # Delegate addition to catalog
        self.__catalog.add_vehicle(vehicle_type)
        # Log addition
        Observability.write_user_log(
            username.get_username(), "A new vehicle had been added."
        )
        # Clear memory
        self.clear_memory()

    def remove_vehicle(self):
        """
        Removes a vehicle from the catalog.
        Update Sergio Sanabria
        """
        model = input("Model: ")
        # Get vehicle by model
        vehicle = self.__catalog.get_vehicle_by_model(model)
        if not vehicle:
            raise ValueError("Vehicle not found.")
        # Remove vehicle from catalog
        self.__catalog.remove_vehicle(vehicle)

    def get_all_vehicles(self):
        """
        This method gets all vehicles from the catalog.
        Update Sergio Sanabria
        """
        if len(self.__vehicle_name) > 0:
            # Print cached vehicles
            
            for vehicle in self.__vehicle_name:
                print(str(vehicle))
        else:
            # Retrieve from catalog and cache
            for vehicle in self.__catalog.get_all_vehicles():
                print(str(vehicle))
                self.__vehicle_name.append(vehicle)

    def get_vehicles_by_speed(self):
        """
        This method gets vehicles by speed from the catalog.
        Update Sergio Sanabria
        """
        min_speed = input("Minimum speed: ")
        max_speed = input("Maximum speed: ")
        if min_speed == self.__speed[0] and max_speed == self.__speed[1]:
            # Print cached vehicles
            for vehicle in self.__vehicle_speed:
                print(str(vehicle))
        else:
            # Retrieve from catalog and cache
            for vehicle in self.__catalog.get_by_speed(min_speed, max_speed):
                print(str(vehicle))
                self.__vehicle_speed.append(vehicle)
            # Update cached speed range
            self.__speed[0] = min_speed
            self.__speed[1] = max_speed

    def get_vehicles_by_price(self):
        """
        Retrieves vehicles by price from the catalog.
        Create Sergio Sanabria
        """
        min_price = input("Minimum price: ")
        max_price = input("Maximum price: ")
        if min_price == self.__price[0] and max_price == self.__price[1]:
            # Print cached vehicles
            for vehicle in self.__vehicle_price:
                print(str(vehicle))
        else:
            # Retrieve from catalog and cache
            for vehicle in self.__catalog.get_by_price(min_price, max_price):
                print(str(vehicle))
                self.__vehicle_price.append(vehicle)
            # Update cached price range
            self.__price[0] = min_price
            self.__price[1] = max_price

    def restore_deleted_vehicle(self):
        """
        Restores the last deleted vehicle.
        Create Sergio Sanabria
        """
        self.__catalog.restore_deleted_vehicle()
