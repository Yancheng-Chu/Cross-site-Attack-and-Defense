document.addEventListener("DOMContentLoaded", function() {

    var queryInput = document.getElementById('query');
        queryInput.addEventListener("focus", function(event) {
      event.target.value = '';
    });
    });