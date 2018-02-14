#-*- coding: UTF-8 -*-
'''
Created on 2018��2��11��

@author: wyc
'''
from bs4 import BeautifulSoup
import re
import urlparse
class HtmlPraser(object):
    

    def getNewUrls(self, pageUrl,soup):
        newUrls = set()
        links = soup.find_all('a',href = re.compile(r"/item/"))
        if links is None or len(links) == 0:
            return
        for link in links:
            newUrl = link['href']
            newFullUrl = urlparse.urljoin(pageUrl, newUrl)
            newUrls.add(newFullUrl)
            
        return newUrls
    
    def getNewData(self, pageUrl,soup):
        resData = {}
        
        resData['url'] = pageUrl
        
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        titleNode = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        resData['title'] = titleNode.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summaryNode = soup.find('div',class_='lemma-summary')
        if summaryNode is None:
            return
        resData['summary'] = summaryNode.get_text()
    
        return resData
    
    def praser(self,pageUrl,htmlContent):
        if pageUrl is None or htmlContent is None:
            return
        soup = BeautifulSoup(htmlContent,'html.parser',from_encoding = 'utf-8')
        
        newUrls = self.getNewUrls(pageUrl,soup)
        newData = self.getNewData(pageUrl,soup)
        
        return newUrls,newData
    