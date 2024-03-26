#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Check if both URL and file path arguments are provided
if (process.argv.length < 4) {
  console.error('Usage: ./fetch_and_store.js <url> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get({ url, encoding: 'utf-8' }, (error, response, body) => {
  if (error) {
    console.error('Error fetching the webpage:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Status Code ${response.statusCode}`);
    return;
  }

  // Write the response body to the specified file path
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
      return;
    }
    console.log(`Webpage content saved to ${filePath}`);
  });
});
