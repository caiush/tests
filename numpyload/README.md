
Speed tests for various was of dumoing a numpy array down to disk, clearly numpy.save is going to be faster, but how much?

```
In [35]: %run create.py
          title   mean   min    max
  bin no pickle   0.121  0.108  0.137
  bin w/ pickle   0.126  0.114  0.142
  python pickle   5.344  5.220  5.743
       c pickle   5.397  5.168  5.757
        marshal   5.602  5.219  5.838

In [36]: %run read.py
          title   mean  min  max
  bin no pickle   0.043  0.032  0.116
  bin w/ pickle   0.040  0.031  0.104
  python pickle   2.539  2.416  2.664
       c pickle   19.381  18.670  20.081
        marshal   22.184  21.125  23.316
```