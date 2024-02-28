        document.addEventListener("DOMContentLoaded", function () {
                var link = document.getElementById('link');
                link.addEventListener('click', function (event) {
                window.location.href = link.getAttribute('href');
            });
        })