// Wait for the DOM content to be fully loaded
$(document).ready(function() {
    // Handle click event on DIV#update_header
    $("#update_header").click(function() {
        // Update text of header element
        $("header").text("New Header!!!");
    });
});
