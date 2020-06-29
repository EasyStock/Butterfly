# coding=utf-8
'''
@Date: 2020-06-10 22:45:42
@LastEditTime: 2020-06-11 12:00:38
@Author: yuchonghuang@sina.cn
'''

from SimpleFilterBase import CSimpleFilterBase
from SimpleFilter_KeyWords import stock_DistanceMA5,stock_Name,stock_DistanceMA10,stock_DistanceMA20,stock_DistanceMA30,stock_DistanceMA60,stock_DistanceMA120,stock_DistanceMA240,stock_Date

class CSimpleFilter_BreakMA(CSimpleFilterBase):
    '''
    破均线的概率
    参数N，代表天数
    参数MA，代表均线
    返回值: 这N天跌破均线的概率和是天数
    '''
    def __init__(self, stockID = None, dataFrame = None, params = None):
        if isinstance(params, (list,tuple)) == False:
            raise Exception('CSimpleFilter_BreakMA paramater error!')
        self.N = params[0]
        self.MA = params[1]
        CSimpleFilterBase.__init__(self,None)
        self.filterName = '%s天跌破均线%s概率过滤'%(self.N,self.MA)
        self.filterDescribe = '%s天跌破均线%s概率过滤'%(self.N,self.MA)
    
    def FilterMA(self, stockID, dataFrame,column):
        size = dataFrame.shape[0]
        if size < self.N:
            return (False,0)
        
        count = 0
        for index in range(1, self.N+1):
            try:
                guaili = float(dataFrame.iloc[-index][column])
                
                if guaili > 0:
                    count = count + 1
                # else:
                #     date = dataFrame.iloc[-index][stock_Date]
                #     print(date)
            except:
                return (False,0)
        
        return (True,count)
    
    def FilterByMA(self, stockID, dataFrame, MA):
        res = (False,0)
        if MA == 5:
            res = self.FilterMA(stockID,dataFrame,stock_DistanceMA5)
        elif MA == 10:
            res = self.FilterMA(stockID,dataFrame,stock_DistanceMA10)
        elif MA == 20:
            res = self.FilterMA(stockID,dataFrame,stock_DistanceMA20)
        elif MA == 30:
            res = self.FilterMA(stockID,dataFrame,stock_DistanceMA30)
        elif MA == 60:
            res = self.FilterMA(stockID,dataFrame,stock_DistanceMA60)
        elif MA == 120:
            res = self.FilterMA(stockID,dataFrame,stock_DistanceMA120)
        elif MA == 240:
            res = self.FilterMA(stockID,dataFrame,stock_DistanceMA240)
        else:
            raise Exception('CSimpleFilter_BreakMA FilterCurrentOnly parameter error!')
        
        if res[0] == False:
            return False

        key = '%s天未跌破均线%s概率'%(self.N,MA)
        self.filterResult[key] = float('%.2f'%(1.0*res[1] / self.N*100))
        key1 = '%s天未跌破均线%s天数'%(self.N,MA)
        self.filterResult[key1] = res[1]
        return True

    def FilterCurrentOnly(self, stockID, dataFrame):
        if dataFrame is None:
            raise Exception('CSimpleFilter_BreakMA dataFrame is None!')
        
        self.filterResult['FilterName'] = self.filterName
        self.filterResult['天数'] = self.N
        if isinstance(self.MA, (list,tuple)):
            ret = False
            for MA in self.MA:
                res = self.FilterByMA(stockID, dataFrame, MA)
                ret = (ret or res)
            return ret
        else:
            return self.FilterByMA(stockID, dataFrame, self.MA)