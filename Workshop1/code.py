# -*- coding: utf-8 -*-
"""code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XWOht95gje5M8oVJCIas3n9O-eswNY4d
"""

"""
This file contains the code of workshop 1 which is about a vehicle project

Author: Sergio Andres Sanabria Castillo
Date: 15-03-2024
"""
class Engine:
    """This engine class represents the parameters and functions of the class"""
    #constructor
    def __init__(self, name, Type, potency, weight):
        #atributes of the class
        self.name = None
        self.Type = None
        self.potency = None
        self.weight = None

    def get_potency(self):
        return self.potency
        """
        This method returns the power of engine
        Returns:
        -(str): potency
        """
    def get_weight(self):
        return self.weight
        """
        This method returns the power of engine
        Returns:
        -(str): weight
        """
    @classmethod
    def crearMotor(cls):
        name = input("Ingrese el nombre del motor: ")
        Type = input("Ingrese el tipo del motor: ")
        potency = float(input("Ingrese la potencia del motor: "))
        weight = float(input("Ingrese el peso del motor: "))
        engine = cls(name, Type, potency, weight)
        return engine

class Vehicle:
    """This engine class vehicle the parameters and functions of the class"""
    #constructor
    def __init__(self, model, chassis, year,engine ):
        #atributes of the class
        self.model = None
        self.chassis = None
        self.year = None
        self.engine = engine

    def calculate_consumption(self):
        base_consumption = 1.1 * self.engine.potency + 0.2 * self.engine.weight
        if self.chassis == 'A':
            return base_consumption - 0.3
        elif self.chassis == 'B':
            return base_consumption - 0.5
        else:
            return base_consumption
    def crear_vehiculo():
        print("\nTipos de vehículos disponibles:")
        print("1. Carro")
        print("2. Camión")
        print("3. Yate")
        print("4. Motocicleta")
        Type = input("Seleccione el tipo de vehículo que desea crear: ")

        model = input("Ingrese el modelo del vehículo: ")
        chassis = input("Ingrese el chasis del vehículo (A, B): ")
        year = (input("Ingrese el año del vehículo: "))
        engine = escoger_motor()

        if Type == "1":
            num_doors = int(input("Ingrese el número de puertas del carro: "))
            vehicle = Car(model, chassis, year, engine, num_doors)
        elif Type == "2":
            max_load = float(input("Ingrese la carga máxima del camión: "))
            vehicle = Truck(model, chassis, year, engine, max_load)
        elif Type == "3":
            length = float(input("Ingrese la longitud del yate: "))
            vehicle = Yacht(model, chassis, year, engine, length)
        elif Type == "4":
            is_offroad = input("¿Es la motocicleta para todo terreno? (si/no): ").lower() == "si"
            vehicle = Motorcycle(model, chassis, year, engine, is_offroad)
        else:
            print("Tipo de vehículo no válido.")
            return

        vehicle.append(vehicle)
        print("Vehículo creado con éxito.")



class Car(Vehicle):
    """This car class is a class extend of vehicle"""
    def __init__(self, model, chassis, year, engine, num_doors):
        super().__init__(model, chassis, year, engine)
        self.num_doors = num_doors

class Truck(Vehicle):
    """This Truck class is a class extend of vehicle"""
    def __init__(self, model, chassis, year, engine, max_load):
        super().__init__(model, chassis, year, engine)
        self.max_load = max_load

class Yacht(Vehicle):
    """This Yacht class is a class extend of vehicle"""
    def __init__(self, model, chassis, year, engine, length):
        super().__init__(model, chassis, year, engine)
        self.length = length

class Motorcycle(Vehicle):
    """This Motorcycle class is a class extend of vehicle"""
    def __init__(self, model, chassis, year, engine, is_offroad):
        super().__init__(model, chassis, year, engine)
        self.is_offroad = is_offroad
#####MENU
def main():
   while True:
    print("\n*** Menú ***")
    print("1. Crear Motor")
    print("2. Crear Vehículo")
    print("3. Mostrar Todos los Vehículos Registrados")
    print("4. Encontrar Vehículo por Año")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        motor = Engine.crear_motor()
        print("Motor creado con éxito:", motor.name)
    elif opcion == "2":

    elif opcion == "3":

    elif opcion == "4":

    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

main()
