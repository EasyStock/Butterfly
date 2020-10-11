# coding=utf-8
'''
@Date: 2020-05-15 15:49:31
@LastEditTime: 2020-05-23 21:56:34
@Author: yuchonghuang@sina.cn
'''

import os
import json
import pandas as pd
import numpy as np

KW_BANKUAI_DELETE = '删除'
KW_BANKUAI_NEW = '新增'
KW_BANKUAI_EXTEND = '扩展'
KW_BANKUAI_REDUCE = '缩减'
KW_BANKUAI_GAINIAN = '所属概念'
KW_BANKUAI_STOCK_ID = '股票代码'

class BanKuaiReader(object):
    def __init__(self):
        self.banKuaiAll = {}
        self.exceptGaiNian = []

    def SplictBanKuaiInfo(self, stockID, banKuaiInfo):
        if stockID == None or banKuaiInfo == None or banKuaiInfo == np.nan or isinstance(banKuaiInfo, str) == False or len(banKuaiInfo) == 0:
            return

        gaiNians = banKuaiInfo.split(';')
        for gaiNian in gaiNians:
            if gaiNian in self.exceptGaiNian:
                continue
            else:
                if gaiNian not in self.banKuaiAll:
                    self.banKuaiAll[gaiNian] = []
                    
                self.banKuaiAll[gaiNian].append(stockID)

    def readNewBanKuaiDataFromXLS(self,banKuaiXLS):
        if banKuaiXLS.find('.xlsx') == -1:
            return

        df = pd.read_excel(banKuaiXLS, index_col=None, encoding='utf_8_sig')
        df1 = pd.DataFrame(df, columns=(KW_BANKUAI_STOCK_ID,KW_BANKUAI_GAINIAN),copy = True)
        rows = df1.shape[0]
        for i in range(1, rows):
            stockID = df1.iloc[i][KW_BANKUAI_STOCK_ID]
            banKaiInfo = df1.iloc[i][KW_BANKUAI_GAINIAN]
            self.SplictBanKuaiInfo(stockID, banKaiInfo)

    
class BanKuaiReprot(object):
    def __init__(self):
        self.banKuaiHistoryReport = {
                KW_BANKUAI_NEW:{},
                KW_BANKUAI_DELETE:{},
                KW_BANKUAI_EXTEND:{},
                KW_BANKUAI_REDUCE:{},
            }

    def notInListB(self,listA,listB):
        ret = [i for i in listA if i not in listB]
        return ret
        
    def listAnd(self, listA, listB):
        ret = [i for i in listA if i in listB]
        return ret
    
            
    def Diff(self, preData,postData):
        if isinstance(preData, BanKuaiReader) == False or isinstance(postData, BanKuaiReader) == False:
            raise Exception('preData or postData parameter error!')
        
        dictKeysA = preData.banKuaiAll.keys()
        dictKeysB = postData.banKuaiAll.keys()

        newKeys = self.notInListB(dictKeysB, dictKeysA) #New Keys
        deleteKeys = self.notInListB(dictKeysA, dictKeysB) #Delete keys
        bothKeys = self.listAnd(dictKeysA, dictKeysB)  #Both

        for key in newKeys:
            self.banKuaiHistoryReport[KW_BANKUAI_NEW][key] = postData.banKuaiAll[key]
            print(KW_BANKUAI_NEW,key, postData.banKuaiAll[key])
            
        for key in deleteKeys:
            self.banKuaiHistoryReport[KW_BANKUAI_DELETE][key] = preData.banKuaiAll[key]
            print(KW_BANKUAI_DELETE,key, preData.banKuaiAll[key])

        for key in bothKeys:
            deleteItems = self.notInListB(preData.banKuaiAll[key], postData.banKuaiAll[key])
            newItems = self.notInListB(postData.banKuaiAll[key], preData.banKuaiAll[key])
            if len(deleteItems) > 0:
                self.banKuaiHistoryReport[KW_BANKUAI_REDUCE][key] = deleteItems
                print(KW_BANKUAI_REDUCE,key, deleteItems)

            if len(newItems) > 0:
                self.banKuaiHistoryReport[KW_BANKUAI_EXTEND][key] = newItems
                print(KW_BANKUAI_EXTEND,key, newItems)

    def _formatItem(self, action, key, items):
        msg = '%s %s %s\n           '%(action, key, len(items))
        delta = 10
        size = len(items)
        for index in range(size):
            item = items[index]
            if index == 0:
                msg = msg + item
            elif index % delta == 0:
                msg = msg + '\n           ' + item
            else:
                msg = msg + ',  ' + item

        msg = msg + '\n\n'
        return msg

    def __str__(self):
        msg = ''
        for key in self.banKuaiHistoryReport[KW_BANKUAI_NEW]:
            msg = msg + self._formatItem(KW_BANKUAI_NEW, key, self.banKuaiHistoryReport[KW_BANKUAI_NEW][key])

        for key in self.banKuaiHistoryReport[KW_BANKUAI_DELETE]:
            msg = msg + self._formatItem(KW_BANKUAI_DELETE, key, self.banKuaiHistoryReport[KW_BANKUAI_DELETE][key])

        for key in self.banKuaiHistoryReport[KW_BANKUAI_REDUCE]:
            msg = msg  + self._formatItem(KW_BANKUAI_REDUCE, key, self.banKuaiHistoryReport[KW_BANKUAI_REDUCE][key])
       
        for key in self.banKuaiHistoryReport[KW_BANKUAI_EXTEND]:
            msg = msg + self._formatItem(KW_BANKUAI_EXTEND, key,self.banKuaiHistoryReport[KW_BANKUAI_EXTEND][key])

        return msg
    
    def WirteToFile(self,fileName):
        with open(fileName, 'w+') as f:
            f.write(self.__str__())

def listAllFilesInFolder(folder):
    allfile=[]
    for dirpath,_,filenames in os.walk(folder):
        for name in filenames:
            if name.find('.xlsx') == -1:
                continue
            allfile.append(os.path.join(dirpath, name))
    return allfile
    

def WrietBanKuaiReport(srcFolder):
    listFiles = listAllFilesInFolder(srcFolder)
    listFiles = sorted(listFiles,reverse= False)
    print(listFiles[-3:])
    report1 = BanKuaiReader()
    report1.readNewBanKuaiDataFromXLS(listFiles[-2])

    report2 = BanKuaiReader()
    report2.readNewBanKuaiDataFromXLS(listFiles[-1])
    r = BanKuaiReprot()
    r.Diff(report1,report2)
    r.WirteToFile('/tmp/aa.txt')

if __name__ == "__main__":
    srcFolder = '/Volumes/Data/Code/github/TreaderAnalysis/data/output/股票/每日数据'
    srcFolder2 = '/Volumes/Data/Code/github/TradingData/OutData/股票/Daily'
    WrietBanKuaiReport(srcFolder)
    