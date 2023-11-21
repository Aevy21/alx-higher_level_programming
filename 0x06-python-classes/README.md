# Python - Classes and Objects

## Object-Oriented Programming (OOP) Definition:
Object-Oriented Programming is a programming paradigm that utilizes object instances of classes for structuring and organizing code. It involves designing software using the concept of objects, which represent real-world entities, and classes, which serve as blueprints defining the structure and behavior of objects.

## Key Concepts:

### Class:
A class is a blueprint or template that defines the structure and behavior of objects. It encapsulates data and functions that operate on the data.

**Example:**
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
```

### Object:
Objects are instances of classes, representing real-world entities. They encapsulate data and behaviors defined by their class.

**Example:**
```python
my_car = Car("Toyota", "Camry")
```

### Instance:
An instance is an individual object created from a class, representing a unique entity with distinct data.

**Example:**
```python
another_car = Car("Honda", "Accord")
```

### Attribute:
An attribute is a characteristic or property of an object.

**Examples:**
```python
# Class attribute
class Dog:
    legs = 4

# Instance attribute
my_dog = Dog()
my_dog.name = "Buddy"
```

### Method:
A method is a function defined within a class, representing behavior associated with the class.

**Example:**
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2
```

### Public, Protected, and Private Attributes:
- **Public Attribute:** Accessible from anywhere, both within and outside the class.
  ```python
  class Example:
      public_attr = "I am public"
  ```

- **Protected Attribute (_):** Accessible within the class and its subclasses.
  ```python
  class Example:
      _protected_attr = "I am protected"
  ```

- **Private Attribute (__):** Name-mangled, limiting direct access from outside the class.
  ```python
  class Example:
      __private_attr = "I am private"
  ```

### String:
A string is a sequence of characters, commonly used to represent text.

**Example:**
```python
message = "Hello, Python!"
```

### Instance and Class Attributes (Continued):
- **Public Class Attribute:**
  ```python
  class Example:
      public_class_attr = "I am a public class attribute"
  ```

- **Private Instance Attribute:**
  ```python
  class Example:
      def __init__(self):
          self.__private_instance_attr = "I am a private instance attribute"
  ```

### Class:
A class is a fundamental concept in OOP, serving as a blueprint for creating objects.

**Example:**
```python
class Human:
    species = "Homo sapiens"
```

This guide provides a comprehensive overview of Python's class and object concepts in the context of Object-Oriented Programming. Use these principles to structure your code effectively and represent real-world entities in a modular and organized manner.
