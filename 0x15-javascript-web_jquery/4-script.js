// Wait for the DOM content to be fully loaded
$(document).ready(function() {
    // Handle click event on DIV#toggle_header
    $("#toggle_header").click(function() {
        // Toggle classes on header element
        $("header").toggleClass("red green");
    });
});
