# coding=utf-8
'''
@Date: 2020-05-24 20:22:50
@LastEditTime: 2020-06-05 20:29:48
@Author: yuchonghuang@sina.cn
'''

# coding=utf-8
'''
@Date: 2020-05-24 20:22:50
@LastEditTime: 2020-05-24 22:43:19
@Author: yuchonghuang@sina.cn
'''

class CAdvanceFilterBase(object):
    def __init__(self, stockID = None, dataFrame = None, params = None):
        self.filterName = "None"
        self.filterDescribe = None
        self.filterResult = {}
        self.callStack = []
        
    def Filter(self, stockID, dataFrame, nextFilter = None):
        res = self.FilterCurrentOnly(stockID, dataFrame)
        self.filterResult['FilterResult'] = res
        self.filterResult['stockID'] = stockID
        self.callStack.append(self.filterResult)
        if res == False :
            return False
        
        if res == None:
            raise Exception('filter result should return Bool')

        return self.FilterNext(stockID, dataFrame,nextFilter)

    def FilterCurrentOnly(self, stockID, dataFrame):
        return False

    def FilterNext(self, stockID, dataFrame, nextFilter = None):
        if dataFrame is None :
            raise Exception('FilterNext dataFrame is None')

        if stockID is None:
            raise Exception('FilterNext stockID is None')
        
        if nextFilter is None:
            return True #filterResult, callStack
        
        if isinstance(nextFilter,(list, tuple)) == False:
            raise Exception('nextFilter should be a list or tuple!')

        for filter_ in nextFilter:
            res = filter_.FilterCurrentOnly(stockID, dataFrame)
            filter_.filterResult['FilterResult'] = res
            self.callStack.append(filter_.filterResult)
            if res == False:
                return res
            else:
                continue
