# coding=utf-8
'''
@Date: 2020-06-11 23:10:13
@LastEditTime: 2020-06-11 23:33:01
@Author: yuchonghuang@sina.cn
'''

from SimpleFilterBase import CSimpleFilterBase
import pandas as pd
from SimpleFilter_KeyWords import stock_Date,stock_DistanceMA5,stock_DistanceMA10,stock_DistanceMA20,\
     stock_DistanceMA30, stock_DistanceMA60,stock_DistanceMA120,stock_DistanceMA240

class CSimpleFilter_GuaiLi(CSimpleFilterBase):
    def __init__(self, stockID = None, dataFrame = None, params = None):
        CSimpleFilterBase.__init__(self,None)
        self.filterName = '乖离率'
        self.filterDescribe = '乖离率'

    def FilterCurrentOnly(self, stockID, dataFrame):
        if dataFrame is None:
            raise Exception('CSimpleFilter_ZhangDieFu dataFrame is None!')
        
        self.filterResult['FilterName'] = self.filterName

        df = dataFrame.replace('--', '999999')
        df.set_index([stock_Date], inplace=True)
        df1 = pd.DataFrame(df,columns=(stock_DistanceMA5, stock_DistanceMA10,stock_DistanceMA20, stock_DistanceMA30, stock_DistanceMA60, stock_DistanceMA120,stock_DistanceMA240),copy = True)
        print(df1.tail(20))
        print(df1.quantile([0.05,0.08,0.1, 0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,0.98]))
        return True