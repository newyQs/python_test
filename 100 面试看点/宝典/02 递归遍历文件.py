def print_directory_contents(sPath):
    '''
    这个函数接收文件夹的名称作为输入参数
    返回该文件夹中文件的路径
    及其包含文件夹中文件的路径
    :param sPath:
    :return:
    '''
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


if __name__ == '__main__':
    print_directory_contents('.')
