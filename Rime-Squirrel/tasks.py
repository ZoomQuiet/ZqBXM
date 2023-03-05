# -*- coding: utf-8 -*-
'''invoke support Rime-Squirrel ZqBXM code manager
'''

__version__ = 'zbxm v.230232.1842'
__author__ = 'Zoom.Quiet'
__license__ = 'MIT@2023'

import os
import sys
import time
import itertools

from pprint import pprint as pp
#pp = pprint.PrettyPrinter(indent=4)

from invoke import task
#from loguru import logger as LOG
#from icecream import install
#install()
#ic.configureOutput(prefix='ic|>')
import pytomlpp as tlib

ROOT = os.path.split(os.path.realpath(__file__))[0]#os.getcwd()#sys.path[0]#os.path.realpath( __file__ )
ORIG = f"{ROOT}/bxm.qim.txt"
AIMP = os.path.expanduser("~/Library/Rime/")
TEMY = f"{ROOT}/bxm4mac.dict.yaml"
AIMY = f"{AIMP}/bxm4zq2mac.dict.yaml"

TOML = f"{ROOT}/bxm.qim.toml"

@task
def ver(c):
    '''echo crt. verions
    '''
    #division_by_zero = 1 / 0
    print('\n ~> powded by {} <~'.format(__version__))


#   support stuff func.
def cd(c, path2, echo=True):
    os.chdir(path2)
    if echo:
        print('\n\t crt. PATH ===')
        c.run('pwd')
        c.run('echo \n')

BXMC = "abcdefghijklmnopqrstuvwxyz"

@task
def init2(c):
    print(f"init from\n\t{ORIG};\nAIM->\t{AIMP}")
    print(f"{AIMP} exists?\n\t",os.path.exists(f"{AIMP}"))
    _gbxm = {}

    def generate_strings(length, prefix=''):
        if length == 0:
            return
        for c in BXMC:
            key = prefix + c
            print(key)
            _gbxm[key] = []
            generate_strings(length-1, key)

    #BXMC = 'abcdefghijklmnopqrstuvwxyz'
    generate_strings(2)
    #pp(_gbxm)
    print(f"gen. all BXM code as {len(_gbxm.keys())}")
    #tlib.dump(_gbxm,open(TOML,'w'))
    return None

@task
def init(c):
    '''$ inv init => auto re-built all BXM code-database
    根据 BXM 的组码规律, 事先生成所有可能/合法的键码,以便以有序dict 的形式进行统一管理
    '''
    print(f"init from\n\t{ORIG};\nAIM->\t{AIMP}")
    print(f"{AIMP} exists?\n\t",os.path.exists(f"{AIMP}"))
    _gbxm = {}

    for c1 in BXMC:#[:4]:
        print(c1)
        _gbxm[c1] = []
        for c2 in BXMC:#[:4]:
            print(f"{c1}{c2}")
            _gbxm[f"{c1}{c2}"] = []
            for c3 in BXMC:#[:4]:
                print(f"{c1}{c2}{c3}")
                _gbxm[f"{c1}{c2}{c3}"] = []
                for c4 in BXMC:#[:4]:
                    print(f"{c1}{c2}{c3}{c4}")
                    _gbxm[f"{c1}{c2}{c3}{c4}"] = []
    #pp(_gbxm)
    print(f"gen. all BXM code as {len(_gbxm.keys())}")
    tlib.dump(_gbxm,open(TOML,'w'))
    return None


@task
def revert(c, orig=ORIG):
    '''$ inv revert => base {ORIG} reload all BXM code into .toml
    '''
    _gbxm = tlib.load(TOML,'r')
    with open(orig,'r') as _orig:
        loop = 100
        for code in _orig:
            #loop -= 1
            #if loop <=0: break
            if "#" == code[0]:
                continue
            #print(code[:-1].split())
            _c,_w = code[:-1].split()
            if _w in _gbxm[_c]:
                pass
            else:
                _gbxm[_c].append(_w)
            print("reverted",_c,_w)
    #return None
    print(f"{code} -> {_gbxm['btl']}")
    tlib.dump(_gbxm,open(TOML,'w'))

    return None


@task
def seek(c, code):
    '''$ inv seek btl => base BXM code seek Word/s
    '''
    _gbxm = tlib.load(TOML,'r')
    print(f"{code} -> {_gbxm[code]}")

    return None


@task
def find(c, word):
    '''$ inv find "是也乎" => base BXM exp. words seek code
    '''
    _gbxm = tlib.load(TOML,'r')

    for code in _gbxm:
        if word in _gbxm[code]:
            print("as code:",code)
            return True
            break

    return False



@task
def upd(c, code, word):
    '''$ inv upd btlx "是也乎哉" => update/insert code-word into .toml
    '''
    _gbxm = tlib.load(TOML,'r')

    if find(c, word):
        if word in _gbxm[code]:
            print(f"{code} HAD defined as {word}, ignore now...")
            return None
        else:
            print("INSERT new word in SAME code")
    else:
        print("INSERT BXM code")
    #_gbxm[code].append(word)
    _gbxm[code].insert(0,word)
    #seek(c, code)
    print(f"{code} -> {_gbxm[code]}")

    tlib.dump(_gbxm,open(TOML,'w'))
    return None


@task
def dele(c, code, word):
    '''$ inv dele btlx "是也乎哉" => DELETE code-word and update .toml
    '''
    _gbxm = tlib.load(TOML,'r')
    #pp(_gbxm[code])
    _gbxm[code].remove(word)
    #pp(_gbxm[code])
    #return None
    tlib.dump(_gbxm,open(TOML,'w'))
    return None


@task
def gen(c, ):
    '''$ inv gen => re-GEN. ~/Library/Rime/ need new code-table
    是也乎哉　增删改查　
    '''
    _now = time.strftime("%y%m%d.%H%M%S", time.localtime(int(time.time())))
    exp = "# Rime dictionary\n"
    exp += "# encoding: utf-8\n\n"
    exp += "---\n"
    exp += "name: bxm4zq2mac\n"
    exp += f'version: "v.{_now}"\n'
    exp += "sort: original\n"
    exp += "...\n\n"

    print(exp)

    _gbxm = tlib.load(TOML,'r')
    _totl = 0
    for c in _gbxm:
        if len(_gbxm[c]) > 0:
            _totl +=len(_gbxm[c])
            #print(c,_gbxm[c],len(_gbxm[c]))
            for word in _gbxm[c]:
                exp += f"{word}\t{c}\n"

    print(f"eport into:{AIMY}\n\t need re-built BXM in Rime/Squirrel")
    open(AIMY,'w').write(exp)
    print(f"transformed {_totl} BXM codes")
    print(f"PS:\n\t .toml include {len(_gbxm)} BXM code points")
    return None
































