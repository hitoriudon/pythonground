import random
import multiprocessing
from multiprocessing import Lock
import time
def func(lock):
        lock.acquire()
        current = multiprocessing.current_process()
        print('###############Thread #' + current.name[8] + ' started...............')
        try:
                for _ in range (10):
                        start = time.process_time()
                        print('[' + current.name[8] + '] -->    ', end="    ")
                        randoms = [random.randint(0,9) for i in range(10)]
                        randoms.sort()
                        end = time.process_time()
                        for i in randoms:
                                print(i, end="    ")
                        print("[  ]", end ="   ")
                        print("%10.8f sec" %(end-start))
        finally:
                lock.release()
if __name__ == '__main__':
        lock=Lock()
        print("#"*15 + "Thread Test: START" +"."*15)
        for _ in range(2):
                p = multiprocessing.Process(target = func, args=(lock,))
                p.start()
                p.join()