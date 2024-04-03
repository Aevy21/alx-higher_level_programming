// Wait for the DOM content to be fully loaded
$(document).ready(function() {
    // Fetch movie titles from API
    $.ajax({
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        method: "GET",
        success: function(response) {
            // Loop through each movie and add title to the list
            response.results.forEach(function(movie) {
                $("#list_movies").append("<li>" + movie.title + "</li>");
            });
        },
        error: function(xhr, status, error) {
            console.error("Error fetching data:", error);
        }
    });
});
