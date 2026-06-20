import threading 
import time
def num():

 for i in range(1,11):
    print(i)

thread = threading.Thread(
    target=num
)

thread.start()
thread.join()
