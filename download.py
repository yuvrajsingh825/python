# Download Manager using Threads

import threading
import time

def download_file(file_name):
    print(f"Downloading {file_name}")
    time.sleep(2)  # Simulate download time

# Create threads
t1 = threading.Thread(target=download_file, args=("file1.pdf",))
t2 = threading.Thread(target=download_file, args=("file2.pdf",))
t3 = threading.Thread(target=download_file, args=("file3.pdf",))

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()

print("Completed")