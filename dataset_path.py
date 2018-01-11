# root根目录， patterns匹配文件格式， single_level是否进行目录深层次查找
import fnmatch, os
def allFiles(root, patterns = '*', single_level = False, yield_folders = False):
    patterns = patterns.split(';')
    for path, subdirs, files in os.walk(root):
        if yield_folders:
           #add subdirs to the tail of files
           files.extend(subdirs)
        files.sort()
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path, name)
                    break
        #only deal one level of the dir
        if single_level:
            break
print("datasetName: ")
for name in allFiles('/data/weixin-39265957/quiz-w8-data/', single_level = True):
    print(name)