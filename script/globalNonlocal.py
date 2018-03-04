#!/usr/bin/python3
# -*- coding: utf-8

# usage about nonlocal.

gcount = 0
def global_test():
    print(gcount)

def global_counter():
    global gcount
    gcount += 1
    return gcount

def global_counter_test():
    for i in range(5):
        print(global_counter())
    global_test()
    
def globalExample():
    global_test()
    global_counter_test()

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def make_counter_test():
    mc = make_counter()
    for i in range(5):
        print(mc())

if __name__ == '__main__':
    #globalExample()
    make_counter_test()
