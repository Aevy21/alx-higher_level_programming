#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const apiURL = process.argv[2];
const filePath = process.argv[3];

request(apiURL, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(filePath, body);
  }
});
