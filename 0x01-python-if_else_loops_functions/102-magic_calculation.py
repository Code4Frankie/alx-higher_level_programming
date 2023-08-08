#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(i, j, k):
    """Match bytecode provided by Holberton School."""
    if i < j:
        return k
    if k > j:
        return i + j

