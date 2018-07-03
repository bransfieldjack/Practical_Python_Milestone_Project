
var xhr = new XMLHttpRequest();


//Open the connection:

xhr.open("GET", "https://www.google.com/url?q=https://jsonplaceholder.typicode.com/posts&sa=D&source=hangouts&ust=1528621279035000&usg=AFQjCNH8azmuBN3z-RLooYNpcOV3OhOLvA");
xhr.send();


xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById("data").innerHTML = this.responseText;
    }
};





