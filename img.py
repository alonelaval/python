# -*- encoding: utf-8 -*-
'''
Created on 2015年7月26日

@author: huawei
'''
from bs4 import BeautifulSoup
import os
import traceback
import urllib
import urllib2
HEADERS = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:27.0) Gecko/20100101 Firefox/27.0"}
TIMEOUT = 60
DOMAIN = "http://www.zcool.com.cn"
PATH = "./images"
class MyClass(object):
    '''
    classdocs
    '''
  
   
    def __init__(self):
        '''
        Constructor
        '''
        
    def getHtml(self,url):
        return self._do_get(url, None);
    
    
    def getPageItems(self,html):
        soup = BeautifulSoup(html)
        pages=set()
        max = 0
        prefix = None
        for tag in soup.find_all("div", class_="bigPage pt30 pb20 vm center"):
            for a in tag.findAll('a',href=True):
                href = a['href']
                if a.text == '' or a.text == ' ':
                    continue
                page = int(a.text)
                if max == 0:
                    prefix =href[0:href.rfind('/')+1]
                if max < page:
                    max = page
                
        for i in range(1,max):
            url = "%s%s%d%s" % (DOMAIN,prefix,i,".html")
            pages.add(url)
        return pages
    
    def getImgs(self,html):
        soup = BeautifulSoup(html)
        imgs =set()
        for tag in soup.find_all("div",class_="workContent center"):
            for a in tag.findAll("a",href=True):
                imgs.add(a['href'].replace("/img.html#src=",""))
        return imgs  
    
    def saveImgs(self,imgs):
        for img in imgs:
            name =img[img.rfind("/"):len(img)] 
            img_local = PATH+name
            if os.path.isfile(img_local):
                continue 
            f = open(img_local,"wb")
            print img
            f.write(self._do_get(img, HEADERS))
            f.flush()
            f.close()
            
    def save_imgs_by_url(self,urls):
        for url in urls:
            for page in my.getPageItems(my.getHtml(url)):
                self.saveImgs(self.getImgs(self.getHtml(page)))
            
    def _do_get(self, url, headers=None):
        '''
        execute http get method
        '''
        response = None
        try:
            request = urllib2.Request(url, headers=headers if headers else HEADERS)
            response = urllib2.urlopen(request, timeout=TIMEOUT)
            return response.read()
        finally:
            if response:
                response.close()
    def getAllImg(self,urls):
        try:
            self.save_imgs_by_url(urls)
        except BaseException:
            traceback.print_exc()
            self.getAllImg(urls) 
 
URLS  = [
        "http://www.zcool.com.cn/show/ZOTM5ODQ=/1.html",
         "http://www.zcool.com.cn/show/ZOTMxOTI=.html",
         "http://www.zcool.com.cn/show/ZOTM5ODg=.html",
         "http://www.zcool.com.cn/show/ZMTEyODQ0.html",
         "http://www.zcool.com.cn/show/ZMTYxNTIw.html"
         ]           

            
            
if __name__=='__main__':
    my = MyClass()
    my.getAllImg(URLS)
# #     for i in my.getPageItems(my.getHtml("http://www.zcool.com.cn/show/ZMTYxNTIw.html")):
# #         print i
#     my.save_imgs_by_url(URLS)
# #     data = my._do_get("http://www.zcool.com.cn/img.html#src=http://img.zcool.cn/community/05f655554a7ba900000115a883388c.jpg", HEADERS)、
#     
#     f = open(PATH+"/111.jpg","wb")
#     f.write(urllib2.urlopen("http://img.zcool.cn/community/0577e3554a7ba600000115a8a33bc3.jpg").read())
#     f.flush()
#     f.close()
            




# http://img.zcool.cn/community/05fb2e554a7ba800000115a836d0c0.jpg
# http://img.zcool.cn/community/05113d554a7ba800000115a89d5ba6.jpg
# http://img.zcool.cn/community/05df52554a7ba800000115a82b316c.jpg
# http://img.zcool.cn/community/051693554a7bb400000115a8508398.jpg
# http://img.zcool.cn/community/052344554a7ba900000115a870965d.jpg
# http://img.zcool.cn/community/050974554a7ba800000115a83e7260.jpg
# http://img.zcool.cn/community/0577e3554a7ba600000115a8a33bc3.jpg
# http://img.zcool.cn/community/0501e6554a7ba600000115a8542417.jpg
# http://img.zcool.cn/community/0506ec554a7ba600000115a89fd217.jpg
# http://img.zcool.cn/community/05e23a554a7ba600000115a8346012.jpg









