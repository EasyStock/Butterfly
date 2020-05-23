# coding=utf-8
'''
@Date: 2020-05-03 20:36:42
@LastEditTime: 2020-05-09 17:00:57
@Author: yuchonghuang@sina.cn
'''

'''
Created on May 6, 2019

@author: mac
'''

import os
import multiprocessing as mp
import time
import pandas as pd

def _ReadAllXLSXData(fileName):
    stockID = fileName[fileName.rfind('/')+1:fileName.find('.')]
    df = pd.read_excel(fileName, index_col=None, encoding='utf_8_sig')
    print('Read file:', fileName, 'Done!')
    return {stockID: df}

def listAllFilesInFolder(folder):
    allfile=[]
    for dirpath,_,filenames in os.walk(folder):
        for name in filenames:
            allfile.append(os.path.join(dirpath, name))
    return allfile

def filterSinceDate(fileList, SinceDate):
    res = []
    for fullpath in fileList:
        date = fullpath[fullpath.rfind('/')+1:fullpath.rfind('.')]
        if date < SinceDate:
            continue
        res.append(fullpath)

    return res

def filterLastN(fileList, lastN):
    fileList = sorted(fileList,reverse = False)
    size = len(fileList)
    if size <= lastN:
        return fileList
    else:
        return fileList[-lastN:]

    
def ToReadAllXLSXData(folder,since = None,lastN = None):
    dataFrames = []
    begin_time = time.time()
    pool = mp.Pool(mp.cpu_count()*2)
    fileList = listAllFilesInFolder(folder)
    if since != None:
        fileList = filterSinceDate(fileList, since)
    elif lastN != None:
        fileList  = filterLastN(fileList , lastN)
    else:
        pass
    
    for fullpath in fileList:
        if fullpath.find('.xlsx') == -1:
            continue
        print(fullpath)
        dataFrames.append(pool.apply_async(
            _ReadAllXLSXData, (fullpath, )))
    pool.close()
    pool.join()
    endTime = time.time()
    print('ToReadAllXLSXData cost:%s, total: %d' % ((endTime - begin_time), len(dataFrames)))
    ret = {}
    for item in dataFrames:
        ret.update(item.get())
    endTime1 = time.time()
    print('ToReadAllXLSXData to dict:%s' % (endTime1 - endTime))
    return ret
