#!/usr/bin/node

const request = require('request');

// Check if the URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: ./get_status_code.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

// Perform a GET request and display the status code
request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  console.log(`code: ${response.statusCode}`);
});
