"""
This module defines both an interface and a concrete implementation for Catalogs.

Author: Carlos Andrés Sierra <cavirguezs@udistrital.edu.co>
"""

from typing import List

from .catalog_interface import Catalog
from ..vehicles_subsystem import Vehicle, VehiclesFacade


class CatalogConcrete(Catalog):
    """
    This is a concrete implementation of the Catalog interface.

    Methods:
        get_all_vehicles() -> List[Vehicle]: Returns a list of all vehicles in the catalog.
        get_by_speed(min_speed: int, max_speed: int) -> List[Vehicle]: Returns a list of vehicles 
            that have a speed between min_speed and max_speed.
        get_by_price(min_price: int, max_price: int) -> List[Vehicle]: Returns a list of vehicles 
            that have a price between min_price and max_price.
        add_vehicle(vehicle_type: str): Adds a vehicle to the catalog.
        remove_vehicle(vehicle: Vehicle): Removes a vehicle from the catalog.
        restore_deleted_vehicle(): Restores the last deleted vehicle.
        get_vehicle_by_model(model: str): Returns a vehicle by its model if found, otherwise None.
    """

    def __init__(self):
        self.__vehicles = []
        self.__vehicles_facade = VehiclesFacade()
        self.__vehicle_temp = None

    def get_all_vehicles(self) -> List[Vehicle]:
        """
        Returns a list of all vehicles in the catalog.
        """
        return self.__vehicles

    def get_by_speed(self, min_speed: int, max_speed: int) -> List[Vehicle]:
        """
        Returns a list of vehicles that have a speed between min_speed and max_speed.
        """
        return [
            vehicle
            for vehicle in self.__vehicles
            if vehicle.is_in_speed(min_speed, max_speed)
        ]

    def get_by_price(self, min_price: int, max_price: int) -> List[Vehicle]:
        """
        Returns a list of vehicles that have a price between min_price and max_price.
        """
        return [
            vehicle
            for vehicle in self.__vehicles
            if vehicle.is_in_price(min_price, max_price)
        ]

    def add_vehicle(self, vehicle_type: str):
        """
        Adds a vehicle to the catalog.

        Args:
            vehicle_type (str): The type of vehicle to add.
        """
        self.__vehicles.append(self.__vehicles_facade.create_vehicle(vehicle_type))

    def remove_vehicle(self, vehicle: Vehicle):
        """
        Removes a vehicle from the catalog.

        Args:
            vehicle (Vehicle): The vehicle to be removed.
        Update Sergio Sanabria
        """
        self.__vehicle_temp = vehicle
        self.__vehicles.remove(vehicle)

    def restore_deleted_vehicle(self):
        """
        Restores the last deleted vehicle.
        Create Sergio Sanabria
        """
        if self.__vehicle_temp:
            self.__vehicles.append(self.__vehicle_temp)
            self.__vehicle_temp = None

    def get_vehicle_by_model(self, model: str):
        """
        Returns a vehicle by its model if found, otherwise None.
        Create Sergio Sanabria
        """
        for vehicle in self.__vehicles:
            if vehicle.model == model:
                return vehicle
        return None
    