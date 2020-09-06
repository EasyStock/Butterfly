'''
Created on Jun 14, 2020

@author: mac
'''


DELETE='delete'
MOVE='move'


CLEAN_CONFIG = {
    'pdf':[MOVE, 'pdf'],
    'dmg':[MOVE, 'dmg'],
    'wbt':[DELETE, ],
    'docx':[MOVE, 'docx'],
    'xlsx':[MOVE, 'xlsx'],
    'ppt':[MOVE, 'ppt'],
    'pptx':[MOVE, 'ppt'],
    'mp3':[MOVE, 'mp3'],
    'zip':[MOVE, 'zip'],
    'rar':[MOVE, 'zip'],
    'tar':[MOVE, 'zip'],
    'gz':[MOVE, 'zip'],
    '7z':[MOVE, 'zip'],
    'doc':[MOVE, 'doc'],
    'pkg':[MOVE, 'pkg'],
    'png':[MOVE, 'png'],
}