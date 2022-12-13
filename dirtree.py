

dir = 'C:/Users/tardi/Desktop/ES7-Quantum/'


import os

def list_files(startpath):
    print("\dirtree{%")
    for root, dirs, files in os.walk(startpath):
        if ".git" not in root:
            level = root.replace(startpath, '').count(os.sep) + 1
            if os.path.basename(root) != "":
                level += 1
            indent = ' ' * 4 * (level)
            print('{} {}/'.format(level, os.path.basename(root)))
            #print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{} {}'.format(level + 1, f))
                #print('{}{}'.format(subindent, f))
list_files(dir)