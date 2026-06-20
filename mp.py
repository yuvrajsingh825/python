from multiprocessing import Process 
import time 

def task():
    print("Running")
    time.sleep(3)
    print("Complete")
  
if __name__ == "__main__":

    p = Process(
        target=task
    )

    p.start()
    p.join()