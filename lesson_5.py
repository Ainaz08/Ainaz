# # #Практика

# class car:
#     def __init__(self,brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.__mileage = 0

# def display_info(self):
#     print(f"Маркa{self.brand}, Модель:{self.model}, Год выпуска:{self.year}")

# def set.mileage(self,mileage):
        


        
# car = Car("Toyota", "Corolla", 2020)
# car.display_info()

# class ElectricCar(Car):
#     def _init_(self, brand, model, year,battery_capacity):
#         super()._init_(brand, model, year)
#         self.battery_capacity = battery_capacity

# def displey_battery_info(self):
#     print(f'емкость батереи: [seif.battery_capacity] kwh')

# car = ElectricCar("Tesla", "Model S", 2021, 100)
# car.display_info()
# car.display_battery_info()







# Метод __repr__: Этот магический метод используется для представления объекта в интерактивной консоли и должен возвращать строку, которая могла бы быть использована для создания такого же объекта.

# Метод __str__: Этот магический метод используется для преобразования объекта в строку, когда используется функция print.

# """Магические методы - dunder методы"""

# from typing import Any


# class Work:
#     def __init__(self, position, graphicks):
#         self.positon = position
#         self.graphicks = graphicks
    
    # def info(self):
    #     print(f"Позиция - {self.positon}, график - {self.graphicks}")
        
    # def __repr__(self):
    #      return f"Позиция - {self.positon}, график - {self.graphicks}"
     
    # def __str__(self):
    #     return f"Позиция - {self.positon}, график - {self.graphicks}"
    
#     def __call__(self):
#         print("Это магический метод __call__")
         
        
# work = Work("Бухгалтер", "8/5")
# print(work)
# work.info()


# def work():
#     print ("hello")

# print(work())




