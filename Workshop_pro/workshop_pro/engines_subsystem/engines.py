"""
This file has some classes related to engines, including engine types.
This is part of the Abstract Factory implementation for the Engines Sub-system.

Author: Carlos Sierra - cavirguezs@udistrital.edu.co
"""


class Engine:
    """
    This class represents an abstraction of an engine for any vehicle.

    Attributes:
        torque (int): The torque of the engine
        maximum_speed (int): The maximum speed of the engine
        dimenssions (str): The dimenssions of the engine
        power (int): The power of the engine
        stability (str): The stability of the engine
        weight (float): The weight of the engine

    Methods:
        get_power(self) -> int: This method returns the power of the engine.
        get_weight(self) -> float: This method returns the weight of the engine.
    """

    def __init__(
        self,
        torque: int,
        maximum_speed: int,
        dimenssions: str,
        power: int,
        stability: str,
        weight: float,
    ):
        self.__torque = torque
        self.__maximum_speed = maximum_speed
        self.__dimenssions = dimenssions
        self.__power = power
        self.__stability = stability
        self.__weight = weight

    def get_power(self) -> int:
        """This method returns the power of the engine."""
        return self.__power

    def get_weight(self) -> float:
        """This method returns the weight of the engine."""
        return self.__weight

    def is_in_speed(self, min_speed: int, max_speed: int) -> bool:
        """This method returns if the engine is in the range of speeds."""
        return min_speed <= self.__maximum_speed <= max_speed

    def __str__(self) -> str:
        return f"Engine: torque={self.__torque}, " \
               f"maximum_speed={self.__maximum_speed}, " \
               f"dimenssions={self.__dimenssions}, " \
               f"power={self.__power}, " \
               f"stability={self.__stability}, " \
               f"weight={self.__weight}"


class GasEngine(Engine):
    """This class represents the behavior of a gas engine"""

class ElectricEngine(Engine):
    """This class represents the behavior of an electric engine"""


class HybridEngine(Engine):
    """
    This class represents the behavior of a hybrid engine.

    Attributes:
        watts (float): The wattage of the engine
        
    Methods:
        __init__(self, torque: int, maximum_speed: int, dimenssions: str,
                 power: int, stability: str, weight: float, watts: float):
            Initializes a new HybridEngine instance with the given parameters.
    gio Sanabria
    """

    def __init__(
        self,
        torque: int,
        maximum_speed: int,
        dimenssions: str,
        power: int,
        stability: str,
        weight: float,
        watts: float
    ):
        super().__init__(torque, maximum_speed, dimenssions, power, stability, weight)
        self.__watts = watts
    def __str__(self):
        return super().__str__() + f", watts={self.__watts}"
