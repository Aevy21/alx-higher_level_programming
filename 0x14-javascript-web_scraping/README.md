# 0x14. JavaScript - Web scraping

## Web Scraping
Web scraping involves extracting data from websites. In JavaScript, you can perform web scraping using libraries like Cheerio.js or by directly manipulating the DOM (Document Object Model) using vanilla JavaScript. 

1. **Cheerio.js**: Cheerio is a fast, flexible, and lean implementation of core jQuery specifically designed for server-side scraping in Node.js. It provides jQuery-like syntax for selecting and manipulating DOM elements on the server.

2. **DOM Manipulation**: Using vanilla JavaScript, you can interact with the DOM of a web page by accessing elements, attributes, and content. Techniques include using `document.querySelector`, `document.querySelectorAll`, and DOM traversal methods like `getElementById`, `getElementsByClassName`, etc.

## Data Manipulation
Data manipulation involves processing and transforming data in various ways using JavaScript methods.

1. **Array Methods**: JavaScript array methods like `map`, `filter`, `reduce`, `forEach`, `find`, etc., are used to iterate over arrays, perform operations, filter elements, transform data, and more.

2. **Object Manipulation**: Objects in JavaScript can be manipulated by adding or removing properties, accessing values using keys, iterating over object properties using loops or methods like `Object.keys`, `Object.values`, and `Object.entries`.

## JSON Handling
JSON (JavaScript Object Notation) is a lightweight data interchange format used for data serialization and transmission.

1. **JSON Data Types**: JSON supports data types such as strings, numbers, booleans, arrays, objects, null, and nested structures.

2. **JSON Syntax and Rules**: JSON data is represented in key-value pairs enclosed in curly braces `{}` for objects and square brackets `[]` for arrays. Keys and string values should be enclosed in double quotes.

3. **Converting Data**: Use `JSON.parse()` to convert JSON data to JavaScript objects and `JSON.stringify()` to convert JavaScript objects to JSON format.

## File Operations
JavaScript can perform file operations both in server-side (Node.js) and client-side (browser) environments.

1. **Node.js File System (`fs` Module)**: In Node.js, you can use `fs` module methods like `fs.readFile`, `fs.writeFile`, `fs.appendFile`, etc., to read, write, and append to files on the server.

2. **Browser File APIs**: In the browser, use APIs like FileReader API for reading files asynchronously, Blob API for creating file-like objects, and Fetch API for making HTTP requests to fetch files.

## HTTP Methods
HTTP methods are used for communication between clients and servers in web development, commonly known as CRUD operations (Create, Read, Update, Delete).

1. **GET**: Used to retrieve data from a server.
2. **POST**: Used to send data to a server to create/update a resource.
3. **PUT**: Used to update a resource on the server.
4. **DELETE**: Used to delete a resource on the server.

Here are examples demonstrating how to make requests using these HTTP methods using the `fetch` API:

#### GET Request:
```javascript
// Making a GET request
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => response.json())
  .then(data => console.log('GET Response:', data))
  .catch(error => console.error('Error:', error));
```
This example fetches a post with ID 1 from JSONPlaceholder API.

#### POST Request:
```javascript
// Making a POST request
fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  body: JSON.stringify({ title: 'New Post', body: 'This is a new post.', userId: 1 }),
  headers: { 'Content-Type': 'application/json' },
})
  .then(response => response.json())
  .then(data => console.log('POST Response:', data))
  .catch(error => console.error('Error:', error));
```
This example sends a new post to JSONPlaceholder API.

#### PUT Request:
```javascript
// Making a PUT request
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'PUT',
  body: JSON.stringify({ id: 1, title: 'Updated Post', body: 'This post has been updated.', userId: 1 }),
  headers: { 'Content-Type': 'application/json' },
})
  .then(response => response.json())
  .then(data => console.log('PUT Response:', data))
  .catch(error => console.error('Error:', error));
```
This example updates the post with ID 1 on JSONPlaceholder API.

#### DELETE Request:
```javascript
// Making a DELETE request
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'DELETE',
})
  .then(response => {
    if (response.ok) {
      console.log('DELETE Request successful');
    } else {
      console.error('DELETE Request failed');
    }
  })
  .catch(error => console.error('Error:', error));
```
This example deletes the post with ID 1 from JSONPlaceholder API.

