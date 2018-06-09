
var xhr = new XMLHttpRequest();


//Open the connection:

xhr.open("GET", "https://swapi.co/api/planets/1/");
xhr.send();


xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById("data").innerHTML = this.responseText;
    }
};





