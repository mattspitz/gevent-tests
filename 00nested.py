from gevent import Greenlet, monkey
monkey.patch_all()

import random
import time

NUM_PARENTS=5
NUM_CHILDREN=3

def main():
    greenlets = []
    for i in xrange(NUM_PARENTS):
        greenlets.append(Greenlet.spawn(parent, i))
    for greenlet in greenlets: greenlet.join()

def parent(my_id):
    print "parent start", my_id
    time.sleep(random.random())
    greenlets = []
    for i in xrange(NUM_CHILDREN):
        greenlets.append(Greenlet.spawn(child, my_id, i))
    for greenlet in greenlets: greenlet.join()
    print "parent end", my_id

def child(parent_id, child_id):
    print "\tchild start", parent_id, child_id
    time.sleep(random.random())
    print "\tchild end", parent_id, child_id

if __name__ == "__main__":
    main()
