from gevent import Greenlet, monkey, pool
monkey.patch_all()

import random
import time

NUM_PARENTS=5
NUM_CHILDREN=3

def main():
    my_pool = pool.Pool()
    for i in xrange(NUM_PARENTS):
        my_pool.start(Greenlet(parent, i))
    my_pool.join()

def parent(my_id):
    print "parent start", my_id
    my_pool = pool.Pool()
    time.sleep(random.random())
    for i in xrange(NUM_CHILDREN):
        my_pool.start(Greenlet(child, my_id, i))
    my_pool.join()
    print "parent end", my_id

def child(parent_id, child_id):
    print "\tchild start", parent_id, child_id
    time.sleep(random.random())
    print "\tchild end", parent_id, child_id

if __name__ == "__main__":
    main()
