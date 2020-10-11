# coding=utf-8
'''
@Date: 2020-10-05 23:00:38
@LastEditTime: 2020-10-05 23:00:38
@Author: yuchonghuang@sina.cn
'''
#[shortName, keyword, description]

colunms = [ '日期',
            '股票代码','股票简称','开盘价','收盘价','最高价',
            '最低价','昨日收盘价', '成交量(股)','成交额(元)','量比',
            '涨跌幅(%)','上市天数',
            '5MA','10MA','20MA', '30MA', '60MA', '120MA', '240MA',
            'BOLL上轨','BOLL中轨','BOLL下轨','BOLL上下轨百分比','BOLL带宽','BOLL百分比','到BOLL上轨','到BOLL中轨', '到BOLL下轨',
             'MACD','rsi6值','rsi12值', 'rsi24值',
            '股价距离5日线距离','股价距离10日线距离', '股价距离月线距离','股价距离30日线距离','股价距离季线距离','股价距离半年线距离', '股价距离年线距离',
            '短线均线乖离度',  '中线均线乖离度', '长线均线乖离度',
            'a股流通市值','所属概念', '所属行业', '技术形态', 
          ]

stockKeyWords = [
    ['D','Date','日期'],

    ['SN','stockName','股票名称'],
    ['ID','stockID','股票代码'],
    ['OP','OpenPrice','开盘价'],
    ['CP','ClosePrice','收盘价'],
    ['CPL','ClosePriceLast','昨日收盘价'],

    ['HP','HighestPrice','最高价'],
    ['LP','LowestPrice','最低价'],
    ['V','Volume','成交量(股)'],
    ['T','Turnover','成交额(元)'],
    ['VR','VolumeRatio','量比'],
    ['ZDF','Quote change','涨跌幅(%)'],
    ['TD','Trading Days','上市天数'],

    ['M5','MA5','5日均线'],
    ['M10','MA10','10日均线'],
    ['M20','MA20','20日均线'],
    ['M30','MA30','30日均线'],
    ['M60','MA60','60日均线'],
    ['M120','MA120','120日均线'],
    ['M240','MA240','240日均线'],

    ['BU','BOLL UP','BOLL上轨'],
    ['BM','BOLL Middle','BOLL中轨'],
    ['BD','BOLL Down','BOLL下轨'],

]

def validate():
    pass

if __name__ == "__main__":
    validate()