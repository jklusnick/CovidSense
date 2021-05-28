let url = 'http://localhost:8080/'

fetch(url, { method: 'GET', mode: 'cors',})
  .then(response => {
    const reader = response.body.getReader();
    return reader.read();
  })
  .then(data => {
    var string = new TextDecoder().decode(data.value); //the string is sent as UTF-8 bytes so it needs to be decoded
    console.log(string)
    let p = document.getElementById('test');
    p.innerHTML = string;
  })
  .catch(err => {
      console.log('Something went wrong!');
      console.log(err);
  });