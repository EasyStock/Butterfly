'''
Created on Jun 14, 2020

@author: mac
'''
from cleanFolderConfig import MOVE,DELETE,CLEAN_CONFIG
import os
import shutil

def CleanOneFolder(srcFolder, destFolder):
    newConfig = ReadConfig(srcFolder,destFolder)
    fileNames = os.listdir(srcFolder)
    for fileName in fileNames:
        key = fileNameToConfig(fileName)
        fullPath = os.path.join(srcFolder,fileName)
        if key not in newConfig:
            print(fullPath, 'do nothing!')
            continue

        config = newConfig[key]
        DoAction(fullPath,config[0],config[1])

def DoAction(srcFile,action,dest=None):
    if action == DELETE:
        DeleteFile(srcFile)
    elif action == MOVE:
        MoveFile(srcFile,dest)


def ReadConfig(srcFolder,destFolder):
    res = {}
    for key in CLEAN_CONFIG:
        config = CLEAN_CONFIG[key]
        action = config[0]
        if action == MOVE:
            dest = os.path.join(destFolder,config[1])
            if os.path.exists(dest) == False:
                os.makedirs(dest)
            res[key] = [action,dest]
        elif action == DELETE:
            res[key] = [action,None]
    return res


def MoveFile(src,dest):
    try:
        shutil.move(src,dest)
    except Exception as e:
        print(e)
    msg = 'MOVE file from %s to %s' %(src,dest)
    print(msg)

def DeleteFile(src):
    s = input('''(Y/N) Try to delete file:%s '''%(src))
    if s.upper() == 'Y':
        os.remove(src)
        msg = 'DELETE file %s ' %(src)
        print(msg)
    else:
        print('Cancel to Delete File:%s'%(src))

def fileNameToConfig(fileName):
    keys = CLEAN_CONFIG.keys()
    ext = fileName[fileName.rfind('.')+1:]
    for key in keys:
        if ext == key:
            return key
    return None

def CleanFolders(srcFolders, destFolder):
    for srcFolder in srcFolders:
        CleanOneFolder(srcFolder, destFolder)
        print('===================================================')

if __name__ == "__main__":
    #ReadConfig(srcFolder,destFolder)
    fileName = 'aaaa.wbt'
    #res = fileNameToConfig(fileName)
    #print(res)
    srcFolder = [
        '/Volumes/Data/Downloads',
        '/Volumes/Data/Desttop Of 10.12',
        '/Volumes/Data/download_10.12',
        '/Volumes/VM/FromMacBook/Downloads',
        '/Volumes/VM/FromMacBook/desktop',
        '/Volumes/VM/FromMacBook/Destop',
    ]
    destFolder = '/Volumes/Data/Files'
    CleanFolders(srcFolder,destFolder)