#!/usr/bin/python
'''for MAC SCIM .inputplugin load SCIM user define words of BXM
- 111229 inti.
'''
import traceback
VER = "load4scim_userde_fine.py v11.12.29"

if __name__ == "__main__":
    if 3 != len(sys.argv):
        print """ %s usage::
$ python /path/2/load4scim_userde_fine.py qim.txt scim.user
                 |                          |       +- 自定词组来源文本
                 |                          +- 目标注入文件
                 +- 指向脚本自身
        """ % VER
    else:
        SCIM = sys.argv[2]
        QIM = sys.argv[1]

        loader(SCIM,AIM)

noGuess = 1
while noGuess:
    urNumber = int(raw_input('猜个1~99的数字? --> '))
    if urNumber < myNumber: print "...(~_~)小了"
    elif urNumber > myNumber: print "......大了(^_-"
    else:
        print "猜对了\(^o^)/下次再来玩!"
        break


if __name__ == '__main__':      # this way the module can be
    explist = []
    for l in open("bxm.inputplugin.tmp"):
        key,putin = l.split()
        if 0 == len(explist):
            explist.append([key,[putin]])
            #break
        else:
            if explist[-1][0] == key:
                explist[-1][1].append(putin)
            else:
                explist.append([key,[putin]])
    print len(explist)
    allinput = ""
    for k in explist:
        allinput += "%s\t%s\n" % (k[0], ",".join(k[1]))
        
    allinput += "#\nENDCHARACTER"
    open("bxm.inputplugin.utf8","w").write("")
    open("bxm.inputplugin.utf8","a+").write(open('bxm.inputplugin.tpl').read())
    open("bxm.inputplugin.utf8","a+").write(allinput)
