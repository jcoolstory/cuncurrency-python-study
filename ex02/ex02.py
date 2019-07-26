import threading
import time
import random

counter = 1

def workerA():

    global counter

    while counter < 1000:

        counter += 1

        print("worker a is incrementing counter to {}".format(counter))

        sleepTime = random.randint(0,1)
        time.sleep(sleepTime)

def workerB():

    global counter

    while counter > -1000:
        counter -= 1
        print("worker b is decrementing counter to {}".format(counter))
        sleepTime = random.randint(0,1)
        time.sleep(sleepTime)

def main():

    t0 = time.time()

    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    t1 = time.time()

    print("execution time {}".format(t1-t0))

if __name__ == "__main__":

    main()
