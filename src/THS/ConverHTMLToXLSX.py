# coding=utf-8
'''
@Date: 2020-05-03 16:24:24
@LastEditTime: 2020-05-03 21:42:53
@Author: yuchonghuang@sina.cn
'''

'''
Created on May 6, 2019

@author: mac
'''

import os
from StockDataItemIO import StockItemIO
import multiprocessing as mp
import time

def _converHTMLToXLSX(srcFileName, outFullName):
    print(srcFileName,'Begin!')
    if os.path.exists(outFullName) == True:
        print(srcFileName,'already exist!')
        return

    io = StockItemIO.CStockItemIO()
    io.readFrom(srcFileName)
    io.saveTo(outFullName)
    print(srcFileName,'Done!')

def GetFolderNameByDate(date):
    year,month,_ = date.split('-')
    Quarter = (int(month)-1)//3+1
    return '%s/Q%s'%(year,Quarter)
    
def ToConverHTMLToXlSX(fileList, destFolder):
    begin_time = time.time()
    pool = mp.Pool(mp.cpu_count()*2)
    if os.path.exists(destFolder) == False:
        os.makedirs(destFolder)
        
    for htmlFile in fileList:
        if htmlFile.find('.xls') == -1:
            continue
        date = htmlFile[htmlFile.rfind('/')+1:htmlFile.rfind('.')]
        destFolder2 = '%s/%s'%(destFolder, GetFolderNameByDate(date))
        if os.path.exists(destFolder2) == False:
            os.makedirs(destFolder2)
        outFullName = u'%s/%s.xlsx' %(destFolder2,date)
        if os.path.exists(outFullName):
            continue
        pool.apply_async(_converHTMLToXLSX, (htmlFile, outFullName))

    pool.close() 
    pool.join()
    endTime = time.time()
    print('ConverHTMLToXlSX:%s'%(endTime - begin_time))
