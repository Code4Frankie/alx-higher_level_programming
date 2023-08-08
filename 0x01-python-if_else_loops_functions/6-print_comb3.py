#!/usr/bin/python3
for s in range(0, 8):
    for t in range(s + 1, 10):
        print("{:d}{:d}".format(s, t), end=', ')
print("{:d}{:d}".format(s + 1, t))
