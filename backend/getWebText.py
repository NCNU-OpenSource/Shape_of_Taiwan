import urllib
from urllib import request
from hanziconv import HanziConv
from pattern.web import plaintext

def getWebText(url) :
    # url = 'https://www.kutu66.com/GitHub/article_97923'
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = request.Request(url, headers=headers) 
    return HanziConv.toTraditional(plaintext(request.urlopen(req).read().decode()))