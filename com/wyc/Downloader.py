#-*- coding: UTF-8 -*-
'''
Created on 2018��2��11��

@author: wyc
'''
import urllib2
class Downloader(object):
    
    def download(self,url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()