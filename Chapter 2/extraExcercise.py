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
Unpacking variadic positional arguments

>>> def is_prime(n):
...     if n > 1:
...         for i in range(2, n):
...             if (n % i) == 0:
...                 return
...             else:
...                 return n
>>> def product(*n, a=1): // n can be single or list of data
...     for i in n:
...         a *= i
...     return a
...
>>> primes = [number for number in range(2,100) if is_prime(number)]
>>> print(product(*primes)) //The syntax *seq unpacks a sequence into its constituent components
2725392139750729502980713245400918633290796330545803413734328823443106201171875
