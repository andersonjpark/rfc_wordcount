from mtFunctionFile import execution_f, get_file_paths, print_dict, writeDict
from ray.util.multiprocessing import Pool
import numpy as np
import collections
import sys

import time
start = time.time()

print("Given dir is " + sys.argv[1])
print("Number of thread is " + sys.argv[2])

givenDir = str(sys.argv[1])
dirPaths = get_file_paths(givenDir) # Returns list of file directory
# dirPaths = get_file_paths('/Users/jspark971/Documents/project&papers/hrl/maildir/dasovich-j/')


n = int(sys.argv[2])
split_paths = np.array_split(dirPaths, n)
counter = collections.Counter()
result_objs = []

with Pool(processes=n) as pool:
    for i in range(n):
        result = pool.apply_async(execution_f, (split_paths[i], ))
        result_objs.append(result)
    for objs in result_objs:
        counter.update(objs.get())
        print('one obj updated')
    print(str(time.time() - start) + ' has passed to finish')

