import threading
import time

def download():

    print("Downloading...")
    time.sleep(5)

    print("Download Complete")

thread = threading.Thread(
    target=download
)

thread.start()

print("Main Program Running")