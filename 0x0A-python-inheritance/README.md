# Python Inheritance README

![visualization](https://images.app.goo.gl/uYBrV2eLXCxG1vDCA)

## Introduction
In Python, inheritance is a fundamental concept in object-oriented programming (OOP) that allows you to create a new class by reusing attributes and methods of an existing class. This README will guide you through key aspects of inheritance in Python.

### Parent Class (Superclass)
A parent class is the class whose features are inherited by another class. It serves as the template for the creation of subclasses.

### Inheriting from a Parent Class
To create a subclass, you use the syntax `class Child(Parent):`. This indicates that the child class inherits attributes and methods from the parent class.

```python
class Parent:
    # Parent class attributes and methods

class Child(Parent):
    # Child class attributes and methods
```

### Overriding Methods or Attributes
Inheritance allows you to override methods or attributes in the child class. This means providing a new implementation for a method or giving a different value to an attribute.

```python
class Child(Parent):
    def overridden_method(self):
        # New implementation for the method
        pass

    overridden_attribute = "New value"
```

### Purpose of Inheritance
1. **Code Reusability:** Inheritance promotes reusing code from existing classes, reducing redundancy and making the code more modular.
2. **Extensibility:** Subclasses can extend or specialize the behavior of the superclass by adding new features.

### Built-in Functions

#### `isinstance(object, classinfo)`
- Returns `True` if the object is an instance of the specified class or a subclass thereof.

#### `issubclass(class, classinfo)`
- Returns `True` if the class is a subclass of a class or a tuple of classes.

#### `type(object)`
- Returns the type of an object. Useful for checking the type of an instance.

#### `super()`
- Returns a temporary object of the superclass, allowing you to call its methods.

### Example
Consider a family analogy:

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, hobby):
        super().__init__(name)
        self.hobby = hobby
```


