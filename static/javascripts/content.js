function translate(data) {
  let allKeys = Object.keys(data);
  let Search_Txt = document.body.textContent;
  allKeys.forEach(element => {
    let n = Search_Txt.search(element);
    if (n > -1) {
      $("body *").replaceText(new RegExp(element, "g"), `<span class="translated" title='網頁原文:${element} / 英文原文:${data[element]["zh_US"]}'>${data[element]["zh_TW"]}</span>`);
    }
  });
}

function handle() {
  console.log()
  if(this.readyState == 4) {
    let data = JSON.parse(this.response);
    translate(data);
  }
}

function init() {
  let xml = new XMLHttpRequest();
  xml.open('GET', 'https://lost.moli.rocks/getData');
  xml.send();
  xml.onreadystatechange = handle;
}
init();