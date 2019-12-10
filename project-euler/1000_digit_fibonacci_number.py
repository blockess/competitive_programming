#!/usr/bin/env python

def gen_fib():
    n1 = 0
    n2 = 1
    while True:
        yield n1
        n1 += n2
        yield n2
        n2 += n1

g = gen_fib()
i = 0
f = 0
while len(str(f)) != 1000:
    f = next(g)
    print("{i}: {f}".format(i=i,f=f))
    i += 1
