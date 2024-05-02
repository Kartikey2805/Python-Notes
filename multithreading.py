import threading
import time

x = 0

def Task():
    global x

    for _ in range(1000000):
        x += 1
    # time taken by this task    
    time.sleep(5)

def main():
    global x
    x = 0
    t1 = threading.Thread(target=Task)
    t2 = threading.Thread(target=Task)
    
    s = time.time()

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    # Task()
    # Task()

    e = time.time()
    
    print(x)
    print(e-s)

for _ in range(10):
    main()