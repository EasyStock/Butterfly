# coding=utf-8
'''
@Date: 2020-05-20 22:35:25
@LastEditTime: 2020-05-23 21:48:23
@Author: yuchonghuang@sina.cn
'''
import pandas as pd
import os
import multiprocessing as mp
import time

KW_MA5 = '5MA'
KW_MA10 = '10MA'
KW_MA20 = '20MA'
KW_MA30 = '30MA'
KW_MA60 = '60MA'
KW_MA120 = '120MA'
KW_MA240 = '240MA'
KW_Close = '收盘价'
UNKNOWN_VALUE = 99999.00

KW_greaterThanMA5 = '大于MA5'
KW_greaterThanMA10 = '大于MA10'
KW_greaterThanMA20 = '大于MA20'
KW_greaterThanMA30 = '大于MA30'
KW_greaterThanMA60 = '大于MA60'
KW_greaterThanMA120 = '大于MA120'
KW_greaterThanMA240 = '大于MA240'
KW_Total = '总数'
KW_date = '日期'
KW_STOCK_ID = '股票代码'
KW_ZHUBAN = "主  板"
KW_KECHUANG = "科创板"
KW_CHUANG_YE = "创业板"
KE_ZHONGXIAO = "中小板"

class MakrketHot(object):
    def __init__(self):
        pass

    
    def _GetCountOf(self, df, column1, column2, key):
        res = df[df[column1] > df[column2]]
        return {
            key:res.shape[0]
        }

    def _FilterStockIDBy(self, df, reg ='^60'):
        res = df[df[KW_STOCK_ID].str.contains(reg)]
        return res
    
    def _Count(self, df,date):
        res = {}
        size_all = df.shape[0]
        res[KW_Total] = size_all
        res[KW_date] = date
        df1 = pd.DataFrame(df, columns=(KW_Close,KW_MA5,KW_MA10,KW_MA20, KW_MA30, KW_MA60, KW_MA120, KW_MA240),copy = True,dtype = float) 
        res.update(self._GetCountOf(df1, KW_Close, KW_MA5, KW_greaterThanMA5))
        res.update(self._GetCountOf(df1, KW_Close, KW_MA10, KW_greaterThanMA10))
        res.update(self._GetCountOf(df1, KW_Close, KW_MA20, KW_greaterThanMA20))
        res.update(self._GetCountOf(df1, KW_Close, KW_MA30, KW_greaterThanMA30))
        res.update(self._GetCountOf(df1, KW_Close, KW_MA60, KW_greaterThanMA60))
        res.update(self._GetCountOf(df1, KW_Close, KW_MA120, KW_greaterThanMA120))
        res.update(self._GetCountOf(df1, KW_Close, KW_MA240, KW_greaterThanMA240))
        return res
        
    def ReadFromFile(self, fileName):
        res = {}
        date = fileName[fileName.rfind('/')+1:fileName.rfind('.')]
        df = pd.read_excel(fileName, index_col=None, encoding='utf_8_sig')
        
        df = df.replace('--', UNKNOWN_VALUE)
        df_SH_ZhuBan = self._FilterStockIDBy(df,'^60\d{4}.SH')
        df_SH_KeChuang = self._FilterStockIDBy(df,'^68\d{4}.SH')
        df_SZ_ChuangYe = self._FilterStockIDBy(df,'^30\d{4}.SZ')
        df_SZ_XiaoBan = self._FilterStockIDBy(df,'^00\d{4}.SZ')
        # print(KW_ZHUBAN, df_SH_ZhuBan.shape[0])
        # print(KW_KECHUANG, df_SH_KeChuang.shape[0])
        # print(KW_CHUANG_YE, df_SZ_ChuangYe.shape[0])
        # print(KE_ZHONGXIAO, df_SZ_XiaoBan.shape[0])

        res[KW_ZHUBAN] = self._Count(df_SH_ZhuBan,date)
        res[KW_KECHUANG] = self._Count(df_SH_KeChuang,date)
        res[KW_CHUANG_YE] = self._Count(df_SZ_ChuangYe,date)
        res[KE_ZHONGXIAO] = self._Count(df_SZ_XiaoBan,date)
        #print(res)
        return res


def listAllFilesInFolder(folder):
    allfile=[]
    for dirpath,_,filenames in os.walk(folder):
        for name in filenames:
            allfile.append(os.path.join(dirpath, name))
    return allfile
        
def _CalculateMarketHotMultiPro(fileName):
    mkth = MakrketHot()
    return mkth.ReadFromFile(fileName)


def printDataFrame(key, df):
    print("\n\n\n=============%s================"%(key))
    print(df.tail(10))

    print("\n\n\n=============平均值 %s================"%(key))
    print(df.mean())

    print("\n\n\n=============分为数 %s================"%(key))
    print(df.quantile([0.05,0.1, 0.5, 0.9, 0.95,0.98]))
    fileName = '/Volumes/Data/StockAssistant/EasyStock/TradingData/%s.xlsx'%(key)
    df.to_excel(fileName, encoding="utf_8_sig", index=False)

def CalculateMarketHotWithFolder_Multi(folder):
    fileNameList = listAllFilesInFolder(folder)
    dataFrames = []
    begin_time = time.time()
    pool = mp.Pool(mp.cpu_count()*2)

    for fullpath in fileNameList:
        if fullpath.find('.xlsx') == -1:
            continue
        dataFrames.append(pool.apply_async(_CalculateMarketHotMultiPro, (fullpath, )))

    pool.close()
    pool.join()
    endTime = time.time()
    print('CalculateMarketHotWithFolder_Multi cost:%s, total: %d' % ((endTime - begin_time), len(dataFrames)))
    res = {
        KW_ZHUBAN:[],
        KW_KECHUANG:[],
        KW_CHUANG_YE:[],
        KE_ZHONGXIAO:[],
    }
    for item in dataFrames:
        res[KW_ZHUBAN].append(item.get()[KW_ZHUBAN])
        res[KW_KECHUANG].append(item.get()[KW_KECHUANG])
        res[KW_CHUANG_YE].append(item.get()[KW_CHUANG_YE])
        res[KE_ZHONGXIAO].append(item.get()[KE_ZHONGXIAO])

    columns = [KW_date, KW_greaterThanMA5,  KW_greaterThanMA10, KW_greaterThanMA20, KW_greaterThanMA30, KW_greaterThanMA60,KW_greaterThanMA120,KW_greaterThanMA240, KW_Total]
    df = pd.DataFrame(res[KW_ZHUBAN],columns=columns)
    printDataFrame(KW_ZHUBAN, df)
    

    df = pd.DataFrame(res[KW_KECHUANG],columns=columns)
    printDataFrame(KW_KECHUANG, df)

    df = pd.DataFrame(res[KW_CHUANG_YE],columns=columns)
    printDataFrame(KW_CHUANG_YE, df)
    
    df = pd.DataFrame(res[KE_ZHONGXIAO],columns=columns)
    printDataFrame(KE_ZHONGXIAO, df)

if __name__ == "__main__":
    folder = '/Volumes/Data/StockAssistant/EasyStock/TradingData/OutData/股票/Daily/'
    CalculateMarketHotWithFolder_Multi(folder)
    # fileName = '/Volumes/Data/StockAssistant/EasyStock/TradingData/OutData/股票/Daily/2020/Q2/2020-05-15.xlsx'
    # mak = MakrketHot()
    # mak.ReadFromFile(fileName)
    
