#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: ./count_wedge_antilles_movies.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = '18';

// Make a GET request to the Star Wars API films endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const filmsData = JSON.parse(body).results;
    const wedgeAntillesMovies = filmsData.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
  }
    {
    console.log(`${wedgeAntillesMovies.length}`);
  }
}
});
