#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: ./compute_completed_tasks.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Make a GET request to the API URL
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
    const todosData = JSON.parse(body);
    const completedTasksByUser = {};

    // Iterate through the todos and count completed tasks for each user
    todosData.forEach(todo => {
      if (todo.completed) {
        if (!completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId] = 1;
        } else {
          completedTasksByUser[todo.userId]++;
        }
      }
    });

    console.log(completedTasksByUser);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
