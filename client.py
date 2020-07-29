
from apscheduler.schedulers.background import BackgroundScheduler
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




if __name__ == '__main__':
    key = ''
    # #创建一个魔眼板对象
    # my_moyan = moyan()
    # my_moyan.create_dianqipack(*dq_data)
    # my_moyan.create_dianhupack(*dq_data)
    # my_moyan.create_envpack(*env_data)
    # my_moyan.connect()

    #批量创建魔眼板对象和定时程序
    namelist = ['my_moyan1','my_moyan2','my_moyan3','my_moyan4','my_moyan5','my_moyan6','my_moyan7','my_moyan8','my_moyan9','my_moyan10','my_moyan11','my_moyan12','my_moyan13','my_moyan14']
    schlist = ['scheduler1','scheduler2','scheduler3','scheduler4','scheduler5','scheduler6','scheduler7','scheduler8','scheduler9','scheduler10','scheduler11','scheduler12','scheduler13','scheduler14']
    for i in range(len(namelist)):
        cmd = '%s = moyan()'%namelist[i]
        exec(cmd)
        eval(namelist[i]).create_dianqipack(*dq_data)
        eval(namelist[i]).create_dianhupack(*dh_data)
        eval(namelist[i]).create_envpack(*env_data)
        print(eval(namelist[i]).return_dianhupack())

        eval(namelist[i]).connect()
        cmd2 = '%s = BackgroundScheduler()' % schlist[i]
        exec(cmd2)
        eval(schlist[i]).add_job(eval(namelist[i]).Send_dianhu,'interval',seconds = 30)
        eval(schlist[i]).add_job(eval(namelist[i]).Send_env, 'interval', seconds=30)
        eval(schlist[i]).start()
    # #创建后台处理的scheduler
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(my_moyan.Send_dianhu,'interval',seconds = 3)
    # scheduler.add_job(my_moyan.Send_env,'interval',seconds = 3)
    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     pass
    while True:
        input('success')
        eval(namelist[1]).Send_dianqi()

