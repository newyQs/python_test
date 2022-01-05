"""

"""
import os


def target_path(s_path):
    """
    这个函数接收文件夹的名称作为输入参数
     返回该文件夹中文件的路径
     及其包含文件夹中文件的路径
    """
    # 枚举目录中的子目录
    for s_child in os.listdir(s_path):
        # 拼接成新目录名
        s_child_path = os.path.join(s_path, s_child)
        # 如果是目录
        if os.path.isdir(s_child_path):
            # 递归枚举
            target_path(s_child_path)
        else:
            # 否则打印文件路径
            print(s_child_path)


if __name__ == '__main__':
    target_path('.')
