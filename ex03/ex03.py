import threading
import time

def threadWoker():
    print("my")

    time.sleep()

    time.sleep(10)

    print("my thread is terminating")

myThread = threading.Thread(target=threadWorker)

myThread.start()

myThread.join()
print("my thread has entered a 'dead' state")

