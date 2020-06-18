chrome.contextMenus.create({
  "id": "newfeedback",
  "title": "新增回饋 %s",
  "contexts": ["all"],
  "onclick": getword
});

function getword(info) {
  // 如果 Modal 不能用再用這個
  chrome.windows.create({
    url: "https://lost.moli.rocks/feedBack",
    // url: "http://127.0.0.1:5000/feedBack",
  });
}