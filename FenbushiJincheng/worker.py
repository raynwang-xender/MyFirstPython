
import time, sys, queue ,math
from multiprocessing.managers import BaseManager
# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass
# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# 连接到服务器，也就是运行master.py的机器:
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=('127.0.0.1' ,9999), authkey=b'python')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        r = task.get(timeout=10)
        print('运行 PI * %s * %s...' % (r, r))
        r = 'PI * %s * %s = %s' % (r, r ,math.pi * r * r)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('任务队列为空.')

    # 处理结束:
print('worker退出.')