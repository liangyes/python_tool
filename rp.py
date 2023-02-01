import os
import shutil
file = r'E:\www\xyx\mohanh5\素材\20221212\新素材'


for root, dirs, files in os.walk(file):
    if root != file:
        break
    for file in files:
        path = os.path.join(root, file)
        if file:
           print(path)
           print("新文件")
           #print(file)
           #遍历目录文件
           file_1 = r'D:\phpstudy_pro\WWW\xiaobing'

           for root_1, dirs_1, files_1 in os.walk(file_1):
               for file_1 in files_1:
                   path_1 = os.path.join(root_1, file_1)
                   if file_1==file:
                      print(path_1)
                      print(root_1)
                      shutil.copy(path,root_1)
                      print("结束")