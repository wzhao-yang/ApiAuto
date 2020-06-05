# coding = utf-8
import configparser
import os
import sys

base_path = os.getcwd()
sys.path.append(base_path)

"""
获取配置文件方法，便于管理
"""


class HandleInit:
    # 定义load方法，加载文件
    def load_ini(self):
        file_path = "../Config/server.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding='utf-8-sig')
        return cf

    # 获取ini里的value值
    def get_value(self, key, node=None):

        if node is None:
            node = 'server'
        # print(node)
        cf = self.load_ini()
        try:
            data = cf.get(node, key)
        except Exception:
            print("没有找到数据")
            data = None
        # data = cf.get(node, key)
        return data


handle_ini = HandleInit()

if __name__ == '__main__':
    hi = HandleInit()
    print("测试获取host得值：", hi.get_value("host"))
