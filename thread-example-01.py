#!/usr/bin/python
#encoding: utf-8

import time
import threading

#just a start counter to measure performance
start = time.perf_counter()

# method to be called for each thread execution
def do_something(s):
	print(f'Sleeping {s} second(s)...')
	time.sleep(s)
	print('Done Sleeping...')

# list to taking all threads reference 
threads = []

# loop to start the threads and append in list above
for _ in range(100):
	t = threading.Thread(target=do_something,args=[5])
	t.start()
	threads.append(t)

# the join method is to including each thread as relevant to main-flow execution
# if you comment this code block, the performance counter will go to 0 
for thread in threads:
	thread.join()

# performance counter ending measure
stop = time.perf_counter()
print(f'Finished in {round(stop-start,2)} second(s)')
