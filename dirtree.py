import os
import re

dir = 'C:/Users/tardi/Desktop/ES7-Quantum/'

gitlink = "https://github.com/UnknownDK/ES7-Quantum/"


def list_files(startpath):
    print("\dirtree{%")
    for root, dirs, files in os.walk(startpath):
        if ".git" not in root:
            level = root.replace(startpath, '').count(os.sep) + 1
            if os.path.basename(root) != "":
                level += 1
            folders = re.split(r' |/|\\', root)
            for fold in reversed(folders):
                if fold in dir:
                    del(folders[folders.index(fold)])
            folderpath = ""
            for folder in folders:
                folderpath += folder + "/"
            print('.' + str(level) + ' \href{' + gitlink + 'tree/master/' + folderpath + '}{' + os.path.basename(root) + '/}.' )
            for f in files:
                print('.' + str(level + 1) + ' \href{' + gitlink + 'blob/master/' + folderpath + f + '}{' + f + '}.' )
    print("}")
list_files(dir)