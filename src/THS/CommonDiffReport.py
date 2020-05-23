# coding=utf-8
'''
@Date: 2020-05-15 15:49:31
@LastEditTime: 2020-05-17 22:30:07
@Author: yuchonghuang@sina.cn
'''
import pandas as pd
import os
from datetime import date

KW_COMMONDIFF_STOCK_ID = '股票代码'

class CommonDiffReport(object):
    def __init__(self):
        pass

    def notInListB(self,listA,listB):
        ret = [i for i in listA if i not in listB]
        return ret
        
    def listAnd(self, listA, listB):
        ret = [i for i in listA if i in listB]
        return ret
    
    def readFromFile(self,fileName,index = KW_COMMONDIFF_STOCK_ID):
        df = pd.read_excel(fileName, index_col=None, encoding='utf_8_sig')
        df.set_index([index], inplace=True)
        return df

    def DiffTwoFile(self, preFile,postFile,index = KW_COMMONDIFF_STOCK_ID):
        preDf = self.readFromFile(preFile,index)
        postDf = self.readFromFile(postFile,index)
        stockIDs_pre = preDf.index.to_list()
        stockIDs_post = postDf.index.to_list()

        newStockIDs = self.notInListB(stockIDs_post, stockIDs_pre)
        deleteStockIDs = self.notInListB(stockIDs_pre, stockIDs_post)
        df_new = postDf.filter(items =  newStockIDs,axis = 0)
        df_delete = preDf.filter(items =  deleteStockIDs,axis = 0)
        print(df_new)
        print(df_delete)
        return (df_new, df_delete)

    def listAllFilesInFolder(self, folder):
        allfile=[]
        for dirpath,_,filenames in os.walk(folder):
            for name in filenames:
                allfile.append(os.path.join(dirpath, name))
        return allfile
    
    def Diff(self, srcFolder, destFolder, suffix):
        allfiles = self.listAllFilesInFolder(srcFolder)
        res = [fileName for fileName in allfiles if fileName.find(suffix) != -1]
        if len(res) <2:
            raise Exception('parameter error!')
        sortedRes = sorted(res,reverse=False)
        df_new, df_delete = self.DiffTwoFile(sortedRes[-2],sortedRes[-1])
        
        destFolder = '%s/%s'%(destFolder,date.today())
        if os.path.exists(destFolder) == False:
            os.makedirs(destFolder)

        file_new =  '%s/%s_New_%s.xlsx'%(destFolder,suffix,date.today())
        file_delete =  '%s/%s_Delete_%s.xlsx'%(destFolder,suffix,date.today())
        df_new.to_excel(file_new,encoding="utf_8_sig", index=True)
        df_delete.to_excel(file_delete,encoding="utf_8_sig", index=True)

    def DiffMultiSuffix(self, srcFolder, destFolder, suffixes):
        for suffix in suffixes:
            self.Diff(srcFolder,destFolder, suffix)

if __name__ == "__main__":
    srcfolder = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/多日过滤'
    destFolder = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/多日过滤_DIFF'
    report = CommonDiffReport()
    report.DiffMultiSuffix(srcfolder,destFolder,['20日均线向上并且值大于0.05','90日新高'])