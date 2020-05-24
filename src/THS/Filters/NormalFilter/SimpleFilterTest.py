# coding=utf-8
'''
@Date: 2020-05-24 21:25:53
@LastEditTime: 2020-05-24 23:03:17
@Author: yuchonghuang@sina.cn
'''

from SimpleFilter_TradingDay import CSimpleFilter_TradingDay
from SimpleFilter_ZhangDieFu import CSimpleFilter_ZhangDieFu
from SimpleFilter_NotST import CSimpleFilter_NotST
from SimpleFilter_Market import CSimpleFilter_Market
from SimpleFilter_GreatThanMA import CSimpleFilter_GreatThanMA
import pandas as pd


def Test1():
    fileName = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/合并/最近合并/000599.SZ.xlsx'
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
    res = filter1.Filter(stockID,dataFrame,(filter2, filter3,filter4,filter5,filter6,filter7,filter8,filter9,filter10,filter11))
    print(res)
    print(filter1.callStack)

if __name__ == "__main__":
    Test1()