import re
import glob

filepath = "C:\\sample\\label.eng\\utter\\*.aup"
files = glob.glob(filepath)

for filename in files:

#ここから①②③
#①トラック名を定義
    labeltrackname = ('labeltrack name="N-both-scene"',\
                      'labeltrack name="B-ope-label"',\
                      'labeltrack name="B-cus-label"')

    f = open(filename, encoding='utf-8')
    
    line = f.readline()


    while line:

    #labeltrack name="（トラック名）"を含む行を抽出
        match = re.search('labeltrack name="(.*?)"', line)

        if match != None:

    #定義したトラック名いずれにもマッチしない場合、
    #Invalid labeltrack name="（誤トラック名）"in file（対象ファイル名）

            if match.group() not in labeltrackname:
                print("トラック名に誤りがあります。" + "Invalid " + match.group() + "in file" + filename)

        line = f.readline()
    
#②トラック名を定義
    title = ('title="opn"',\
             'title="inq"',\
             'title="que"',\
             'title="ans"',\
             'title="clo"',\
             'title="conf"',\
             'title="reg"')

    f = open(filename, encoding='utf-8')

    
    line = f.readline()

    while line:

#labeltrack name="（トラック名）"を含む行を抽出
        match = re.search('title="(.*?)"', line)


        if match != None:

#定義したトラック名いずれにもマッチしない場合、
#Invalid title="（誤トラック名）"in file（対象ファイル名）

            if match.group() not in title:
                print("ラベル名に誤りがあります。" + "Invalid " + match.group() + "in file" + filename)

        line = f.readline()

#③ ラベル付け誤り検出

    f = open(filename, encoding='utf-8')

    
    line = f.readline()

    while line:
        match = re.search('labeltrack name="B-ope-label"', line)
    
        if match != None:
            line = f.readline()
            match2 = re.search('title="(.*?)"', line)
            
            if match2 != None:
                if match2.group() != 'title="conf"':
                    print("\"B-ope-label\"にはラベル名\"conf\"のみ設定してください。" +  "Invalid " + match2.group() + " in file" + filename)

        match3 = re.search('labeltrack name="B-cus-label"', line)
    
        if match3 != None:
            line = f.readline()
            match4 = re.search('title="(.*?)"', line)

            if match4 != None:
                if match4.group() != 'title="reg"':
                    print("\"B-cus-label\"にはラベル名\"reg\"のみ設定してください。" +  "Invalid " + match4.group() + " in file" + filename)

        line = f.readline()
        
    pass