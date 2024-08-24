# # Инкапсуляция

# class Publikexample :
#     def __init__(self, value) : 
#         self.value = value #Публичный атрибут

#     def info(self):
#         return self.value # Публичный метод
    

# public = Publikexample(42)

# print(public.info()) #Вызов публичный метод
# print(public.value) #Доступ к публичному атрибуту

# #Защищенный

# class Publikexample :
#     def __init__(self,value):
#         self._value = value # Защищенный атрибут

#     def info(self):
#         return self._value # Защищенный метод
    
# protected = Publikexample(43)
# print(protected._value)
# print(protected._info())

# #Приватный

# class  Publikexample :
#     def __init__(self,value):
#          self._value = value # Приватный атрибут

#       def info(self):
#         return self._value #Приватный метод
    
#     def access_private(self):
#         return self._info() 
    
# private =  Publikexample(55)
# print()

    











    
# class Car:
#     def init(self, make, model, year, mileage):
#         # Public attributes
#         self.make = make  # Car make
#         self.model = model  # Car model
        
#         # Protected attributes
#         self._year = year  # Car year of manufacture
        
#         # Private attributes
#         self.__mileage = mileage  # Car mileage
    
#     # Public method to display car information
#     def display_info(self):
#         print(f"Car make: {self.make}, Model: {self.model}")
    
#     # Protected method to calculate the car's age
#     def _calculate_age(self):
#         from datetime import datetime
#         current_year = datetime.now().year
#         return current_year - self._year
    
#     # Private method to update the mileage
#     def __update_mileage(self, new_mileage):
#         if new_mileage > self.__mileage:
#             self.__mileage = new_mileage
#         else:
#             print("New mileage must be greater than the current mileage.")
    
#     # Public method to set the mileage
#     def set_mileage(self, new_mileage):
#         self.__update_mileage(new_mileage)
    
#     # Public method to get the mileage
#     def get_mileage(self):
#         return self.__mileage
    
# # Example script to test the Car class
# if name == "main":
#     # Create an instance of the Car class
#     my_car = Car("Toyota", "Camry", 2015, 50000)
    
#     # Access public attributes and methods
#     print(my_car.make)  # Toyota
#     print(my_car.model)  # Camry
#     my_car.display_info()  # Car make: Toyota, Model: Camry
    
#     # Access protected attributes and methods (not recommended)
#     print(my_car._year)  # 2015
#     print(my_car._calculate_age())  # Car's age based on the current year
    
#     # Access private attributes and methods (not recommended and will fail)
#     # print(my_car.__mileage)  # AttributeError
#     # my_car.__update_mileage(60000)  # AttributeError
    
#     # Using public method to set and get private attribute
#     my_car.set_mileage(60000)
#     print(my_car.get_mileage())  # 60000
    
#     # Trying to set a lower mileage
#     my_car.set_mileage(55000)  # New mileage must be greater than the current mileage.
#     print(my_car.get_mileage())  # 60000








#     class Car:
#     def init(self, make, model, year, mileage, fuel_efficiency, owner_name):
#         # Public attributes
#         self.make = make
#         self.model = model
        
#         # Protected attributes
#         self._year = year
        
#         # Private attributes
#         self.__mileage = mileage
#         self.__fuel_efficiency = fuel_efficiency  # Fuel efficiency in mpg
#         self.__owner_name = owner_name  # Owner's name
    
#     # Public method to display car information
#     def display_info(self):
#         print(f"Car make: {self.make}, Model: {self.model}")
    
#     # Protected method to calculate the car's age
#     def _calculate_age(self):
#         from datetime import datetime
#         current_year = datetime.now().year
#         return current_year - self._year
    
#     # Private method to update the mileage
#     def __update_mileage(self, new_mileage):
#         if new_mileage > self.__mileage:
#             self.__mileage = new_mileage
#         else:
#             print("New mileage must be greater than the current mileage.")
    
#     # Public method to set the mileage
#     def set_mileage(self, new_mileage):
#         self.__update_mileage(new_mileage)
    
#     # Public method to get the mileage
#     def get_mileage(self):
#         return self.__mileage
    
#     # Public method to get fuel efficiency
#     def get_fuel_efficiency(self):
#         return self.__fuel_efficiency
    
#     # Public method to get owner name
#     def get_owner_name(self):
#         return self.__owner_name
    
# # Example script to test the Car class
# if name == "main":
#     # Create an instance of the Car class with additional attributes
#     my_car = Car("Toyota", "Camry", 2015, 50000, 30, "John Doe")
    
#     # Access new attributes and methods
#     print(my_car.get_fuel_efficiency())  # 30
#     print(my_car.get_owner_name())  # John Doe











class Computer:
    def init(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __make_computations(self):
        addition = self.cpu + self.memory
        subtraction = self.cpu - self.memory
        multiplication = self.cpu * self.memory
        if self.__memory != 0:
            division = self.cpu / self.memory
        else:
            division = "undefined (division by zero)"
        return addition, subtraction, multiplication, division

    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    def info(self):
        addition, subtraction, multiplication, division = self.__make_computations()
        return (f"Computer Info:\n"
                f"CPU: {self.__cpu}\n"
                f"Memory: {self.__memory}\n"
                f"Addition: {addition}\n"
                f"Subtraction: {subtraction}\n"
                f"Multiplication: {multiplication}\n"
                f"Division: {division}")

class Laptop(Computer):
    def init(self, cpu, memory, memory_card):
        super().init(cpu, memory)
        self.__memory_card = memory_card

    def get_memory_card(self):
        return self.__memory_card

    def info(self):
        base_info = super().info()
        return f"{base_info}\nMemory Card: {self.__memory_card}"

# Создаем объекты и тестируем методы
desktop = Computer(3.5, 16)
laptop = Laptop(2.8, 8, 512)

# Распечатываем информацию об объектах
print(desktop.info())
print()
print(laptop.info())

# Пробуем геттеры
print("Desktop CPU:", desktop.get_cpu())
print("Desktop Memory:", desktop.get_memory())
print("Laptop Memory Card:", laptop.get_memory_card())