# coding=utf-8
'''
@Date: 2020-05-24 22:45:38
@LastEditTime: 2020-05-24 22:54:07
@Author: yuchonghuang@sina.cn
'''

from  SimpleFilterBase import CSimpleFilterBase
import re

STOCK_MARKET_NONE = 'NONE'
STOCK_MARKET_SHANGHAI = '主板'
STOCK_MARKET_ZHONGXIAOBAN= '中小板'
STOCK_MARKET_CHUANGYEBAN = '创业板'
STOCK_MARKET_KECHUANGBAN= '科创板'

class CSimpleFilter_Market(CSimpleFilterBase):
    def __init__(self, stockID = None, dataFrame = None, params = (STOCK_MARKET_SHANGHAI,STOCK_MARKET_ZHONGXIAOBAN, STOCK_MARKET_CHUANGYEBAN,  STOCK_MARKET_KECHUANGBAN)):
        CSimpleFilterBase.__init__(self,None)
        self.filterName = '交易板块过滤'
        self.filterDescribe = '交易板块过滤'
        self.banKuai = params
        
    def FilterCurrentOnly(self, stockID, dataFrame):
        self.filterResult['FilterName'] = self.filterName
        res = STOCK_MARKET_NONE
        if re.search('^60',stockID) is not None:
            res = STOCK_MARKET_SHANGHAI
        elif re.search('^30',stockID) is not None:
            res = STOCK_MARKET_CHUANGYEBAN
        elif re.search('^00',stockID) is not None:
            res = STOCK_MARKET_ZHONGXIAOBAN
        elif re.search('^68',stockID) is not None:
            res = STOCK_MARKET_KECHUANGBAN
        else:
            res = STOCK_MARKET_NONE

        self.filterResult['板块'] = res
        if isinstance(self.banKuai,(list,tuple)) == True:
            if res in self.banKuai:
                return True
            else:
                return False
        else:
            if self.banKuai == res:
                return True
            else:
                return False

        return False