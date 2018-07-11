var xhr = new XMLHttpRequest();

xhr.open("GET", "https://swapi.co/api/");
xhr.send();

xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200){
        console.log(typeof(JSON.parse(this.responseText)));
    }
    
};







 var xhr = new XMLHttpRequest;
               
                  xhr.open('GET', '/files/users.txt', true);
                  xhr.onload = function (){
                      document.write( xhr.responseText );
                  };
                  xhr.send(null);