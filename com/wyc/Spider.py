#-*- coding: UTF-8 -*-
'''
Created on 2018��2��11��

@author: wyc
'''
from UrlManager import UrlManager
from Downloader import Downloader
from HtmlPraser import HtmlPraser
from Output import Output


class Spider(object):
    def __init__(self):
        print 'init'
        self.urlManager = UrlManager()
        self.downloader = Downloader()
        self.praser = HtmlPraser()
        self.outputer = Output()
        
    def craw(self,rootUrl):
        self.urlManager.addUrl(rootUrl)
        count = 1
            
        while self.urlManager.hasNewUrl():
                newUrl = self.urlManager.getNewUrl()
                print '爬取第',count,'个url,url是：',newUrl
                htmlContent = self.downloader.download(newUrl)
                newUrls,newData = self.praser.praser(newUrl, htmlContent)
                self.urlManager.addUrls(newUrls)
                self.outputer.collect(newData)
                
                if count == 10:
                    break    
                
                count = count + 1   
            
        self.outputer.output()


if __name__ == '__main__':
    rootUrl = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    spider = Spider()
    spider.craw(rootUrl)