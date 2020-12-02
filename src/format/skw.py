#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   skw.py
@Time    :   2020/10/12 22:34:17
@Author  :   JianPing Huang 
@Contact :   yuchonghuang@126.com
'''

#[shortName, keyword, description]

colunms = ['日期',
           '股票代码', '股票简称', '开盘价', '收盘价', '最高价',
           '最低价', '昨日收盘价', '成交量(股)', '成交额(元)', '量比',
           '涨跌幅(%)', '上市天数',
           '5MA', '10MA', '20MA', '30MA', '60MA', '120MA', '240MA',
           'BOLL上轨', 'BOLL中轨', 'BOLL下轨', 'BOLL上下轨百分比', 'BOLL带宽', 'BOLL百分比', '到BOLL上轨', '到BOLL中轨', '到BOLL下轨',
           'MACD', 'rsi6值', 'rsi12值', 'rsi24值',
           '股价距离5日线距离', '股价距离10日线距离', '股价距离月线距离', '股价距离30日线距离', '股价距离季线距离', '股价距离半年线距离', '股价距离年线距离',
           '短线均线乖离度',  '中线均线乖离度', '长线均线乖离度',
           'a股流通市值', '所属概念', '所属行业', '技术形态',
           ]

stockKeyWords = [
    ['D', '日期'],

    ['SN', '股票名称'],
    ['ID', '股票代码'],
    ['OP', '开盘价'],
    ['CP', '收盘价'],
    ['CPL', '昨日收盘价'],

    ['HP', '最高价'],
    ['LP', '最低价'],
    ['V', '成交量(股)'],
    ['T', '成交额(元)'],
    ['VR', '量比'],
    ['ZDF', '涨跌幅(%)'],
    ['TD', '上市天数'],

    ['M5', '5日均线'],
    ['M10', '10日均线'],
    ['M20', '20日均线'],
    ['M30', '30日均线'],
    ['M60', '60日均线'],
    ['M120', '120日均线'],
    ['M240', '240日均线'],

    ['BU', 'BOLL上轨'],
    ['BM', 'BOLL中轨'],
    ['BD', 'BOLL下轨'],
    ['BWP', 'BOLL上下轨百分比'],
    ['BW', 'BOLL带宽'],
    ['BP', 'BOLL百分比'],
    ['DBU', '到BOLL上轨'],
    ['DBM', '到BOLL中轨'],
    ['DBD', '到BOLL下轨'],

    ['MACD', 'MACD'],
    ['RSI6', 'rsi6值'],
    ['RSI12', 'rsi12值'],
    ['RSI24', 'rsi24值'],

    ['DMA5', '股价距离5日线距离'],
    ['DMA10', '股价距离10日线距离'],
    ['DMA20', '股价距离月线距离'],
    ['DMA30', '股价距离30日线距离'],
    ['DMA60', '股价距离季线距离'],
    ['DMA120', '股价距离半年线距离'],
    ['DMA240', '股价距离年线距离'],

    ['GLS', '短线均线乖离度'],
    ['GLM', '中线均线乖离度'],
    ['GLL', '长线均线乖离度'],
    ['SZ', 'a股流通市值'],
    ['GN', '所属概念'],
    ['HY', '所属行业'],
    ['JS', '技术形态'],
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
    ValidateListDuplicate(colunms)


def validateKeyWords():
    first = [key[0] for key in stockKeyWords]
    ValidateListDuplicate(first)

    second = [key[1] for key in stockKeyWords]
    ValidateListDuplicate(second)


def validate():
    validateColumn()
    validateKeyWords()


def PrintKey():
    for item in stockKeyWords:
        msg = '{0:{3}<15}\t{1:^15}\t{2:<10}'.format(
            item[1], "----->", item[0], chr(12288), end='')
        print(msg)


if __name__ == "__main__":
    validate()
    PrintKey()
