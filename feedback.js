chrome.contextMenus.create({
  "id": "newfeedback",
  "title": "新增回饋 %s",
  "contexts": ["all"]
});

function getword(info) {
  chrome.tabs.executeScript(null, { file: "/static/javascripts/feedbModal.js" }, () => chrome.runtime.lastError);
  // 如果 Modal 不能用再用這個
  // chrome.windows.create({
  //   url: "https://lost.moli.rocks/getData",
  //   // url: "backend/templates/test.html",
  // });
}