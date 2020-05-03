# coding=utf-8
'''
@Date: 2020-05-03 15:46:14
@LastEditTime: 2020-05-03 22:21:43
@Author: yuchonghuang@sina.cn
'''

import SplitAndIndexRawData
import ConverHTMLToXLSX
import ReadAllXLSXData

srcFolder = '/Volumes/Data/StockAssistant/EasyStock/TradingData/RawData/股票'
srcTempFolder = '/Volumes/Data/StockAssistant/EasyStock/TradingData/临时数据/股票/'
destFolder = '/Volumes/Data/StockAssistant/EasyStock/TradingData/OutData/股票/Daily/'

def ToSplitRawDataAndCreateIndex():
    return SplitAndIndexRawData.ToSplitRawDataAndCreateIndex(srcTempFolder,srcFolder)

def ToConverHTMLToXlSX(fileList):
    ConverHTMLToXLSX.ToConverHTMLToXlSX(fileList,destFolder)


def ToReadAllXLSXData(sinceDate = '2020-04-25',lastN = 3):
    return ReadAllXLSXData.ToReadAllXLSXData(destFolder,lastN=lastN)

if __name__ == "__main__":
    res = ToSplitRawDataAndCreateIndex()
    fileList = res.values()
    ToConverHTMLToXlSX(fileList)
    res = ToReadAllXLSXData()
    for d in res:
        print(d, res[d])
        input()