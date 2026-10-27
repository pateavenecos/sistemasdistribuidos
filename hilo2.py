import threading
import time

threads = []

def coder():
    for k in range(5):
        print ('Coders:'+str(k))
        threads.append(k)
        time.sleep(1)
    return

def printAsteristics():
    for i in range(10):
        print ('*')
        time.sleep(2)
    return

#execute theread -----------------------
t1 = threading.Thread(target=coder)
t2=threading.Thread(target=printAsteristics)
t1.start()
t2.start()