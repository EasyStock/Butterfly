# coding=utf-8
'''
@Date: 2020-06-06 09:58:53
@LastEditTime: 2020-06-07 20:01:40
@Author: yuchonghuang@sina.cn
'''
import os
import pandas as pd
from AdvanceFilter_BOLLOpen import CAdvanceFilter_BOLLOpen

def TestAllFile():
    folder = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/合并/最近合并'
    files = os.listdir(folder)
    result = []
    for fileName in files:
        if fileName.find('.xlsx') == -1:
            continue
        fullPath = os.path.join(folder, fileName)
        stockID = fileName[fileName.find('/')+1: fileName.find('.xlsx')]
        dataFrame = pd.read_excel(fullPath, index_col=None, encoding='utf_8_sig')
        filter12 = CAdvanceFilter_BOLLOpen(stockID,dataFrame)
        res = filter12.Filter(stockID, dataFrame)
        filterRes = filter12.filterResult
        if res is True:
            result.append(filterRes) 
            print(res,filterRes )
    df = pd.DataFrame(result)
    fileName = '/tmp/TestAllFile.xlsx'
    df.to_excel(fileName,encoding="utf_8_sig", index=True)
    print(df) 

def TestSingleFilter():
    fileName = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/合并/最近合并/300816.SZ.xlsx'
    stockID = '300816.SZ'
    dataFrame = pd.read_excel(fileName, index_col=None, encoding='utf_8_sig')
    filter12 = CAdvanceFilter_BOLLOpen(stockID,dataFrame)
    res = filter12.Filter(stockID, dataFrame)
    print(res)
    print(filter12.callStack)
    
if __name__ == "__main__":
    TestAllFile()