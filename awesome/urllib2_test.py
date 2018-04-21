import urllib.request
from bs4 import BeautifulSoup


def urldownload():
    url = "http://www.baidu.com"
    response1 = urllib.request.urlopen(url)
    print (response1.getcode())
    print(response1.read())

    request = urllib.request.Request(url)
    request.add_header('user-agent','Mozilla/5.0')
    reponse2 = urllib.request.urlopen(request)
    print (reponse2.getcode())
    print(reponse2.read())

    

def beautifultest():
    html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
    soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

    links = soup.find_all('a')
    for link in links:
        print(link.name,link['href'],link.get_text())


if __name__=='__main__':
    # urldownload()
    beautifultest()
    
    
    
