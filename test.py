from struct import *
import  math
from moyan import *
'''
电器，电弧和环境数据包数据
'''
dq_data_origin = [1,1,1,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
dh_data_origin = [2,0,0,15.2,6.7,7]
env_data_origin = [2,32,12,2,3,1,1]

#转换后变成一个一个字节的数据格式
dh_data = dianhuchange(dh_data_origin)
dq_data = dianqichange(dq_data_origin)
env_data = env_data_origin
def byte_to_float(x):
	arr = []
	y = []
    #如果x不是4的整数倍就会抛出IndexError
	for i in range(0,len(x),4):
		y = x[i:i+4]
		fo = intBitsToFloat(fourBytesToInt(y[0], y[1],y[2],y[3]))
		fo = round(fo,3)
		arr.append(fo)
#	print(arr)
	return arr
#int型转成float
def intBitsToFloat(bits):
    if (bits >> 31) & 1 == 0:
        s = 1
    else:
        s = -1
    #判断
    e = (bits >> 23) & 0xff
    if e == 0:
       m = (bits & 0x7fffff) << 1
    else:
       m = (bits & 0x7fffff) | 0x800000
    return s * m * float(math.pow(2, e-150))
#四个字节数据转int
def fourBytesToInt(b1, b2, b3, b4):
    return (b4 << 24) | (b3 << 16) | (b2 << 8) | b1

# print(byte_to_float(total))
# mm =pack('BBBB',*total)
# print(mm)
# print(unpack('BBBB',mm))
# nn = pack('f',6044.609)
# print(byte_to_float(nn))
# print(unpack('f',nn))
#
# print(unpack('f',b'\x0033sAff'))

dh_data = [0xbb,0xaa,17,2,0,0,15.2,6.7,7,0xEE,0xff]
# test = [0xbb,0xaa,5.7,6.7]
# test2 = [5.6]
# mm = pack('BBBBBBffBBB',*dh_data)
# nn = pack('BBff',*test)
#
# print(mm)
# print(nn)
#
# byte = pack('f',5.6)
# print(byte)
# byte_return = [i for i in byte]
# print(byte_return)
# a = byte_to_float(byte_return)
# print(a)
#
#
# arr_return = []
# arr_return.extend(dh_data[0:6])
# print(dh_data[6])
# arr_return.extend(floatobyte(dh_data[6]))
# arr_return.extend(floatobyte(dh_data[7]))
# arr_return.extend(dh_data[8:11])
# print(arr_return)

# test = [1,1,1,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
# b = dianqichange(test)
# print(b)
# print(len(b))





# '''
# 发送电器识别包
# '''
# def Send_dianqi(data):
#     Socket_client.send(pack(76*'B',*data.arr_return))
#     print("dianqi success")

# '''
# 发送电弧数据包
# '''
# def Send_dianhu(data):
#     Socket_client.send(pack(17*'B',*data.arr_return))
#     print("dianhu success")

# '''
# 发送环境数据包
# '''
# def Send_env(data):
#     Socket_client.send(pack(12*'B',*data.arr_return))
#     print("env success")
# '''
# 实现一个电器识别包类
# '''
#
# class dianqi(object):
#
#     arr_return = []
#     def __init__(self, *args):
#
#         self.arr_return.append(0xaa)#数据头高位
#         self.arr_return.append(0xbb)#数据头低位
#         self.arr_return.append(76)#电器包长度
#         self.arr_return.extend(args)#包括终端号总闸开关总功率单功率，15个识别数据
#         self.arr_return.append(0xee)#结束位
#         self.arr_return.append(0xff)
#     #返回数据包
#     def return_arr(self):
#         return self.arr_return

# '''
# 实现一个电弧识别包类
# '''
# class dianhu(object):
#
#     arr_return = []
#     def __init__(self, *args):
#
#         self.arr_return.append(0xbb)
#         self.arr_return.append(0xaa)
#         self.arr_return.append(17)
#         self.arr_return.extend(args)#包括终端号，总闸开关，总功率，单功率，电弧数据
#         self.arr_return.append(0xee)
#         self.arr_return.append(0xff)
#     def return_arr(self):
#
#         return self.arr_return
#
# '''
# 实现一个环境参数包类
# '''
#
# class env(object):
#
#     arr_return = []
#     def __init__(self, *args):
#
#         self.arr_return.append(0xaa)
#         self.arr_return.append(0xcc)
#         self.arr_return.append(12)
#         self.arr_return.extend(args)#包括终端号，温度，湿度，pm2.5，噪声
#         self.arr_return.append(0xee)
#         self.arr_return.append(0xff)
#     def return_pack(self):
#         return self.arr_return
# class haha(object):
#     def __init__(self,m,n):
#         self.max = m
#         self.min = n
# k = 5
# l = 1
# namelist = ['aa','bb','cc']
# for i in range(len(namelist)):
#     cmd = '%s = haha(k,l)'%namelist[i]
#     exec(cmd)
#     print(eval(namelist[i]).max)

#创建一个魔眼板对象
my_moyan = moyan()
my_moyan.create_dianqipack(*dq_data)
my_moyan.create_dianhupack(*dq_data)
my_moyan.create_envpack(*env_data)
print(my_moyan.return_dianhupack())



my_moyan2 = moyan()
my_moyan2.create_dianqipack(*dq_data)
my_moyan2.create_dianhupack(*dq_data)
my_moyan2.create_envpack(*env_data)
print(my_moyan2.return_dianhupack())