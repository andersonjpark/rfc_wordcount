from profile_singlethread import execution_f, print_dict, writeDict
import time
import sys

givenDir = sys.argv[1]

start = time.time()
cleanDict = execution_f(givenDir)
# cleanDict = execution_f('/Users/jspark971/Documents/project&papers/hrl/maildir/dasovich-j/')

# Prints the dictionary as standard output
# print_dict(cleanDict)

print(str(time.time() - start) + ' has passed to finish')