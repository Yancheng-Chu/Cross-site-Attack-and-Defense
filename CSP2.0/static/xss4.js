// const timer = '{{ timer }}';
//
// function startTimer(seconds) {
//             seconds = parseInt(seconds) || 3;
//             setTimeout(function () {
//                 window.confirm("Time is up!");
//                 window.history.back();
//             }, seconds * 1000);
//         }
//
//         document.addEventListener("DOMContentLoaded", function () {
//             var img = document.getElementById('loadingImage');
//             img.addEventListener('load',function(){
//                 startTimer(timer)
//             })
//         })

        // function executeScript(scriptText) {
        //     var scriptElement = document.createElement('script');
        //     scriptElement.textContent = scriptText;
        //     scriptElement.setAttribute('nonce','rrr')
        //     document.head.appendChild(scriptElement);
        // }
 function startTimer(seconds) {
            seconds = parseInt(seconds) || 3;
            setTimeout(function () {
                window.confirm("Time is up!");
                window.history.back();
            }, seconds * 1000);
        }
        document.addEventListener("DOMContentLoaded", function () {
            let img = document.getElementById('loadingImage')
            window.onload = function () {
                var timerValue = '{{ timer }}';

// 构造包含函数调用的字符串
                var codeToExecute = "startTimer('" + timerValue + "');";
                var dummyElement = document.createElement('div');

// 将编码字符串赋值给虚拟元素的 innerHTML 属性，这将解码 HTML 实体
                dummyElement.innerHTML = codeToExecute;

// 获取解码后的字符串
                var decodedString = dummyElement.textContent;
                console.log('222',decodedString)
// executeScript(decodedString);
                new Function(decodedString);

            }
        })


