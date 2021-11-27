import sys
import os
from os import walk
import pathlib
import shutil

if len(sys.argv) != 2:
    print(len(sys.argv))
    print('Use script.py filename(without extension)')
    sys.exit(1)

contador = 0
allpaths = []
rootdirectory = pathlib.Path(__file__).parent.resolve()
root = next(walk(rootdirectory), (None, None, []))
print(root[0])

for dir in root[1]:
    dirpath = root[0]+'\\'+dir
    archivos = next(walk(dirpath), (None, None, []))[2]
    paths = [None]*(len(archivos))
    for i in range(len(archivos)):
        if(archivos[i][-3:] == 'jpg'):
            old = dirpath + '\\' + archivos[i]
            newpath = root[0] + '\\' + str(contador).zfill(4) + '.jpg'
            paths[i] = newpath
            shutil.copy(old, newpath)
            print(old + '\n -> \t' +newpath)
            contador+=1
    allpaths = allpaths + paths

command = 'jpeg2pdf *.jpg -o \"' + sys.argv[1] + '.pdf\"'
os.system(command)

for file in allpaths:
    os.remove(file)