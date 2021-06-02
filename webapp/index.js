let url = 'http://localhost:8080/'

fetch(url, { method: 'GET', mode: 'cors',})
  .then(response => {
    const reader = response.body.getReader();
    return reader.read();
  })
  .then(data => {
    var string = new TextDecoder().decode(data.value); //the string is sent as UTF-8 bytes so it needs to be decoded
    console.log(string);
    let lt = document.getElementById('low-temp');
    let ht = document.getElementById('high-temp');
    if (string.includes("module")) {
      alert("No bluetooth module detected");
      lt.innerHTML = "0.0";
      ht.innerHTML = "0.0";
    }
    else {
      string = string.slice(1,-1);
      var temps = string.split(",");
      lt.innerHTML = temps[0];
      ht.innerHTML = temps[1];
    }
  })
  .catch(err => {
      console.log(err);
      alert("Something went wrong! Confirm server status.");
  });