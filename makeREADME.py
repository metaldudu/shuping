#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# 读取当前目录生成README.md

import os
import sys
import datetime
from pypinyin import lazy_pinyin

f = open('README.md','w',encoding='utf-8')
f.write('# 书评和笔记\n') # 页面H1
files = os.listdir(os.getcwd())
files.sort()

for i in files:
    subpath = os.path.join(os.getcwd(),i)
    if (i[0] == '.'):
        pass #排除隐藏目录
    elif os.path.isdir(subpath):
        f.write('\n\n## ' + i + '\n\n') #文件夹做为二级标题
        f.write('|   |   |   |\n|---|---|---|\n|')
        subfiles = os.listdir(subpath)
        subfiles.sort(key=lambda char: lazy_pinyin(char)[0][0]) # 实现中文排序
        l = 1 #计数器
        outstr = '' # 输出表格部分
        for j in subfiles:
            if j != 'README.md':
                if j != 'makeREADME.py':
                    link = '[' + j.replace('.md', '') + '](' + i + '/' + j + ')'
                    if l % 4 == 0:
                        outstr = outstr + link + '|\n|' # 倍数换行
                    else:
                        outstr = outstr + link + '|'
                    l = l + 1    

        f.write(outstr)
print ('done!')

f.write('\n\n--- \n\nUPDATE: ' + str(datetime.date.today()))
f.close()
