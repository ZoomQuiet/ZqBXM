# -*- coding: utf-8 -*-
#!/usr/bin/python
#
'''for MAC rimeIME Squirrel reformat QIM table 
'''
import sys
#import traceback

VER = "fix2Squirrel4BXM {v12.12.1}"

def reformat(qimf):
    print qimf
    totlel = 0
    exp = ""
    for l in open(qimf):
        totlel += 1
        if "#" in l:
            print l[:-1]
        else:
            d = l.split()
            #print d
            exp += "%s\t%s\n"%(d[1], d[0])

    print "\t 共处理:%d 行" % totlel
    print ">>>输出为: bxm_zq4mac.dict.yaml"
    open("bxm_zq4mac.dict.yaml", 'w').write(exp)

if __name__ == '__main__':      # this way the module can be
    if 2 != len(sys.argv):
        print """ %s usage::
fix2Squirrel4BXM.py path/2/qim.txt
        """ % VER
    else:
        QIM = sys.argv[1]
        reformat(QIM)


