# Exception Handling in Python

## Overview

This Python script provides insights into handling exceptions, utilizing `try` and `except` blocks, raising exceptions, highlighting the differences between errors and exceptions, and exploring inbuilt exceptions.

## Exception Handling with `try` and `except`

In Python, the `try` and `except` blocks are used to handle exceptions gracefully. The `try` block contains the code that might raise an exception, and the `except` block specifies how to handle that exception.

### Example

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle the specific exception
    print(f"Error: {e}")
```

## Raising Exceptions

You can explicitly raise exceptions using the `raise` keyword. This is useful when a certain condition is met, and you want to notify the calling code about an issue.

### Example

```python
def example_function(x):
    if x < 0:
        raise ValueError("Input must be non-negative")
    return x * 2
```

## Differences Between Errors and Exceptions

- **Errors:** Generally unrecoverable issues at runtime.
- **Exceptions:** Events that disrupt the normal flow but can be handled in code.

## Inbuilt Exceptions

Python provides a range of inbuilt exceptions to handle different types of errors. Some common ones include:
- `ValueError`
- `TypeError`
- `ZeroDivisionError`

## Common Inbuilt Exceptions

~`ValueError`: Raised when a function receives an argument of the correct type but an inappropriate value.

~`TypeError`: Raised when an operation or function is applied to an object of an inappropriate type.

~`ZeroDivisionError`: Raised when division or modulo by zero is encountered.

~`FileNotFoundError`: Raised when a file or directory is requested but cannot be found.

~`IndexError`: Raised when a sequence subscript is out of range.

~`KeyError`: Raised when a dictionary key is not found.

~`AssertionError`: Raised when an assert statement fails.

For a comprehensive list, refer to the [official Python documentation](https://docs.python.org/3/library/exceptions.html).
https://www.dataquest.io/blog/python-exceptions/

