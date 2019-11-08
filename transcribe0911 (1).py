
# coding: utf-8

# In[8]:


import re
import sys
import glob
import os.path

args = sys.argv

#対象ファイルの格納フォルダパス、およびfillerリストをフルパス指定
filepath = args[1] + '\\*.tsv'
fillertxt = args[2]
files = glob.glob(filepath)

#fillerリストの読み込み（カンマ区切りのリスト形式）
with open(fillertxt, encoding='utf-8')as f:
    filler = f.read().splitlines()
    #元ファイル読み込み（1行ずつ読み込み）
    for filename in files:
        with open(filename, encoding='utf-8', newline="\n")as f: 
            row = []
            line = f.readline()
            #各対象ファイルをタブ区切り位置によって0ch,1chに分け、それぞれ別で処理を行う
            for l in line:
                row = line.split('\t')
                name, ext = os.path.splitext(filename)
                if len(row) == 4:
                    del row[:3]
                    with open(name.rstrip(name[-2:]) + '_0ch' + ext, 'a', encoding='utf-8', newline="\n") as f2:
                        #小文字化、両端の括弧、ダブルクオーテーション、シングルクオーテーション、行内のピリオド
                        #行内のカンマ、感嘆符、複合語のハイフンを消す
                        row = str(row).lower().strip("[""]""\"""\'").replace(".","").replace(",","")\
                        .replace("?","").replace("!","").replace(";","").replace("-", "" )
                        #原文からfillerを消す
                        row = str(row).split()
                        row = list(filter(lambda x: x not in filler, row))
                        #リスト⇒文字列、シングルクオーテーション置換
                        row = ' '.join(row).replace("\'","\\u0027").replace("\\n", "\n" )
                        f2.write(row)
                elif len(row) == 5:
                    del row[:4]
                    with open(name.rstrip(name[-2:]) + '_1ch' + ext, 'a', encoding='utf-8', newline="\n") as f3:
                        row = str(row).lower().strip("[""]""\"""\'").replace(".","").replace(",","")\
                        .replace("?","").replace("!","").replace(";","").replace("-", "" )
                        #原文からfillerを消す
                        row = str(row).split()
                        row = list(filter(lambda x: x not in filler, row))
                        #リスト⇒文字列、シングルクオーテーション置換
                        row = ' '.join(row).replace("\'","\\u0027").replace("\\n", "\n" )
                        f3.write(row)
                line = f.readline()
