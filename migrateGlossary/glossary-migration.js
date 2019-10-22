//this script will strip the bb glossary table of its text.
//to do - push to HTML file with the ABC Nav
var texts = $("td").map(function() {
    return $(this).text();
});
$(document).ready(function() {
    $("a").remove();
});

console.log(texts);