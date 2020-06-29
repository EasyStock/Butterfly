# coding=utf-8
'''
@Date: 2020-05-25 09:09:39
@LastEditTime: 2020-06-04 16:09:22
@Author: yuchonghuang@sina.cn
'''

from SimpleFilterBase import CSimpleFilterBase
from SimpleFilter_KeyWords import stock_ClosePrice, stock_OpenPrice, stock_HighPrice, stock_LowerPrice,stock_ClosePrice_Yesterday,stock_Date,stock_Name

class CSimpleFilter_PinBar(CSimpleFilterBase):
    def __init__(self, stockID = None, dataFrame = None, params = None):
        CSimpleFilterBase.__init__(self,None)
        self.filterName = '简单PinBar'
        self.filterDescribe = '简单PinBar'

    def UpPinBar(self, openPrice, closePrice, highPrice, lowPrice,closePrice_Yesterday):
        totalSize = highPrice - lowPrice
        min_open_close = min(openPrice, closePrice)
        max_open_close = max(openPrice, closePrice)
        shadow_down = min_open_close - lowPrice # 下影线
        body = max_open_close - min_open_close

        if totalSize == 0.0:
            return (False, 0,0)
        
        if closePrice < 5: #股价小于5
            return (False, 0,0)
            
        raito_shadow = shadow_down / totalSize
        bodyRatio = body / totalSize
            
        if  raito_shadow < 0.667:
            return (False, raito_shadow,bodyRatio) #下影线 部分必须超过振幅的2/3

        if bodyRatio < 0.1:
            return (False, raito_shadow,bodyRatio) #实体部分不能太小
        
        if totalSize / closePrice_Yesterday <0.05:
            return (False, raito_shadow,bodyRatio) #振幅小于 5%

        return (True, raito_shadow,bodyRatio)

    
    def DownPinBar(self, openPrice, closePrice, highPrice, lowPrice,closePrice_Yesterday):
        totalSize = highPrice - lowPrice
        min_open_close = min(openPrice, closePrice)
        max_open_close = max(openPrice, closePrice)
        shadow_up = highPrice - max_open_close #上影线
        body = max_open_close - min_open_close

        if totalSize == 0.0:
            return (False, 0,0)

        if closePrice < 5: #股价小于5
            return (False, 0,0)
            
        raito_shadow = shadow_up / totalSize
        bodyRatio = body / totalSize

        if  raito_shadow < 0.667:  #影线占K线的2/3
            return (False, raito_shadow,bodyRatio)
        
        if bodyRatio < 1.0/6: #实体部分占比 1/3 X 1/2 ～ 1/3
            return (False, raito_shadow,bodyRatio)

        if totalSize / closePrice_Yesterday <0.05:
            return (False, raito_shadow,bodyRatio) #振幅小于 5%

        return (True, raito_shadow,bodyRatio)
    
    def FilterCurrentOnly(self, stockID, dataFrame):
        if dataFrame is None:
            raise Exception('CSimpleFilter_PinBar dataFrame is None!')

        self.filterResult['FilterName'] = self.filterName
        openPrice = float(dataFrame.iloc[-1][stock_OpenPrice])
        closePrice = float(dataFrame.iloc[-1][stock_ClosePrice])
        highPrice = float(dataFrame.iloc[-1][stock_HighPrice])
        lowPrice = float(dataFrame.iloc[-1][stock_LowerPrice])
        closePrice_Yesterday = float(dataFrame.iloc[-1][stock_ClosePrice_Yesterday])
        
        min_open_close = min(openPrice, closePrice)
        max_open_close = max(openPrice, closePrice)
        
        try:
            highPrice_yesterday = float(dataFrame.iloc[-2][stock_HighPrice])
            lowPrice_yesterday = float(dataFrame.iloc[-2][stock_LowerPrice])
            bodyIn = (lowPrice_yesterday <  min_open_close < max_open_close < highPrice_yesterday)
            zhenfu = (highPrice - lowPrice) > (highPrice_yesterday - lowPrice_yesterday)
            self.filterResult['bodyIn'] = bodyIn
            self.filterResult['zhenfu'] = zhenfu
            self.filterResult['左眼'] = (bodyIn and zhenfu)
        except:
            self.filterResult['bodyIn'] = False
            self.filterResult['zhenfu'] = False
            self.filterResult['左眼'] = False
            
        self.filterResult['振幅'] = float('%.2f'%((highPrice - lowPrice)/closePrice_Yesterday* 100))
        self.filterResult[stock_Date] = dataFrame.iloc[-1][stock_Date]

        upres, raito_shadow, bodyRatio = self.UpPinBar(openPrice,closePrice,highPrice,lowPrice,closePrice_Yesterday)
        self.filterResult['下影线'] = raito_shadow
        self.filterResult['实体'] = bodyRatio
        
        downres, raito_shadow, bodyRatio = self.DownPinBar(openPrice,closePrice,highPrice,lowPrice, closePrice_Yesterday)
        self.filterResult['上影线'] = raito_shadow
        self.filterResult['实体'] = bodyRatio
        self.filterResult[stock_Name] = dataFrame.iloc[-1][stock_Name]

        if upres is True:
            self.filterResult['方向'] = 'UpPinBar'
            return True
        
        if downres is True:
            self.filterResult['方向'] = 'DownPinBar'
            return True   
        
        return False