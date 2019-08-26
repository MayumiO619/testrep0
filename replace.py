#import sys

#args = sys.argv

#print(args[0])
#print(args[1])
#print(args[2])

import sys

args = sys.argv

with open(args[1], encoding='utf-8') as f:

    with open(args[1] + '_edited', 'w', encoding='utf-8')as f2:

        line = f.readline()
    
        while line:

            f2.write(line.replace(' ', '').replace('<s>', '').replace('<sp>', '、').replace('</s>', '。'))
            line = f.readline()
