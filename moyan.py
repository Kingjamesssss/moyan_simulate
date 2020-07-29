from ctypes import *
from struct import *
import socket
'''
连接服务器
'''
HOST = '127.0.0.1'
PORT = 8888
ADDRESS = (HOST, PORT)


'''
实现一个魔眼版类
'''
class moyan(object):
    def __init__(self):
        self.dianqi_return = []
        self.dianhu_return = []
        self.env_retrun = []
        self.Socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def create_dianqipack(self,*args):
        self.dianqi_return.append(0xaa)#数据头高位
        self.dianqi_return.append(0xbb)#数据头低位
        self.dianqi_return.append(76)#电器包长度
        self.dianqi_return.extend(args)#包括终端号总闸开关总功率单功率，15个识别数据
        self.dianqi_return.append(0xee)#结束位
        self.dianqi_return.append(0xff)

    def create_dianhupack(self,*args):
        self.dianhu_return.append(0xbb)
        self.dianhu_return.append(0xaa)
        self.dianhu_return.append(17)
        self.dianhu_return.extend(args)#包括终端号，总闸开关，总功率，单功率，电弧数据
        self.dianhu_return.append(0xee)
        self.dianhu_return.append(0xff)

    def create_envpack(self,*args):
        self.env_retrun.append(0xaa)
        self.env_retrun.append(0xcc)
        self.env_retrun.append(12)
        self.env_retrun.extend(args)#包括终端号，温度，湿度，pm2.5，噪声
        self.env_retrun.append(0xee)
        self.env_retrun.append(0xff)

    def return_dianqipack(self):
        return self.dianqi_return

    def return_dianhupack(self):
        return self.dianhu_return

    def return_envpack(self):
        return self.env_retrun

    def connect(self):
        self.Socket_client.connect(ADDRESS)

    def disconnect(self):
        self.Socket_client.close()

    '''
    发送电器识别包
    '''
    def Send_dianqi(self):
        self.Socket_client.send(pack(76 * 'B', *self.dianqi_return))
        print("dianqi success")

    '''
    发送电弧数据包
    '''
    def Send_dianhu(self):
        self.Socket_client.send(pack(17 * 'B', *self.dianhu_return))
        print("dianhu success")

    '''
    发送环境数据包
    '''
    def Send_env(self):
        self.Socket_client.send(pack(12 * 'B', *self.env_retrun))
        print("env success")

'''
float转byte
'''
def floatobyte(origin):
    m = pack('f',origin)
    byte_return = [i for i in m]
    return byte_return

'''
电弧包转换格式
'''
def dianhuchange(data):
    arr_return = []
    arr_return.extend(data[0:3])
    arr_return.extend(floatobyte(data[3]))
    arr_return.extend(floatobyte(data[4]))
    arr_return.append(data[5])
    return arr_return

'''
电器识别包数据转换
'''
def dianqichange(data):
    arr_return = []
    arr_return.extend(data[0:3])
    for i in range(3,20):
        arr_return.extend(floatobyte(data[i]))

    return arr_return;


