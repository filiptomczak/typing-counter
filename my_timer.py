import time 

class Timer:

    def __init__(self):
        self.start = time.time()
        self.stop = time.time()

    def start_time(self):
        self.start = time.time()

    def stop_time(self):
        self.stop = time.time()
        length = self.stop - self.start
        print(length)
        return length

