# coding=utf-8
'''
@Date: 2020-04-26 22:46:33
@LastEditTime: 2020-05-03 14:59:40
@Author: yuchonghuang@sina.cn
'''

from log import ConfigLog, INFO_LOG, ERROR_LOG,LOG_STOCK_COMMON


if __name__ == "__main__":
    ConfigLog(LOG_STOCK_COMMON)
    INFO_LOG('hello world')