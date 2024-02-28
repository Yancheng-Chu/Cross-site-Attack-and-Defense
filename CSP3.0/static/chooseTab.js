// document.addEventListener('DOMContentLoaded', function () {
    function chooseTab(num) {
        // Dynamically load the appropriate image.
        var html = "Image " + parseInt(num) + "<br>";
        html += "<img src='/static/cloud" + num + ".jpg' />";
        $('#tabContent').html(html);

        window.location.hash = num;

        // Select the current tab
        var tabs = document.querySelectorAll('.tab');
        for (var i = 0; i < tabs.length; i++) {
            if (tabs[i].id === "tab" + parseInt(num)) {
                tabs[i].className = "tab active";
            } else {
                tabs[i].className = "tab";
            }
        }

        // Tell parent we've changed the tab
        top.postMessage(self.location.toString(), "*");
    }


    window.onload = function () {
        var tabs = document.querySelectorAll('.tab');

    // 为每个 tab 元素添加点击事件监听器
    tabs.forEach(function (tab) {
        tab.addEventListener('click', function (event) {
            var tabId = event.target.id; // 获取被点击元素的 ID
            var num = tabId.replace('tab', ''); // 提取 ID 中的数字部分
            chooseTab(num); // 调用 chooseTab 函数并传递相应的数字
        });
    });

        chooseTab(unescape(self.location.hash.substr(1)) || "1");
    };

    // Extra code so that we can communicate with the parent page
    window.addEventListener("message", function (event) {
        if (event.source === parent) {
            chooseTab(unescape(self.location.hash.substr(1)));
        }
    }, false);

// });



