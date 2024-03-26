#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Check if the URL and file path are provided as arguments
if (process.argv.length < 4) {
  console.error('Usage: ./fetch_and_store.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, response.statusMessage);
    return;
  }

  // Write the response body to the specified file
  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error('Error writing file:', err);
    } else {
      console.log(`Successfully saved the response to ${filePath}`);
    }
  });
});
