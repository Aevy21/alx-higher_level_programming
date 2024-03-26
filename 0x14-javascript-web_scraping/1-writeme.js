#!/usr/bin/node

const fs = require('fs');

// Check if the file path and string to write are provided as arguments
if (process.argv.length < 4) {
  console.error('Usage: ./write_file.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write string to file asynchronously with utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err); // Print the error object if an error occurred while writing
  }
});
