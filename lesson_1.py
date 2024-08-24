
# ООП - Объектно ориентированние программирование 

# class Person: # Класс чертеж
#     def __init__(self, name, lastname, age, nationalety): # __init__ : конструктор, self: сам объект 
#         self.name = name 
#         self.lastname = lastname
#         self.age = age
#         self.nationalety = nationalety
        
#     def info(self):
#         print(f"Имя: {self.name}, Фамилия: {self.lastname}, Возраст: {self.age}, Нация: {self.nationalety}")
        
# person = Person("Элиза", "Эркинбек кызы", 18, "Кыргыз")
# person.info()

# class Car: 
#     def __init__(self, model, year, color, volume):
#         self.model = model
#         self.year = year
#         self.color = color 
#         self.volume = volume
    
#     def info(self):
#         print(f"Модель машины: {self.model}, Год выпуска: {self.year}, Цвет: {self.color}, Объем: {self.volume}")
        
# bmw = Car('BMW', 2016, 'black', '2.5')
# lexus = Car('Lexus', '2023', 'White', '4')
# bmw.info()
# lexus.info()
    
# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def plus(self):
#         print(f'Ответ: {self.num1 + self.num2}')
        
#     def minus(self):
#         print(f'Ответ: {self.num1 - self.num2}')
        
#     def multiplication(self):
#         print(f'Ответ: {self.num1 * self.num2}')
        
#     def division(self):
#         print(f'Ответ: {self.num1 / self.num2}')
        
# num1 = float(input("Введите первое число: "))
# operator = input("+, -, *, /: ")
# num2 = float(input("Введите вторе число: "))

# calc = Calculator(num1, num2)

# if operator == '+':
#     calc.plus()
# elif operator == '-':
#     calc.minus()
# elif operator == '*':
#     calc.multiplication()
# elif operator == '/':
#     calc.division()
# else:
#     print("Неверный оператор")
    





# class Fruits:
#     def init(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight

#     def info(self):
#         print(f'Fruit: {self.name}, Color: {self.color}, Weight: {self.weight}g')

# # Создаем объекты класса Fruits
# apple = Fruits("Apple", "Red", 150)
# banana = Fruits("Banana", "Yellow", 120)
# cherry = Fruits("Cherry", "Red", 10)

# # Выводим информацию о каждом фрукте
# apple.info()
# banana.info()
# cherry.info()




# class Heroes:
#     def init(self, name, role, health):
#         self.name = name
#         self.role = role
#         self.health = health

#     def info(self):
#         print(f'Hero: {self.name}, Role: {self.role}, Health: {self.health} HP')

#     def attack(self):
#         print(f'{self.name} attacks the enemy!')

# # Создаем объекты класса Heroes
# hero1 = Heroes("Arthur", "Knight", 100)
# hero2 = Heroes("Merlin", "Mage", 80)
# hero3 = Heroes("Lancelot", "Warrior", 90)

# # Выводим информацию о каждом герое и выполняем действие
# hero1.info()
# hero1.attack()

# hero2.info()
# hero2.attack()

# hero3.info()
# hero3.attack()



# Fruit: Apple, Color: Red, Weight: 150g
# Fruit: Banana, Color: Yellow, Weight: 120g
# Fruit: Cherry, Color: Red, Weight: 10g
# Hero: Arthur, Role: Knight, Health: 100 HP
# Arthur attacks the enemy!
# Hero: Merlin, Role: Mage, Health: 80 HP
# Merlin attacks the enemy!
# Hero: Lancelot, Role: Warrior, Health: 90 HP
# Lancelot attacks the enemy!



# class Book:
#     def init(self, title, author):
#         self.title = title
#         self.author = author

#     def info(self):
#         print(f'Книга: "{self.title}", Автор: {self.author}')

# # Создаем объект класса Book
# book = Book("Война и мир", "Лев Толстой")

# # Выводим информацию о книге
# book.info()