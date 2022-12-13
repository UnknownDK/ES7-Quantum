

dir = 'C:/Users/tardi/Desktop/ES7-Quantum/'

gitlink = "https://github.com/UnknownDK/ES7-Quantum/"
# Folder:
# https://github.com/UnknownDK/ES7-Quantum/tree/master/qiskitCode
# File:
# https://github.com/UnknownDK/ES7-Quantum/blob/master/qiskitCode/measure00000.py
import os
import re

def list_files(startpath):
    print("\dirtree{%")
    for root, dirs, files in os.walk(startpath):
        if ".git" not in root:
            level = root.replace(startpath, '').count(os.sep) + 1
            if os.path.basename(root) != "":
                level += 1
            indent = ' ' * 4 * (level)
            print('.' + str(level) + ' \href{' + gitlink + 'tree/master/' + os.path.basename(root) + '}{' + os.path.basename(root) + '/}.' )
            #print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                #print('.{} {}'.format(level + 1, f))
                folders = re.split(r' |/|\\', root)
                for fold in reversed(folders):
                    if fold in dir:
                        del(folders[folders.index(fold)])
                folderpath = ""
                for folder in folders:
                    folderpath += folder + "/"
                #print(folderpath)
                print('.' + str(level + 1) + ' \href{' + gitlink + 'blob/master/' + folderpath + f + '}{' + f + '/}.' )
                #print('{}{}'.format(subindent, f))
    print("}")
list_files(dir)