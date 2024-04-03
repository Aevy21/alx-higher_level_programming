// Wait for the DOM content to be fully loaded
$(document).ready(function() {
    // Handle click event on DIV#add_item
    $("#add_item").click(function() {
        // Create new <li> element
        var newItem = $("<li>").text("Item");

        // Append new <li> element to UL.my_list
        $("ul.my_list").append(newItem);
    });
});
