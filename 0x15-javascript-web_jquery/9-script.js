// fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.
$(document).ready(function() {
    // Fetch translation from API
    $.ajax({
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
        method: "GET",
        success: function(response) {
            // Update the content of DIV#hello with the translated value
            $("#hello").text(response.hello);
        },
        error: function(xhr, status, error) {
            console.error("Error fetching data:", error);
        }
    });
});
