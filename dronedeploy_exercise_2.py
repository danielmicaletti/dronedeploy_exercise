# Implement the 3 functions belows so the code executes and produces the expected output.
# Do not include any other imports.
# Do not use any Python built-in functions like.
# Is guarenteed to execute to completion.

import time
import random

## YOUR CODE ONLY BELOW HERE
# 1. Implement this function
def enum(iterator):
    # Iterate Object(s) from stream yeilding index and item
    for index, item in enumerate(iterator):
        yield index, item

# 2. Implement this function (a generator)
def stream_objects():
    # Create Generator with Object. Stream Object(s) while True
    while True:
        yield Object()
    
# 3. Implement this function
def timetaken(func):
    #Runtime of func by setting start time, running func and subtracting end time 
    def inner_func(*args, **kwargs):
        start_run = time.time()
        output = func(*args, **kwargs)
        end_run = time.time()
        #print "Time {}".format(end_run-start_run)
        return output
    return inner_func

## YOUR CODE ONLY ABOVE HERE


## DO NOT MODIFY ANYTHING BELOW HERE
class Object():
    def __init__(self):
        self.complete = random.random() < 0.2

    def is_complete(self):
        return self.complete

@timetaken
def run():
    for index, current in enum(stream_objects()):
        if current.is_complete():
            return index

print 'Expected output:'
print "Run function took # seconds."
print 'Final object was at index #.'

print 'Actual output:'
final_index = run()
print 'Final object was at index {}'.format(final_index)