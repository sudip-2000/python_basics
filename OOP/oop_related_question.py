"""...................................................OOP related questions..............................."""

"""............................class and object..........................."""



#Create a class Person with attributes name and age.
# Write a method display() to print the person's details.
# Create an object of the class and call the method.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        

person_1 = Person("Ram", 25)
person_2= Person("Shyam", 30)

person_1.display()
person_2.display()


"""..................................................................................................."""





"""
Create a class Person with attributes name and age.
Add a method is_adult() that returns True if the person is 18 or older, otherwise False.
Instantiate two Person objects, one for a child and one for an adult,
and check if they are adults using the is_adult() method.

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def is_adult(self):
        if self.age>=18:
            return True
        else:
            return False
        
person_1 = Person("Ram", 50)
person_2 = Person("Shyam", 15)

print(person_1.is_adult())
print(person_2.is_adult())


""".................................................................................................................."""



#Create a class Circle with a method to calculate and return the area and perimeter of a circle.
# The radius should be passed during object creation.


class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
circle = Circle(5)

area=circle.area()
perimeter=circle.perimeter()

print("Area of circle:", area)
print("Perimeter of circle:", perimeter)


""".................................................................................................................."""


#Write a class Rectangle that has attributes length and width.
# Add methods to calculate and return the area and perimeter of the rectangle.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
rectangle = Rectangle(4, 6)

area=rectangle.area()
perimeter=rectangle.perimeter()

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)



"""..........................................................................................................................."""


#Create a class Car with attributes like brand, model, and price.
# Write methods to update the price and display car details.


class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def update_price(self, new_price):
        self.price = new_price
        
    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        
car = Car("Honda", "Civic", 2500000)

car.update_price(3000000)
car.display_details()



"""........................................................................................................................"""


"""
           Create a class Employee with the following:
A class variable num_employees that keeps track of the total number of employees.
An instance variable name for the employee's name.
A method display_info() to print the name and the total number of employees.

"""

class Employee:
    num_employees=0
    
    def __init__(self, name):
        self.name = name
        Employee.num_employees +=1
        
    def display_info(self):
        print("Name:" , self.name)
        print("Total number of employees:", Employee.num_employees)
        
employee_1 = Employee("Ram")
employee_2 = Employee("Shyam")
employee_3 = Employee("Hari")


employee_1.display_info()


""".................................................................................................................."""



"""
Write a class BankAccount with:
A class variable bank_name that is the same for all accounts.
Instance variables account_number and balance.
A method to display the account's details.

"""


class BankAccount:
    bank_name = "NIC Asia"
    
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def display_details(self):
        print("Bank Name:", BankAccount.bank_name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        
account_1 = BankAccount("123456", 50000)
account_2 = BankAccount("789012", 75000)

account_1.display_details()


"""......................................................................................................................."""



"""
Create a class Book with:
A class variable total_books.
A class method get_total_books() that returns the value of total_books.
"""


class Book:
    total_books = 0
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
book_1 = Book()
book_2 = Book()
book_3 = Book()

Book.total_books = 3

print("Total number of books:", Book.get_total_books())


"""..................................................................................................................."""


"""
Create a class Book with:
A class variable total_books.
A class method get_total_books() that returns the value of total_books.
"""


class Book:
    total_books = 0
    
    @staticmethod
    def get_total_books():
        return Book.total_books
    
book_1 = Book()
book_2 = Book()
book_3 = Book()

Book.total_books = 3

print("Total number of books:", Book.get_total_books())


"""..................................................................................................................."""


""".....................................encapsulation................................................."""

"""In Python, encapsulation is achieved using **access modifiers**:

