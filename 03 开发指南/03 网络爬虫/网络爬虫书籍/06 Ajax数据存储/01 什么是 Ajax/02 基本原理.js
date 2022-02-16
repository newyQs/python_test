/*
https://cuiqingcai.com/5593.html

发送 Ajax 请求到网页更新的这个过程可以简单分为以下 3 步：
(1) 发送请求；
(2) 解析内容；
(3) 渲染网页;
 */
var xmlhttp;

if (window.XMLHttpRequest) {
    // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp=new XMLHttpRequest();
} else {
    // code for IE6, IE5
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
}
xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState==4 && xmlhttp.status==200) {
        document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
};
xmlhttp.open("POST","/ajax/",true);
xmlhttp.send();