# coding=utf-8
'''
@Date: 2020-05-03 14:21:10
@LastEditTime: 2020-05-03 14:45:53
@Author: yuchonghuang@sina.cn
'''

import logging
import datetime

now = datetime.datetime.now()
LOG_PATH = '/tmp'
LOG_STOCK_COMMON = '%s/butterfly_common_%04d%02d%02d_%02d%02d%02d.log'%(LOG_PATH,now.year,now.month,now.day,now.hour,now.minute,now.second)
LOG_STOCK_FILTER = '%s/butterfly_stockFilter_%04d%02d%02d_%02d%02d%02d.log'%(LOG_PATH,now.year,now.month,now.day,now.hour,now.minute,now.second)

allLogFiles = {
    LOG_STOCK_COMMON:None,
    LOG_STOCK_FILTER:None,
}

def INFO_LOG(msg):
    msg_console = "\033[0;32;40m%s\033[0m"%(msg)
    print(msg_console)

    logger = logging.getLogger('logfile')
    logger.info(msg)

def DEBUG_LOG(msg):
    msg_console = "\033[0;32;40m%s\033[0m"%(msg)
    print(msg_console)

    logger = logging.getLogger('logfile')
    logger.debug(msg)

def WARNING_LOG(msg):
    msg_console = "\033[0;33;40m%s\033[0m"%(msg)
    print(msg_console)

    logger = logging.getLogger('logfile')
    logger.warning(msg)


def ERROR_LOG(msg):
    msg_console = "\033[0;37;41m%s\033[0m"%(msg)
    print(msg_console)

    logger = logging.getLogger('logfile')
    logger.error(msg)


def CRITICAL_LOG(msg):
    msg_console = "\033[0;37;41m%s\033[0m"%(msg)
    print(msg_console)

    logger = logging.getLogger('logfile')
    logger.critical(msg)


def ConfigLogWithFile(key):
    if key not in allLogFiles:
        return
    
    if allLogFiles[key] is not None:
        return

    # init file 
    
    logger = logging.getLogger('logfile')
    logger.setLevel('DEBUG')
    
    BASIC_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(filename=key, filemode='w',format=BASIC_FORMAT,datefmt=DATE_FORMAT)
    allLogFiles[key] = logger

def ConfigLog(key):
    ConfigLogWithFile(key)

if __name__ == '__main__':
    ConfigLog(LOG_STOCK_COMMON)
    DEBUG_LOG("this is debug info")
    INFO_LOG("this is info info")
    WARNING_LOG("this is warning info")
    ERROR_LOG("this is error info")
    CRITICAL_LOG("this is critical info")