1. **Public members:** These can be accessed from outside the class.
2. **Protected members:** These are intended to be used only within the class and its subclasses.
3. **Private members:** These are intended to be used only within the class itself and cannot be accessed directly from outside.
"""

#Create a class Employee with attributes name and salary.
# Make salary private and add getter and setter methods to access and update it.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        self.__salary = new_salary
        
employee=Employee("Ram", 50000)
print(employee.get_salary())

employee.set_salary(60000)
print(employee.get_salary())



""".................................................................................................................."""


#protected attribute and method

"""In Python, **protected members** are conventionally defined by prefixing the attribute or method with a single underscore (`_`). 
This indicates that these members should not be accessed directly from outside the class,
but Python does not enforce this restriction (it’s a convention)."""



class Car:
    def __init__(self, brand, model, price):
        self.brand = brand #public attribute
        self._model = model #protected attribute (_)
        self.__price = price #private attribute (__)
        
    def _display_details(self):    #protected method
        print("Brand:", self.brand)
        print("Model:", self._model)
        print("Price:", self.__price)
        
car = Car("Honda", "Civic", 2500000)


print(car.brand)
print(car._model)   # Accessing protected attributes (technically possible, but not recommended)
print(car._Car__price)  # Accessing private attribute via name mangling. not recommended as it is against the principles of encapsulations

car._display_details() 

        
        




"""......................................................................................................................"""


"""..............................................inheritance................................................."""


# single inheritance

"""In single inheritance, a subclass inherits from only one superclass.
"""

class Animal:
    def sound(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def bark(self):
        print("Dog barks")
        

dog = Dog()
dog.sound()
dog.bark()




"""......................................................................................................."""



#Multiple Inheritance

"""In multiple inheritance, a subclass inherits from more than one superclass.
Python allows this, but it's important to handle potential conflicts
that may arise if the same method is defined in multiple base classes."""

class Animal:
    def sound(self):
        print("Animal makes a sound")
        
class Flyable:
    def fly(self):
        print("Flyable can fly")
        
class Bird(Animal, Flyable):
    def sing(self):
        print("Bird sings")
        
bird = Bird()
bird.sound()
bird.fly()
bird.sing()



""".................................................................................................................."""


#multilevel inheritance


"""In multilevel inheritance, a subclass derives from another subclass, creating a chain of inheritance."""

class Animal:
    def sound(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def bark(self):
        print("Dog barks")
        
class Puppy(Dog):
    def wag_tail(self):
        print("Puppy wags its tail")
        
puppy = Puppy()
puppy.sound()
puppy.bark()
puppy.wag_tail()


""".........................................................................................................."""

#Hierarchical Inheritance

"""In hierarchical inheritance, multiple subclasses inherit from the same superclass."""

class Animal:
    def sound(self):
        print("animal makes a sound")
        
class Dog(Animal):
    def bark(self):
        print("Dog barks")
        
class Cat(Animal):
    def meow(self):
        print("Cat meows")
        
dog = Dog()
dog.sound()
dog.bark()

cat = Cat()
cat.sound()
cat.meow()


""".........................................................................................................."""


#Hybrid Inheritance

"""Hybrid inheritance is a combination of more than one type of inheritance. 
It can combine multiple inheritance, multilevel inheritance, etc."""


class Animal:
    def sound(self):
        print("Animal makes a sound")
        
class Mammal:
    def walk(self):
        print("Mammal walks")
        
class Dog(Animal, Mammal):
    def bark(self):
        print("Dog barks")
        
class Puppy(Dog):
    def wag_tail(self):
        print("Puppy wags its tail")
        
puppy = Puppy()
puppy.sound() #inherited from Animal
puppy.bark() #inherited from Dog
puppy.walk() #inherited from Mammal
puppy.wag_tail() #defined in Puppy



"""..............................................................................................."""

#Create a base class Animal with a method sound(). 
# Create derived classes Dog and Cat that override the sound() method.


class Animal:
    def sound(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def sound(self):
        print("Dog barks")
        
class Cat(Animal):
    def sound(self):
        print("Cat meows")
        
animal=Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()




"""..........................................................................................."""




"""
Create a class Employee with attributes name and salary.

Create subclasses Manager and Developer that inherit from Employee and add their own attributes.
In the subclasses, implement a method display_details() to print the employee's details.
Instantiate objects of both subclasses and display their details.
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        
    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        
class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        
    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        
manager = Manager("Ram", 50000)
developer = Developer("Shyam", 60000)

manager.display_details()
developer.display_details()
        

"""..................................................................................................................................."""



"""...............................polymorphism..........................."""

#Create a class Calculator with a method add() to add two numbers.
# Overload the add() method to also add three numbers.


class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    
    def add(self, num1, num2, num3=0):
        return num1 + num2 + num3
    
calculator = Calculator()
print(calculator.add(1, 2,5))
print(calculator.add(1, 2))


"""..........................................................................................."""

#Define a base class Shape with a method draw(). 
# Override the draw() method in derived classes Circle and Square to print different messages.


class Shape:
    def draw(self):
        print("Drawing a shape")
        
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")
        
class Square(Shape):
    def draw(self):
        print("Drawing a square")
        
shape = Shape()
shape.draw()

circle = Circle()
circle.draw()

square = Square()
square.draw()


"""....................................................................................................................."""

"""...............................Abstraction..............................."""



#Create an abstract class Vehicle with abstract methods start() and stop().
# Create concrete classes Car and Bike that implement these methods.

from abc import ABC, abstractmethod

# Create an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

# Create concrete classes
class Car(Vehicle):
    def start(self):
        print("Starting the car")
        
    def stop(self):
        print("Stopping the car")
        
class Bike(Vehicle):
    def start(self):
        print("Starting the bike")
        
    def stop(self):
        print("Stopping the bike")
        
car = Car()
car.start()
car.stop()

bike = Bike()
bike.start()
bike.stop()



"""..........................................................................................."""







    
    
    
    
        
        
    
    
    







        
        
    



