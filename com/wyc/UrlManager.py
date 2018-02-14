#-*- coding: UTF-8 -*-
'''
Created on 2018��2��11��

@author: wyc
'''
class UrlManager(object):
    
    def __init__(self):
        self.newUrls = set()
        self.olgUrls = set()
    
    def hasNewUrl(self):
        return len(self.newUrls) != 0
    
    def getNewUrl(self):
        url = self.newUrls.pop()
        return url
    
    def addUrl(self,url):
        if url is None:
            return
        if url not in self.newUrls and url not in self.olgUrls:
            self.newUrls.add(url)
        
    def addUrls(self,urls):
        if urls is None or len(urls) == 0:
            return None
        for url in urls:
            self.addUrl(url)
            