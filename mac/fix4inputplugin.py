#!/usr/bin/python

if __name__ == '__main__':      # this way the module can be
    exporder = []
    expdict = {}
    loop = 0
    for l in open("bxm.inputplugin.tmp"):
        loop +=1
        if loop%1000 :
            pass
        else:
            print loop
        key,putin = l.split()
        if key in expdict.keys():
            expdict[key].append(putin)
            #pass
        else:
            exporder.append(key)
            expdict[key] = [putin]
    print len(exporder)
    print len(expdict.keys())
    allinput = ""
    for k in exporder:
        allinput += "%s\t%s\n" % (k, ",".join(expdict[k]))
    open("bxm.inputplugin.utf8","w").write(open('bxm.inputplugin.tpl').read()% locals())
'''
        if crtkey == key:
            #print key,putin
            #print "crtkey,crtput:",crtkey,crtput
            crtput.append(putin)
            print "%s\t%s"% (key,",".join(crtput))
        else:
            #print "%s\t%s"% (key,",".join(crtput))
            crtkey,crtput = key,[putin]
            pass
'''
