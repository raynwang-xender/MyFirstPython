

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口, 设置验证码'python':
manager = QueueManager(address=('127.0.0.1', 9999), authkey=b'python')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    r = random.randint(8, 10000)
    print('任务放入队列：r=%s' % r)
    task.put(r)

print('从result队列获取结果....')
for i in range(10):
    # 通过队列上面的get方法获取，同时设置超时时间为10秒
    r = result.get(timeout=20)
    print('面积: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master退出')