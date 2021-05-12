#!/usr/bin/python
#encoding: utf-8

import time
import concurrent.futures

#just a start counter to measure performance
start = time.perf_counter()

# method to be called for each thread execution
def do_something(s):
	print(f'Sleeping {s} second...')
	time.sleep(s)
	print('Done Sleeping...')

# thread start with ThreadPoolExecutor and some generator expression to create a list results
# ThreadPoolExecutor is good to you limit the number of threads in execution same time
# the default max_workers number is 5 * CPU cores and the 'join' of example 1 is not necessary
with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
	results = [executor.submit(do_something, 5) for _ in range(100)]

# performance counter ending measure
stop = time.perf_counter()
print(f'Finished in {round(stop-start,2)} second(s)')

