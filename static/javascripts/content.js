function translate(data) {
  console.log(123456787654323456789);
  console.log(data);
  
  
  let allKeys = Object.keys(data);
  let Search_Txt = document.body.innerText;
  allKeys.forEach(element => {
    let n = Search_Txt.search(element);
    if (n > -1) {
      $("body *").replaceText(new RegExp(element, "g"), `<span class="translated" title='網頁原文:${element} / 英文原文:${data[element]["en_US"]}'>${data[element]["zh_TW"]}</span>`);
    }
  });
}

function handle() {
  if(this.readyState == 4) {
    console.log(this.response);
    
    let data = JSON.parse(this.response);
    translate(data);
  }
}

function init() {
<<<<<<< HEAD
  // let xml = new XMLHttpRequest();
  // xml.open('GET', 'https://lost.moli.rocks/getData');
  // xml.send();
  // xml.onreadystatechange = handle;
  $.ajax({
    type: 'GET',
    contentType: 'application/json',
    url: 'http://127.0.0.1:5000/getData',
    dataType: 'json',
    data: { "texts": document.body.innerText },
    success: function (result) {
      console.log(result);
      translate(result);
    }, error: function (result) {
      console.log(result);
    }
  });
=======
  let xml = new XMLHttpRequest();
  xml.open('GET', 'http://127.0.0.1:5000/getData');
  xml.send();
  xml.onreadystatechange = handle;
>>>>>>> origin/b8
}
init();