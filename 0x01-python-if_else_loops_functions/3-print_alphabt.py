#!/usr/bin/python3
for s in range(97, 123):
    if chr(s) == 'q' or chr(s) == 'e':
        continue
    print(chr(s).format(s), end='')
