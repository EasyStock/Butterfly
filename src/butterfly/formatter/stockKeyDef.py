#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockKeyDef.py
@Time    :   2020/10/12 22:42:46
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

stock_Date = u'日期'
stock_ID = u'股票代码'
stock_Name = u'股票简称'
stock_OpenPrice = u'开盘价'
stock_ClosePrice = u'收盘价'
stock_ClosePrice_Yesterday = u'昨日收盘价'
stock_HighPrice = u'最高价'
stock_LowerPrice = u'最低价'
stock_Volumn = u'成交量(股)'
stock_Volumn_Ratio = u'量比'  # 0~0.8, 0.8~1.5, 1.5~2.5 2.5~5, 5~10 10~
stock_Turnover = u'成交额(元)'
stock_ZhangDieFu = u'涨跌幅(%)'

stock_MA5 = u'5MA'
stock_MA10 = u'10MA'
stock_MA20 = u'20MA'
stock_MA30 = u'30MA'
stock_MA60 = u'60MA'
stock_MA120 = u'120MA'
stock_MA240 = u'240MA'

stock_MACD = u'MACD'

stock_BOLLUp = u'BOLL上轨'
stock_BOLLMid = u'BOLL中轨'
stock_BOLLDown = u'BOLL下轨'
stock_BOLL_Percent = u'BOLL百分比'
stock_BOLL_Band_width = u'BOLL带宽'
stock_CLOSE_TO_BOLLUP = u'到BOLL上轨'
stock_CLOSE_TO_BOLLDOWN = u'到BOLL下轨'
stock_CLOSE_TO_BOLLMID = u'到BOLL中轨'
stock_CLOSE_TO_BOLL_DOWN_TO_UP = u'BOLL上下轨百分比'

stock_DISTANCE_MA_SHORT = u'短线均线乖离度'  # MA5, MA10, MA20
stock_DISTANCE_MA_MID = u'中线均线乖离度'  # MA5, MA10,MA20,MA60
stock_DISTANCE_MA_LONG = u'长线均线乖离度'  # MA5,MA10,MA20,MA60,MA120,MA240

stock_RSI_6 = u'rsi6值'
stock_RSI_12 = u'rsi12值'
stock_RSI_24 = u'rsi24值'

stock_GaiNian = u'所属概念'
stock_ShiZhi = u'a股流通市值'

stock_HangYe = u'所属行业'
stock_Days = u'上市天数'
stock_XinTai = u'技术形态'

stock_DistanceMA5 = u'股价距离5日线距离'
stock_DistanceMA10 = u'股价距离10日线距离'
stock_DistanceMA20 = u'股价距离月线距离'  # 乖离率
stock_DistanceMA30 = u'股价距离30日线距离'
stock_DistanceMA60 = u'股价距离季线距离'
stock_DistanceMA120 = u'股价距离半年线距离'
stock_DistanceMA240 = u'股价距离年线距离'


#[shortName, keyword, description]

all_Stock_keys = [stock_Date,
           stock_ID, stock_Name, stock_OpenPrice, stock_ClosePrice, stock_HighPrice, stock_LowerPrice, stock_ClosePrice_Yesterday, stock_Volumn, stock_Turnover,

           stock_Volumn_Ratio, stock_ZhangDieFu, stock_Days,

           stock_MA5, stock_MA10, stock_MA20, stock_MA30, stock_MA60, stock_MA120, stock_MA240,
           stock_DistanceMA5, stock_DistanceMA10, stock_DistanceMA20, stock_DistanceMA30, stock_DistanceMA60, stock_DistanceMA120, stock_DistanceMA240,

           stock_BOLLUp, stock_BOLLMid, stock_BOLLDown,
           stock_CLOSE_TO_BOLLUP, stock_CLOSE_TO_BOLLMID, stock_CLOSE_TO_BOLLDOWN,

           stock_CLOSE_TO_BOLL_DOWN_TO_UP, stock_BOLL_Band_width, stock_BOLL_Percent,
           stock_MACD, stock_RSI_6, stock_RSI_12, stock_RSI_24,

           stock_DISTANCE_MA_SHORT,  stock_DISTANCE_MA_MID, stock_DISTANCE_MA_LONG,
           stock_ShiZhi, stock_GaiNian, stock_HangYe, stock_XinTai,
           ]

