
import urllib.request
import ssl
from urllib import request

class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None

        context = ssl._create_unverified_context()
        headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0)"}
        req = request.Request(url,headers=headers)
        print('begin downling %s' % url)
        response = request.urlopen(req,context=context)
        if (response.getcode()) != 200:
            return None
        
        #print('read out %s' % response.read())
        html_str = response.read().decode()
        return html_str

            