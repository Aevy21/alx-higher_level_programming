// Wait for the DOM content to be fully loaded
$(document).ready(function() {
    // Fetch character name from API
    $.ajax({
        url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
        method: "GET",
        success: function(response) {
            // Update the content of DIV#character with the character name
            $("#character").text(response.name);
        },
        error: function(xhr, status, error) {
            console.error("Error fetching data:", error);
        }
    });
});
