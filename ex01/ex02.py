import threading
import urllib.request
import time

def downloadImage(imagePath, fileName):

    print("downloading image form ", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)
    print("completed download")

def excuteThread(i):

    imageName = "temp/image-" + str(i) + ".jpng"

    downloadImage("http://lorempixel.com/400/200/sports", imageName)

def main():

    t0 = time.time()

    threads = []

    for i in range(10):
        thread = threading.Thread(target=excuteThread, args=(i,))
        threads.append(thread)
        thread.start()

        for i in threads:
            i.join()

        t1 = time.time()
        totalTime = t1-t0
        print("total execution time {}".format(totalTime))

if __name__ == "__main__":

    main()
