#!/usr/bin/node

const fs = require('fs');

// Check if the file path is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: ./read_file.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read file asynchronously with utf-8 encoding
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error); // Print the error object if an error occurred
  } else {
      console.log(data); // Print the file content
    }
  }
});
