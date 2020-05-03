# coding=utf-8
'''
@Date: 2020-05-03 15:46:14
@LastEditTime: 2020-05-03 16:09:17
@Author: yuchonghuang@sina.cn
'''
from StockDataItemIO import StockItemIO

if __name__ == "__main__":
    fileName = u'/Volumes/Data/StockAssistant/EasyStock/TradingData/RawData/股票/2020/Q2/2020-04-24.xls'
    fileName_dest = u'/tmp/2019-05-07.xlsx'
    io = StockItemIO.CStockItemIO()
    io.readFrom(fileName)
    io.saveTo(fileName_dest)