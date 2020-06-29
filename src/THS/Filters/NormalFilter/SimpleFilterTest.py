# coding=utf-8
'''
@Date: 2020-05-24 21:25:53
@LastEditTime: 2020-06-24 14:26:18
@Author: yuchonghuang@sina.cn
'''

from SimpleFilter_TradingDay import CSimpleFilter_TradingDay
from SimpleFilter_ZhangDieFu import CSimpleFilter_ZhangDieFu
from SimpleFilter_NotST import CSimpleFilter_NotST
from SimpleFilter_Market import CSimpleFilter_Market
from SimpleFilter_GreatThanMA import CSimpleFilter_GreatThanMA
from SimpleFilter_PinBar import CSimpleFilter_PinBar
from SimpleFilter_BreakMA import CSimpleFilter_BreakMA
from SimpleFilter_GuaiLi import CSimpleFilter_GuaiLi
import pandas as pd
import os


def TestSingleFilter(): 
    fileName = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/合并/最近合并/300433.SZ.xlsx'
    stockID = '300595.SZ'
    dataFrame = pd.read_excel(fileName, index_col=None, encoding='utf_8_sig')
    #filter12 = CSimpleFilter_PinBar(stockID,dataFrame)
    #filter12 = CSimpleFilter_BreakMA(stockID,dataFrame,(10,20))
    filter12 = CSimpleFilter_GuaiLi(stockID,dataFrame)
    res = filter12.Filter(stockID, dataFrame)
    print(res)
    print(filter12.callStack)

def Test1():
    fileName = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/合并/最近合并/300595.SZ.xlsx'
    stockID = '000599.SZ'
    dataFrame = pd.read_excel(fileName, index_col=None, encoding='utf_8_sig')
    print(dataFrame) 
    filter1 = CSimpleFilter_TradingDay(stockID,dataFrame,(8788, 999999))
    filter2 = CSimpleFilter_ZhangDieFu(stockID, dataFrame,(2,4))
    filter3 = CSimpleFilter_NotST(stockID,dataFrame)
    filter4 = CSimpleFilter_Market(stockID, dataFrame,'中小板')
    filter5 = CSimpleFilter_GreatThanMA(stockID,dataFrame,5)
    filter6 = CSimpleFilter_GreatThanMA(stockID,dataFrame,10)
    filter7 = CSimpleFilter_GreatThanMA(stockID,dataFrame,20)
    filter8 = CSimpleFilter_GreatThanMA(stockID,dataFrame,30)
    filter9 = CSimpleFilter_GreatThanMA(stockID,dataFrame,60)
    filter10 = CSimpleFilter_GreatThanMA(stockID,dataFrame,120)
    filter11 = CSimpleFilter_GreatThanMA(stockID,dataFrame,240)
    filter12 = CSimpleFilter_PinBar(stockID,dataFrame)
    #res = filter1.Filter(stockID,dataFrame,(filter2, filter3,filter4,filter5,filter6,filter7,filter8,filter9,filter10,filter11))
    res = filter1.Filter(stockID,dataFrame,(filter2, filter12))
    print(res)
    print(filter1.callStack)


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
        # filter12 = CSimpleFilter_PinBar(stockID,dataFrame)
        # res = filter12.Filter(stockID, dataFrame)
        filter12 = CSimpleFilter_BreakMA(stockID,dataFrame,(30,(20,30,60)))
        res = filter12.Filter(stockID, dataFrame)
        filterRes = filter12.filterResult
        if res is True:
            result.append(filterRes) 
            print(res,filterRes )
    df = pd.DataFrame(result)
    fileName = '/tmp/TestAllFile_SimpleFilter.xlsx'
    df.to_excel(fileName,encoding="utf_8_sig", index=True)
    print(df) 
            
if __name__ == "__main__":
    TestSingleFilter()