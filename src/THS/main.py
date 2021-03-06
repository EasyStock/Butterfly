# coding=utf-8
'''
@Date: 2020-05-03 15:46:14
@LastEditTime: 2020-06-01 20:15:25
@Author: yuchonghuang@sina.cn
'''

import SplitAndIndexRawData
import ConverHTMLToXLSX 
import ReadAllXLSXData
import MergeDailyData
import MarketHot
import BanKuaiReport

srcFolder = '/Volumes/Data/Code/github/TradingData/RawData/股票'
srcTempFolder = '/Volumes/Data/Code/github/TradingData/临时数据/股票/'
destFolder = '/Volumes/Data/Code/github/TradingData/OutData/股票/Daily/'
destFolder_MergeData = '/Volumes/Data/Code/github/TradingData/OutData/股票/Merged/'

allDailyFiles = None #{date:file}
allDailyDataFrames = None #{date:DataFrame}
allMergedDataFrames = None #{stockID:dataFrame}

def ToSplitRawDataAndCreateIndex():
    return SplitAndIndexRawData.ToSplitRawDataAndCreateIndex(srcTempFolder,srcFolder)

def ToConverHTMLToXlSX(fileList):
    if isinstance(fileList, dict):
        fileList = fileList.values()
    ConverHTMLToXLSX.ToConverHTMLToXlSX(fileList,destFolder)


def ToReadAllXLSXData(sinceDate = None,lastN = 3):
    return ReadAllXLSXData.ToReadAllXLSXData(destFolder,since = sinceDate, lastN=lastN)

def ToMergeDailyData(dataFrameDict,destFolder):
    return MergeDailyData.ToMergeDailyData(dataFrameDict,destFolder)

def CalculateMarketHotWithFolder():
    return MarketHot.CalculateMarketHotWithFolder_Multi(destFolder)

def ToWriteBanKuaiReport():
    return BanKuaiReport.WrietBanKuaiReport(destFolder)
    
if __name__ == "__main__":
    allDailyFiles = ToSplitRawDataAndCreateIndex()
    ToConverHTMLToXlSX(allDailyFiles)
    ToWriteBanKuaiReport()

    # allDailyDataFrames = ToReadAllXLSXData(sinceDate='2019-05-14')
    # mergedDict = ToMergeDailyData(allDailyDataFrames,destFolder_MergeData)

    CalculateMarketHotWithFolder() 
    
 