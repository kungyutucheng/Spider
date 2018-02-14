#-*- coding: UTF-8 -*-
'''
Created on 2018��2��11��

@author: wyc
'''
class Output(object):
    def __init__(self):
        self.datas = []
        
    def collect(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    def output(self):
        fout = open('out.txt','w')
        
        for data in self.datas:
            fout.write(data['url'].encode('utf-8'))
            fout.write('\n')
            fout.write(data['title'].encode('utf-8'))
            fout.write('\n')
            fout.write(data['summary'].encode('utf-8'))
            fout.write('\n')
            
        fout.flush()
        fout.close()