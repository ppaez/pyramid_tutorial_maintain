#! /usr/bin/python3

import os
import sys
import glob

if len(sys.argv) == 2:
    n=sys.argv[1]
else:
    n=''

docspath=os.path.join('docs','tutorials','wiki'+n)

lines={}
includes={}
for rstfile in glob.glob(os.path.join(docspath, '*.rst')):
    lines[rstfile]=open(rstfile).readlines()
    n=0
    line=lines[rstfile]
    while n<len(line):
        if '.. literalinclude::' in line[n]:
            srcfilepath=line[n].split()[-1]
            srcfilepath=os.path.join(*srcfilepath.split(os.sep)[1:])
            if srcfilepath not in includes:
                includes[srcfilepath]=[]
            includes[srcfilepath].append([])
            n+=1
            while '  :' in line[n]:
                if ':li' in line[n] or ':emph' in line[n] or \
                   ':end' in line[n] or ':pyobj' in line[n]:
                    includes[srcfilepath][-1].append( (n,line[n].strip()) )
                n+=1
        else:
            n+=1

stages = 'basiclayout models views authorization tests'.split()

def bystage(item):
    f, refs = item
    stage = f.split(os.sep)[0]
    return stages.index(stage)

print(len(lines), 'rst files in', docspath)
print( sum(map(len,includes.values())), 'includes for', len(includes.keys()), 'files')
print()

currstage=''
for f,refs in sorted(includes.items(), key=bystage ):
    # line on each stage
    stage = f.split(os.sep)[0]
    if stage != currstage:
        print('-'*40)
        currstage=stage

    print(len(refs), f)
    for ref in refs:
        for n, value in ref:
            print(n, value)
        print()
    
