#!/usr/bin/env python3

def f(n: int):
    assert isinstance(n, int) and n >= 0, "n must be an non-negative int!"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)

for i in range(10):
    print("i = {:3d}, f(i) = {:3d}".format(i, f(i)))
