$(document).ready(function() {
    // Handle click event on DIV#red_header
    $("#red_header").click(function() {
        // Select the header element and update text color to red (#FF0000)
        $("header").css("color", "#FF0000");
    });
});
