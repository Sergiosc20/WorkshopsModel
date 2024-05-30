"""
This file has some test classes related to the implementation of an Abstract Factory Pattern Design.

Author: Carlos Sierra <cavirguezs@udistrital.edu.co>
"""
from workshop_pro.engines_subsystem.factories import HighEngineFactory, LowEngineFactory
from workshop_pro.engines_subsystem.engines import ElectricEngine, GasEngine, HybridEngine


class TestEngineFactories:
    """This class has different test cases to validate engines factories"""

    @classmethod
    def setup_class(cls):
        """
        This method is executed before each test method.
        """
        cls.high_engine_factory = HighEngineFactory()
        cls.low_engine_factory = LowEngineFactory()

    def test_create_high_electric_engine(self):
        """
        This method is a unit test for the create_electric_engine method
        of the HighEngineFactory class.
        """
        new_engine = self.high_engine_factory.create_electric_engine()
        assert isinstance(new_engine, ElectricEngine)
        assert (
            str(new_engine)
            == "Engine: torque=180, maximum_speed=300, dimenssions=200x200x200, power=200, stability=high, weight=100.9"
        )

    def test_create_high_gas_engine(self):
        """
        This method is a unit test for the create_gas_engine method
        of the HighEngineFactory class.
        """
        new_engine = self.high_engine_factory.create_gas_engine()
        assert isinstance(new_engine, GasEngine)
        assert (
            str(new_engine)
            == "Engine: torque=210, maximum_speed=400, dimenssions=210x200x250, power=250, stability=medium, weight=120.5"
        )
    
    def test_create_high_hybrid_engine(self):
        """
        This method is a unit test for the create_hybrid_engine method
        of the HighEngineFactory class.
        """
        new_engine = self.high_engine_factory.create_hybrid_engine()
        assert isinstance(new_engine, HybridEngine)
        assert (
            str(new_engine)
            == "Engine: torque=185, maximum_speed=320, dimenssions=200x210x220, power=210, stability=medium, weight=105.5, watts=54.2"
        )

    def test_create_low_electric_engine(self):
        """
        This method is a unit test for the create_electric_engine method
        of the LowEngineFactory class.
        """
        new_engine = self.low_engine_factory.create_electric_engine()
        assert isinstance(new_engine, ElectricEngine)
        assert (
            str(new_engine)
            == "Engine: torque=90, maximum_speed=100, dimenssions=100x100x100, power=50, stability=low, weight=63.4"
        )

    def test_create_low_gas_engine(self):
        """
        This method is a unit test for the create_gas_engine method
        of the LowEngineFactory class.
        """
        new_engine = self.low_engine_factory.create_gas_engine()
        assert isinstance(new_engine, GasEngine)
        assert (
            str(new_engine)
            == "Engine: torque=100, maximum_speed=150, dimenssions=110x100x150, power=100, stability=low, weight=80.5"
        )
    
    def test_create_low_hybrid_engine(self):
        """
        This method is a unit test for the create_hybrid_engine method
        of the LowEngineFactory class.
        """
        new_engine = self.low_engine_factory.create_hybrid_engine()
        assert isinstance(new_engine, HybridEngine)
        assert (
            str(new_engine)
            == "Engine: torque=95, maximum_speed=125, dimenssions=105x100x120, power=80, stability=low, weight=70.5, watts=35.6"
        )
