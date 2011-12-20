#!/usr/bin/python
'''for MAC SCIM .inputplugin appended BXM
- 111220 change data str. usage list only
- 111219 inti.
'''
import traceback
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

'''
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
