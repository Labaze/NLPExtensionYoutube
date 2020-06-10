var url;
chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function
(tabs) {
    url = tabs[0].url;
    // document.getElement
    // ById("host").innerHTML = url;
    // document.getElementById("host2").value = url;
});
window.onload= function (){
        const submit = document.getElementById("summarize");
        submit.addEventListener("click", (event) => {
        alert("Resume: "+url);
        var newxmlhttp = new XMLHttpRequest();
        var theUrl = "http://127.0.0.1:8000/results";
        newxmlhttp.open("POST", theUrl, true);
        newxmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=UTF-8");
        newxmlhttp.send("url="+url);
        newxmlhttp.onreadystatechange = function() {
            if (newxmlhttp.readyState == 4){
            //alert(decodeURIComponent(JSON.parse(newxmlhttp.responseText)));
            alert(newxmlhttp.responseText);
            }
        };
    });
};
