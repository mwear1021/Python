""" # OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class """

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.name = name
    
#     def get_data(self):
#         return f"Vehicle name: {self.name}, Top Speed: {self.max_speed}, Mileage: {self.mileage}"  

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers."
        
# # class Bus(Vehicle):
# #     def __init__(self, name, max_speed, mileage):
# #         super().__init__(name, max_speed, mileage)

# # school_bus = Bus("School Volvo", 180, 12)

# # output = Bus.get_data(school_bus)
# #print(output)

""" OOP Exercise 4: Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50. """

# class Bus(Vehicle):
#     def __init__(self, name, max_speed, mileage):
#         super().__init__(name, max_speed, mileage)

#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity)
    
# bus1= Bus("really cool bus", 450, 300500)

# print(bus1.seating_capacity(400))

""" OOP ex 5: Define a class attribute "color" with a default value white. I.e., Every Vehicle should be white."""

# class Vehicle:
#     color = "white"
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def get_data(self):
#         return f"Color: {Vehicle.color}; Vehicle name: {self.name}; Top speed: {self.max_speed}; Mileage: {self.mileage}"

# class Bus(Vehicle):
#     pass
        
# class Car(Vehicle):
#     pass

# bus1 = Bus("School Volvo", 180, 80)
# car1 = Car("Toyota Camry", 210, 350000)

# print(Bus.get_data(bus1))
# print(Car.get_data(car1))

"""OOP ex 6:
given: Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.
"""

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100
    
# class Bus(Vehicle):
#     pass

#     def fare(self):
#         maintenance_tax = .10
#         total = (self.capacity * 100 * maintenance_tax) + (self.capacity * 100)
#         return total

# bus1 = Bus("School Volvo", 12, 50)
# print(f"Total bus fare is {bus1.fare()}") #output: Total bus fare is 5500.0

"""
OOP EX 7: Write a program to determine which class a given Bus object belongs to.
"""

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
    
#     def get_class(self):
#         return type(self)


# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)
# print(Vehicle.get_class(School_bus))

"""
OOP EX 8: Determine if School_bus is also an instance of the Vehicle class
"""

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)

# print(isinstance(School_bus, Vehicle))  # True