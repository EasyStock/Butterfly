# coding=utf-8
'''
@Date: 2020-05-09 16:59:15
@LastEditTime: 2020-05-11 17:48:06
@Author: yuchonghuang@sina.cn
'''
import pandas as pd
import time
import multiprocessing as mp
import os

colunms = [ '日期',
            '股票代码','股票简称','开盘价','收盘价','最高价',
            '最低价','昨日收盘价', '成交量(股)','成交额(元)','量比',
            '涨跌幅(%)','上市天数',
            '5MA','10MA','20MA', '30MA', '60MA', '120MA', '240MA',
            'BOLL上轨','BOLL中轨','BOLL下轨','BOLL上下轨百分比','BOLL带宽','BOLL百分比','到BOLL上轨','到BOLL中轨', '到BOLL下轨',
             'MACD','rsi6值','rsi12值', 'rsi24值',
            '股价距离5日线距离','股价距离10日线距离', '股价距离月线距离','股价距离30日线距离','股价距离季线距离','股价距离半年线距离', '股价距离年线距离',
            '短线均线乖离度',  '中线均线乖离度', '长线均线乖离度',
            'a股流通市值','所属概念', '所属行业', '技术形态', 
          ]


def _WriteMergeDataToFile(stockID, dataFrame, destFolder):
    if stockID is None or dataFrame is None or destFolder is None:
        print('_WriteMergeDataToFile, parameter error')
        return
    
    destFileName = '%s/%s.xlsx'%(destFolder,stockID)
    dataFrame.to_excel(destFileName,encoding="utf_8_sig", index=True)
    print(destFileName, 'Merged, Done!')

def WriteMergeDataToFile(mergedResult, destFolder):
    res = {}
    begin_time = time.time()
    pool = mp.Pool(mp.cpu_count()*2)
    if os.path.exists(destFolder) == False:
        os.makedirs(destFolder)

    for stockID in mergedResult:
        df = pd.DataFrame(mergedResult[stockID],columns=colunms)
        df.set_index(["日期"], inplace=True)
        res[stockID] = df
        pool.apply_async(_WriteMergeDataToFile, (stockID, df,destFolder))
    
    pool.close() 
    pool.join()
    endTime = time.time()
    print('WriteMergeDataToFile:%s'%(endTime - begin_time))
    return res

def ToMergeDailyData(dfDict,destFolder):
    res = {}
    for date in dfDict:
        dictInfos = dfDict[date].T.to_dict().values()
        for dictInfo in dictInfos:
            stockID = dictInfo['股票代码']
            if stockID not in res:
                res[stockID] = []
            dictInfo['日期'] = date
            res[stockID].append(dictInfo)  

    return WriteMergeDataToFile(res,destFolder)
