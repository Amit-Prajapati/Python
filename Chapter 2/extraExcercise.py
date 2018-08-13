Example 1: To loop over a sequence in reverse, first specify the sequence in forward direction "range(start, end, with step of)" and
            then call reversed() function.
>>> for i in reversed(range(0, 10, 2)):
...     print(i)
...
8
6
4
2
0

