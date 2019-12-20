import threading
import time

exitFlag = 0

# """
# 创建线程
# """
# class myThread(threading.Thread):
#     def __init__(self, threadId, name, counter):
#         threading.Thread.__init__(self)
#         self.threadId = threadId
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print("开始线程{0}".format(self.name))
#         print_time(self.name,self.counter,5)
#         print("退出线程{0}".format(self.name))
#
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print("{0}:{1}".format(threadName,time.ctime(time.time())))
#         counter -= 1
#
#
# thread1 = myThread(1, "thread-1", 1)
# thread2 = myThread(1, "thread-2", 2)
#
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("exit main thread")
#


"""线程同步"""
class myThread(threading.Thread):
    def __init__(self,threadId,name,counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("start thread:{0}".format(self.name))
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        threadLock.release()



def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print("{0}:{1}".format(threadName,time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")











