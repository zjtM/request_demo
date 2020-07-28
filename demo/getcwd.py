import os
'''获取当前文件的绝对路径'''
def get_cwd():
    path = os.path.dirname(os.path.abspath(__file__))
    return path