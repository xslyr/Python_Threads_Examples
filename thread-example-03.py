#!/usr/bin/python
#encoding: utf-8

import time
import concurrent.futures

#just a start counter to measure performance
start = time.perf_counter()

# method to be called for each thread execution
def do_something(s):
	init_exec = time.perf_counter()
	print(f'Sleeping {s} second...')
	time.sleep(s)
	return time.perf_counter() - init_exec
	

# here we have ThreadPoolExecutor receiving some iterator parameter
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
	secs = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
	results = [executor.submit(do_something, sec) for sec in secs]
	
	# for each thread completed print your return 
	for f in concurrent.futures.as_completed(results):
		print('Done Sleeping in {} seconds '.format(f.result()))

# performance counter ending measure
stop = time.perf_counter()
print(f'Finished in {round(stop-start,2)} second(s)')