stockKeyWordsMap = [
    ['D', stock_Date],

    ['SN', stock_Name],
    ['ID', stock_ID],
    ['OP', stock_OpenPrice],
    ['CP', stock_ClosePrice],
    ['CPL', stock_ClosePrice_Yesterday],

    ['HP', stock_HighPrice],
    ['LP', stock_LowerPrice],
    ['V', stock_Volumn],
    ['T', stock_Turnover],
    ['VR', stock_Volumn_Ratio],
    ['ZDF', stock_ZhangDieFu],
    ['TD', stock_Days],

    ['M5', stock_MA5],
    ['M10', stock_MA10],
    ['M20', stock_MA20],
    ['M30', stock_MA30],
    ['M60', stock_MA60],
    ['M120', stock_MA120],
    ['M240', stock_MA240],

    ['BU', stock_BOLLUp],
    ['BM', stock_BOLLMid],
    ['BD', stock_BOLLDown],
    ['BWP', stock_CLOSE_TO_BOLL_DOWN_TO_UP],
    ['BW', stock_BOLL_Band_width],
    ['BP', stock_BOLL_Percent],
    ['DBU', stock_CLOSE_TO_BOLLUP],
    ['DBM', stock_CLOSE_TO_BOLLMID],
    ['DBD', stock_CLOSE_TO_BOLLDOWN],

    ['MACD', stock_MACD],
    ['RSI6', stock_RSI_6],
    ['RSI12', stock_RSI_12],
    ['RSI24', stock_RSI_24],

    ['DMA5', stock_DistanceMA5],
    ['DMA10', stock_DistanceMA10],
    ['DMA20', stock_DistanceMA20],
    ['DMA30', stock_DistanceMA30],
    ['DMA60', stock_DistanceMA60],
    ['DMA120', stock_DistanceMA120],
    ['DMA240', stock_DistanceMA240],

    ['GLS', stock_DISTANCE_MA_SHORT],
    ['GLM', stock_DISTANCE_MA_MID],
    ['GLL', stock_DISTANCE_MA_LONG],
    ['SZ', stock_ShiZhi],
    ['GN', stock_GaiNian],
    ['HY', stock_HangYe],
    ['JS', stock_XinTai],
]


def ValidateListDuplicate(destList):
    ls = list(set(destList))
    if len(ls) == len(destList):
        return
    res = []
    for key in destList:
        if key not in ls:
            res.append(key)
        else:
            ls.remove(key)

    print("duplicate key:", res)

    raise Exception('duplicate key Exception')


def validateColumn():
    ValidateListDuplicate(all_Stock_keys)


def validateKeyWords():
    first = [key[0] for key in stockKeyWordsMap]
    ValidateListDuplicate(first)

    second = [key[1] for key in stockKeyWordsMap]
    ValidateListDuplicate(second)

    for key in all_Stock_keys:
        if key not in second:
            raise Exception('miss key in second:%s' % (key))

    for key in second:
        if key not in all_Stock_keys:
            raise Exception('miss key in columns:%s' % (key))


def validate():
    validateColumn()
    validateKeyWords()


def PrintKey():
    for item in stockKeyWordsMap:
        msg = '{0:{3}<15}\t{1:^15}\t{2:<10}'.format(
            item[1], "----->", item[0], chr(12288), end='')
        print(msg)

def KeyConverter(key):
    for item in stockKeyWordsMap:
        if item[0] == key:
            return item[1]
        elif item[1] == key:
            return item[0]
        else:
            continue
    raise Exception('key not found!')

if __name__ == "__main__":
    validate()
    PrintKey()
