# Python Data Structures README

This Python project is a reference guide for working with common data structures in Python, specifically focusing on lists, strings, and tuples.

## Lists

### What are Lists?

Lists are ordered, mutable collections that can store elements of various data types. In Python, you create a list by enclosing elements in square brackets and separating them with commas.

### Differences and Similarities Between Strings and Lists

- Strings are immutable sequences of characters, while lists can contain diverse data types.
- Both strings and lists are ordered.
- Lists can be modified, while strings cannot be changed once created.

### Common List Methods

- `append(item)`: Adds an item to the end of the list.
- `insert(index, item)`: Inserts an item at a specific index.
- `pop(index)`: Removes and returns the item at the specified index.
- `remove(item)`: Removes the first occurrence of the specified item.
- `len(list)`: Returns the number of items in the list.
- `sort()`: Sorts the list in ascending order.
- `reverse()`: Reverses the order of elements in the list.

### Using Lists as Stacks and Queues

- To use a list as a stack, use `append()` to add elements to the end and `pop()` to remove elements from the end (Last-In-First-Out).
- To use a list as a queue, use `append()` to enqueue elements and `pop(0)` to dequeue elements (First-In-First-Out).

### List Comprehensions

List comprehensions provide a concise way to create lists by applying an expression to each item in an existing iterable.

## Tuples

### What are Tuples?

Tuples are ordered, immutable collections that can store elements of various data types. In Python, you create a tuple by enclosing elements in parentheses or separating them with commas.

### When to Use Tuples Versus Lists

Tuples are suitable for storing collections of values that should not be modified, while lists are used when you need to add, remove, or change elements.

### Tuple Packing and Sequence Unpacking

- Tuple packing is creating a tuple by enclosing multiple values within parentheses.
- Sequence unpacking is extracting individual elements from a sequence like a tuple or a list.

## `del` Statement

The `del` statement is used to remove elements from a list or to delete variables or objects. For example:
- `del my_list[2]` removes an item from a list.
- `del my_variable` deletes a variable from memory.
Certainly, here's an updated section in the README that explains how to implement a stack with two simple operations: push and pop.

```markdown
## Using Lists as Stacks

### Implementing a Stack

A stack is a data structure that follows the Last-In-First-Out (LIFO) principle, making it suitable for tasks like tracking function calls or maintaining a history. You can implement a stack using Python lists with two primary operations: `push` and `pop`.

#### Push Operation

The `push` operation adds an item to the top of the stack. In Python, you can use the `append()` method to perform this operation. Here's an example:

```python
my_stack = []  # Create an empty list as the stack
my_stack.append(1)  # Push 1 onto the stack
my_stack.append(2)  # Push 2 onto the stack
```

Now, `my_stack` contains `[1, 2]`, with `2` at the top.

#### Pop Operation

The `pop` operation removes and returns the top item from the stack. In Python, you can use the `pop()` method without an argument to pop the last item. Here's an example:

```python
popped_item = my_stack.pop()  # Pop the top item (2) and store it in popped_item
```

After this operation, `my_stack` contains `[1]`, and `popped_item` contains `2`.

By using the `append()` and `pop()` methods, you can effectively implement a stack using Python lists. Remember that these operations follow the LIFO principle, which means the last item added is the first one to be removed.
`

To implement a queue in Python with two simple operations (enqueue and dequeue), you can use a list. Here's a section to add to your README explaining how to implement a queue:

```markdown
## Using Lists as Queues

### Implementing a Queue

A queue is a data structure that follows the First-In-First-Out (FIFO) principle, making it suitable for tasks like managing tasks in a job queue or handling requests. You can implement a queue using Python lists with two primary operations: `enqueue` and `dequeue`.

#### Enqueue Operation

The `enqueue` operation adds an item to the rear of the queue. In Python, you can use the `append()` method to perform this operation. Here's an example:

```python
my_queue = []  # Create an empty list as the queue
my_queue.append(1)  # Enqueue 1 at the rear of the queue
my_queue.append(2)  # Enqueue 2 at the rear of the queue
```

Now, `my_queue` contains `[1, 2]`, with `1` at the front (the first item to be dequeued) and `2` at the rear.

#### Dequeue Operation

The `dequeue` operation removes and returns the front item from the queue. In Python, you can use the `pop(0)` method to perform this operation. Here's an example:

```python
dequeued_item = my_queue.pop(0)  # Dequeue the front item (1) and store it in dequeued_item
```

After this operation, `my_queue` contains `[2]`, and `dequeued_item` contains `1`.

By using the `append()` method to enqueue items and the `pop(0)` method to dequeue items, you can effectively implement a queue using Python lists. Remember that these operations follow the FIFO principle, which means the first item added is the first one to be removed.
```

This section provides a clear explanation of how to implement a queue using Python lists and describes the `enqueue` and `dequeue` operations with examples.

Feel free to explore the code examples and explanations in this project to gain a better understanding of working with these data structures in Python

