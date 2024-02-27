import os
import shutil


# 创建指定文件夹
def create_dir(path):
    if os.path.exists(path) is False:
        os.makedirs(path)


# 创建指定文件夹 如果目录存在则清空
def empty_and_create_dir(path):
    if os.path.exists(path) is False:
        os.makedirs(path)
    else:
        shutil.rmtree(path)
        os.makedirs(path)
