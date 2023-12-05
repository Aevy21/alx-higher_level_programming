# Python I/O README

## File in Python

In Python, a file is a named location on disk or in memory used to store information. Files are used for various purposes, such as storing data, configuration settings, or code.

## File Object

A file object is an interface to an open file, allowing you to perform various operations on the file, such as reading, writing, and closing.

## Opening a File

To open a file, you can use the `open()` function. It takes a filename and a mode as parameters. Common modes include:

- `'r'`: Read (default)
- `'w'`: Write
- `'a'`: Append
- `'b'`: Binary mode
- `'t'`: Text mode (default)

Example:

```python
with open('example.txt', 'r') as file:
    # File is open for reading within this block
    content = file.read()
    # Operations on the file
# File is automatically closed after leaving the block
```

## Reading from a File

Python provides various methods to read from a file:

- `read()`: Reads the entire file content.
- `readline()`: Reads a single line from the file.
- `readlines()`: Reads all lines in the file and returns a list.

Example:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    # Process the content
```

## Writing to a File

To write to a file, you can use the `write()` method. Remember to open the file in write or append mode.

Example:

```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!")
    # Additional write operations
```

## Closing a File

The `with` statement automatically closes the file when leaving its block. However, you can also close a file explicitly using the `close()` method.

Example:

```python
file = open('example.txt', 'r')
content = file.read()
file.close()  # Explicitly close the file
```

## Cleanup Tactics

Cleanup actions are automatically handled by the `with` statement. The file is properly closed, and resources are released. This ensures good resource management and helps avoid potential issues.

Example:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    # Operations on the file
# File is automatically closed, ensuring cleanup
```
## Table summary
Certainly! Below are the two separated tables with short descriptions above each:

### File Modes

| Mode | Function |
|------|----------|
| `r`  | Open a file for reading. This is the default mode. |
| `w`  | Open a file for writing. If the file already exists, overwrite its contents. Create a new file if the file does not exist. |
| `a`  | Open a file for appending. Preserve the file’s contents, add new data to the end of the file. |
| `r+` | Open a file for reading and writing. |
| `w+` | Allows writing as well as reading from the file. |
| `a+` | Allows appending as well as reading from the file. |

**Description:**  
File modes determine how a file should be opened and what operations are allowed on the file. Each mode serves a different purpose, such as reading, writing, appending, or a combination of reading and writing.

### File Methods

| Method      | Description |
|-------------|-------------|
| `close()`   | Closes the file. |
| `flush()`   | Flushes the internal buffer. |
| `fileno()`  | Returns the file descriptor of the file. |
| `next()`    | Returns the next line from the file. |
| `read(size)`| Reads `size` number of bytes from the file. Reads the entire file if you don’t pass any argument value. |
| `readline(size)` | Reads one line from a file. |
| `readlines()`| Reads the entire file and returns a list of the lines. |
| `seek(offset, whence)` | Lets us control the position of the file pointer. |
| `tell()`    | Returns the current position of the file pointer. |
| `truncate(size)` | It truncates the file to the specified size. |
| `writable()` | Returns `True` if we can write into the file. |
| `write(string)` | Writes `string` into the file. |

**Description:**  
File methods provide various operations to interact with a file, including reading, writing, and managing the file pointer. These methods help perform specific tasks such as closing the file, flushing the buffer, and controlling the file pointer's position.


The information about file modes and methods is adapted from the official Python documentation. You can find more details in the [Python Documentation on File Objects](https://techvidvan.com/tutorials/python-file-read-write/)

This README provides a basic overview of Python I/O operations. .
