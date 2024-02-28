var time = {{timer}};
let c = 'startTimer(' + time + ')';
console.log(c)
        document.addEventListener("DOMContentLoaded", function () {
            var img = document.getElementById('loadingImage');
            function startTimer(seconds) {
            seconds = parseInt(seconds) || 3;
            setTimeout(function () {
                window.confirm("Time is up!");
                // window.history.back();
            }, seconds * 1000);
        }
            img.onload = function(){
                startTimer('{{timer}}')
            }

            console.log()
        })