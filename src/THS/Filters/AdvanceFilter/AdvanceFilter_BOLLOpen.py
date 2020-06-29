# coding=utf-8
'''
@Date: 2020-06-06 09:54:33
@LastEditTime: 2020-06-07 20:41:18
@Author: yuchonghuang@sina.cn
'''
from AdvanceFilterBase import CAdvanceFilterBase
from AdvanceFilter_KeyWords import stock_ClosePrice, stock_BOLLDown,stock_BOLLUp,stock_Date,stock_Name,stock_BOLLMid

class CAdvanceFilter_BOLLOpen(CAdvanceFilterBase):
    def __init__(self, stockID = None, dataFrame = None, params = None):
        CAdvanceFilterBase.__init__(self,None)
        self.filterName = 'BOLL开口'
        self.filterDescribe = 'BOLL开口过滤'
        
    def isBOLLOpen(self,dataFrame):
        lastBollUp = dataFrame.iloc[-1][stock_BOLLUp]
        lastBollDown = dataFrame.iloc[-1][stock_BOLLDown]
        
        count = 0
        size = dataFrame.shape[0]
        for index in range(2,size):
            bollUp = dataFrame.iloc[-index][stock_BOLLUp]
            bollDown = dataFrame.iloc[-index][stock_BOLLDown]
            if (lastBollUp > bollUp and bollDown > lastBollDown):
                count = count + 1
                lastBollUp = bollUp
                lastBollDown = bollDown
            else:
                break
        
        return count

    def FilterCurrentOnly(self, stockID, dataFrame):
        if dataFrame is None:
            raise Exception('CAdvanceFilter_BOLLOpen dataFrame is None!')
        size = dataFrame.shape[0]
        if size <= 2:
            return False

        self.filterResult['FilterName'] = self.filterName
        bollOpenCount = self.isBOLLOpen(dataFrame)
        self.filterResult['BollOpenDays'] = bollOpenCount
        self.filterResult[stock_Date] = dataFrame.iloc[-1][stock_Date]
        self.filterResult[stock_Name] = dataFrame.iloc[-1][stock_Name]
        try:
            bollUp = dataFrame.iloc[-1][stock_BOLLMid] > dataFrame.iloc[-2][stock_BOLLMid]
            if bollUp:
                self.filterResult['开口方向'] = '上'
            else:
                self.filterResult['开口方向'] = '下'
        except:
            self.filterResult['开口方向'] = '未知'

        try:
            d = (float(dataFrame.iloc[-1][stock_BOLLUp]) - float(dataFrame.iloc[-2][stock_BOLLUp]))/ float(dataFrame.iloc[-2][stock_ClosePrice])*100
            self.filterResult['开口百分比'] = float('%.2f'%(d))
        except:
            self.filterResult['开口百分比'] = '未知'
            return False

        if bollOpenCount > 0:
            return True
        else:
            return False
        