import glob

filepath = "C:\\sample\\label.eng\\utter\\*.aup"
files = glob.glob(filepath)

labels = ['title="opn"','title="inq"','title="que"','title="ans"','title="clo"','title="reg"','title="conf"']

sum = []

for filename in files:  
            
    #ファイル単体のラベル数をラベルごとに表示
        with open(filename, encoding='utf-8') as f:
            
            lines = f.read()

            
            print('----------------------------------------------------------------------------')
            print('File:' + filename)
            print()
            print (labels[0] + ',' + str(lines.count(labels[0])))
            print (labels[1] + ',' + str(lines.count(labels[1])))
            print (labels[2] + ',' + str(lines.count(labels[2])))
            print (labels[3] + ',' + str(lines.count(labels[3])))
            print (labels[4] + ',' + str(lines.count(labels[4])))
            print (labels[5] + ',' + str(lines.count(labels[5])))
            print (labels[6] + ',' + str(lines.count(labels[6])))

    
    #初回実行時のみリストsumに個数を入れる。2回目以降は加算
            if len(sum) == 0:
            
                sum.append(int(lines.count(labels[0])))
                sum.append(int(lines.count(labels[1])))
                sum.append(int(lines.count(labels[2])))
                sum.append(int(lines.count(labels[3])))
                sum.append(int(lines.count(labels[4])))
                sum.append(int(lines.count(labels[5])))
                sum.append(int(lines.count(labels[6])))
                opn = sum[0]
                inq = sum[1]
                que = sum[2]
                ans = sum[3]
                clo = sum[4]
                reg = sum[5]
                conf = sum[6]
            
            else:
                
                opn = opn + int(lines.count(labels[0]))
                inq = inq + int(lines.count(labels[1]))
                que = que + int(lines.count(labels[2]))
                ans = ans + int(lines.count(labels[3]))
                clo = clo + int(lines.count(labels[4]))
                reg = reg + int(lines.count(labels[5]))
                conf = conf + int(lines.count(labels[6]))

print('----------------------------------------------------------------------------')
print('Summary(' + str(len(glob.glob(filepath))) + '):')
print()                
print (labels[0] + ',' + str(opn))
print (labels[1] + ',' + str(inq))
print (labels[2] + ',' + str(que))
print (labels[3] + ',' + str(ans))
print (labels[4] + ',' + str(clo))
print (labels[5] + ',' + str(reg))
print (labels[6] + ',' + str(conf))