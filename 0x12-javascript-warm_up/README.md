# JavaScript Basics

## Introduction
JavaScript is a versatile programming language commonly used for web development. It allows developers to add interactivity and dynamic behavior to web pages. This README provides an overview of the fundamental concepts in JavaScript.

## Table of Contents
- [Variables](#variables)
- [Data Types](#data-types)
- [Functions](#functions)
- [Conditional Statements](#conditional-statements)
- [Loops](#loops)

## Variables
Variables are used to store data values. In JavaScript, variables can be declared using the `let` or `const` keywords.

Example:
```javascript
let x = 10;
const PI = 3.14;
```

## Data Types
JavaScript supports several data types, including:
- **Primitive Data Types**:
  - Number: Represents both integer and floating-point numbers.
  - String: Represents a sequence of characters.
  - Boolean: Represents true or false.
  - Undefined: Represents a variable that has been declared but not assigned a value.
  - Null: Represents an intentional absence of any object value.
  - Symbol (ES6): Represents a unique identifier.

Example:
```javascript
let name = 'John';
let age = 30;
let isAdult = true;
let fruits = ['apple', 'banana', 'orange'];
```

## Functions
Functions are blocks of reusable code that perform a specific task. They can accept parameters and return values.

Example:
```javascript
function greet(name) {
    return 'Hello, ' + name + '!';
}

console.log(greet('Alice')); // Output: Hello, Alice!
```

## Conditional Statements
Conditional statements allow you to execute different code blocks based on specified conditions. They include `if`, `else if`, and `else`.

Example:
```javascript
let num = 10;

if (num > 0) {
    console.log('Positive number');
} else if (num < 0) {
    console.log('Negative number');
} else {
    console.log('Zero');
}
```

## Loops
Loops are used to repeatedly execute a block of code as long as a specified condition is true. Common types of loops in JavaScript include `for`, `while`, and `do...while`.

Example:
```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

This README provides a brief overview of Javascripy
