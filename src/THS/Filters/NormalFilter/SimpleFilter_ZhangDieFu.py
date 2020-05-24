# coding=utf-8
'''
@Date: 2020-05-24 21:21:16
@LastEditTime: 2020-05-24 23:04:01
@Author: yuchonghuang@sina.cn
'''

from SimpleFilterBase import CSimpleFilterBase
from SimpleFilter_KeyWords import stock_ZhangDieFu

class CSimpleFilter_ZhangDieFu(CSimpleFilterBase):
    def __init__(self,stockID = None, dataFrame = None, params = None):
        if isinstance(params, (list,tuple)) == False:
            raise Exception('CSimpleFilter_ZhangDieFu paramater error!')
        self.params = params
        CSimpleFilterBase.__init__(self,None)
        self.filterName = '涨跌幅%.2f-%.2f'%(params[0], params[1])
        self.filterDescribe = '涨跌幅在%.2f-%.2f之间过滤'%(params[0], params[1])
    
    def FilterCurrentOnly(self, stockID, dataFrame):
        if dataFrame is None:
            raise Exception('CSimpleFilter_ZhangDieFu dataFrame is None!')
        
        self.filterResult['FilterName'] = self.filterName
        zhangdieFu = float(dataFrame.iloc[-1][stock_ZhangDieFu])
        self.filterResult['涨跌幅'] = zhangdieFu
        if float(self.params[0])<= zhangdieFu < float(self.params[1]):
            return True
        else:
            return False