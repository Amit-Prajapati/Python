Reversed Iteration:
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
------------------------------------------------------------
Sorted Iteration:
Example: To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the sort unaltered.
>>> basket = ['pear', 'banana', 'orange', 'pear', 'apple']
>>> for fruit in sorted(basket):
...     print(fruit)
...
apple
banana
orange
pear
pear
------------------------------------------------------------
