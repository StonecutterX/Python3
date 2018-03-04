#!/usr/bin/python3

import _thread 
import threading
import time

exitFlag = 0

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

def print_time1(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

def test1():
    try:
        _thread.start_new_thread(print_time, ("Thread-1", 2, ))
        _thread.start_new_thread(print_time, ("Thread-2", 4, ))

    except:
        print("Error: can not start thread")

    while 1:
        pass

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("start thread: " + self.name)
        print_time1(self.name, self.counter, 5)
        print("exit  thread: " + self.name)

class myThreadwithLock(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("start thread: " + self.name)
        threadLock.acquire()
        print_time1(self.name, self.counter, 5)
        threadLock.release()
    
def myThreadTest():
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("exit main thread")

def myThreadwithLockTest():
    global threadLock
    threadLock = threading.Lock()
    threads = []

    thread1 = myThreadwithLock(1, "Thread-1", 1)
    thread2 = myThreadwithLock(2, "Thread-2", 2)

    thread1.start()
    thread2.start()

    threads.append(thread1)
    threads.append(thread2)

    for t in threads:
        t.join()
        print("stopping")
    print("exit main thread")

if __name__ == '__main__':
    #test1()
    #myThreadTest()
    myThreadwithLockTest()
