// timer.js
function startTimer(seconds) {
    seconds = parseInt(seconds) || 3;
    setTimeout(function () {
        window.confirm("Time is up!");
        window.history.back();
    }, seconds * 1000);
}

document.addEventListener("DOMContentLoaded", function () {
    window.onload = function () {
        var dum = document.createElement('div');
                dum.innerHTML = '{{timer}}';
                var decodedString = dum.textContent;
              startTimer(decodedString)
    }
})