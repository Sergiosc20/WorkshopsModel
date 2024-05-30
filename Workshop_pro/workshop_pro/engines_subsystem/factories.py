"""
This file has some classes related to the implementation of an Abstract Factory Pattern Design..

Author: Carlos Sierra - cavirguez@udistrital.edu.co
"""

from abc import ABC, abstractmethod

from .engines import ElectricEngine, GasEngine, HybridEngine


class AbstractEngineFactory(ABC):
    """
    This class is an abstract factory to create both gas and electric engines.

    Methods:
        create_electric_engine -> ElectricEngine: This method create an electric engine.
        create_gas_engine -> GasEngine: This method create a gas engine.
        create_gas_hybrid -> HybridEngine: This method create a hybrid engine.
    """

    @abstractmethod
    def create_electric_engine(self) -> ElectricEngine:
        """
        This method create an electric engine.

        Returns:
            An electric engine object.
        """

    @abstractmethod
    def create_gas_engine(self) -> GasEngine:
        """
        This method create a gas engine.

        Returns:
            A gas engine object.
        """

    @abstractmethod
    def create_hybrid_engine(self) -> HybridEngine:
        """
        This method create a hybrid engine.

        Returns:
            A hybrid engine object.

        Create Sergio Sanabria
        """


class HighEngineFactory(AbstractEngineFactory):
    """
    This class is a concrete factory to create expensive versions of engines.

    Methods:
        create_electric_engine -> ElectricEngine: This method create an expensive electric engine.
        create_gas_engine -> GasEngine: This method create an expensive gas engine.
    Update Sergio Sanabria
    """

    def create_electric_engine(self) -> ElectricEngine:
        return ElectricEngine(
            torque=180,
            maximum_speed=300,
            dimenssions="200x200x200",
            power=200,
            stability="high",
            weight=100.9,
        )

    def create_gas_engine(self) -> GasEngine:
        return GasEngine(
            torque=210,
            maximum_speed=400,
            dimenssions="210x200x250",
            power=250,
            stability="medium",
            weight=120.5,
        )
  
    def create_hybrid_engine(self) -> HybridEngine:
        return HybridEngine(
            torque=185,
            maximum_speed=320,
            dimenssions="200x210x220",
            power=210,
            stability="medium",
            weight=105.5,
            watts=54.2,
        )

class LowEngineFactory(AbstractEngineFactory):
    """
    This class is a concrete factory to create cheap versions of engines.

    Methods:
        create_electric_engine -> ElectricEngine: This method create a cheap electric engine.
        create_gas_engine -> GasEngine: This method create a cheap gas engine.
    Update Sergio Sanabria
    """

    def create_electric_engine(self) -> ElectricEngine:
        return ElectricEngine(
            torque=90,
            maximum_speed=100,
            dimenssions="100x100x100",
            power=50,
            stability="low",
            weight=63.4,
        )

    def create_gas_engine(self) -> GasEngine:
        return GasEngine(
            torque=100,
            maximum_speed=150,
            dimenssions="110x100x150",
            power=100,
            stability="low",
            weight=80.5,
        )

    def create_hybrid_engine(self) -> HybridEngine:
        return HybridEngine(
            torque=95,
            maximum_speed=125,
            dimenssions="105x100x120",  
            power=80,
            stability="low",
            weight=70.5,
            watts=35.6,
        )
