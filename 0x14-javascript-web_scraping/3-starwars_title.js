#!/usr/bin/node

const request = require('request');

// Check if the movie ID is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: ./get_star_wars_movie_title.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, response.statusMessage);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    console.log(`${movieData.title}`);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
