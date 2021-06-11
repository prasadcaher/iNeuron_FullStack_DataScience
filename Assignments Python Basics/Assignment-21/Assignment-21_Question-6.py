import multiprocessing
import random
from datetime import datetime
from time import sleep

def time_check(seconds):
    sleep(seconds)
    print(f"Wait: {seconds} seconds, Current Time : {datetime.utcnow()}")


if __name__ == '__main__':
    for i in range(3):
        seconds = random.randrange(1,5)
        process = multiprocessing.Process(target=time_check, args=(seconds,))
        process.start()

