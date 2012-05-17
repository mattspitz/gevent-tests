from gevent import Greenlet, monkey, pool
monkey.patch_all()

import random
import time

NUM_PARENTS=5
NUM_CHILDREN=3

shared_pool = pool.Pool()
def main():
    for i in xrange(NUM_PARENTS):
        shared_pool.start(Greenlet(parent, i))
    shared_pool.join()

def parent(my_id):
    print "parent start", my_id
    time.sleep(random.random())
    for i in xrange(NUM_CHILDREN):
        shared_pool.start(Greenlet(child, my_id, i))
    print "parent end", my_id

def child(parent_id, child_id):
    print "\tchild start", parent_id, child_id
    time.sleep(random.random())
    print "\tchild end", parent_id, child_id

if __name__ == "__main__":
    main()
