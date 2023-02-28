"""
------------------------------------------
@File       : example.py
@CreatedOn  : 2023/2/28 10:31
------------------------------------------
"""
from list_file import file_filter


def demo():
    test_path = './'
    depth = 0  # 当前目录
    suffix = ".py"  # 搜索后缀为".py"的文件
    key_str = '_'  # 并且路径中包含'_'

    for j in file_filter(test_path, depth=depth):
        print(j)


if __name__ == "__main__":
    demo()
