# coding=utf-8
'''
@Date: 2020-05-24 22:00:21
@LastEditTime: 2020-05-24 23:03:52
@Author: yuchonghuang@sina.cn
'''

from SimpleFilterBase import CSimpleFilterBase
from SimpleFilter_KeyWords import stock_Name

class CSimpleFilter_NotST(CSimpleFilterBase):
    def __init__(self, stockID = None, dataFrame = None, params = None):
        CSimpleFilterBase.__init__(self,None)
        self.filterName = '非ST'
        self.filterDescribe = '非ST过滤'
        
    def FilterCurrentOnly(self, stockID, dataFrame):
        if dataFrame is None:
            raise Exception('CSimpleFilter_ZhangDieFu dataFrame is None!')

        self.filterResult['FilterName'] = self.filterName
        name = dataFrame.iloc[-1][stock_Name]
        self.filterResult['StockName'] = name
        if name.lower().find('st') != -1:
            return False
            
        return True