#!/bin/env python

import numpy
import pickle
import cPickle
import time 
test = numpy.random.normal(0, 1, (1000, 100, 100))

def test_speed(title, ext, func):

    r = []
    for i in xrange(10):
        fout = open("test." + ext, "wb")
        s = time.time()
        func(fout, test)
        fout.close()
        r.append(time.time() - s)
    results = numpy.mean(r), numpy.min(r), numpy.max(r)
    print "%15s   %.3f  %.3f  %.3f " % (title, results[0], results[1], results[2])
    return results
print "%15s   mean   min    max " % ("title")

test_speed("bin no pickle" , "nopickle.npy", lambda x,y : numpy.save(x, y, allow_pickle=False))
test_speed("bin w/ pickle" , "pickle.npy", lambda x,y : numpy.save(x, y, allow_pickle=True))
test_speed("python pickle", "pkl", lambda x,y : pickle.dump(y, x))
test_speed("c pickle", "cpkl", lambda x,y : cPickle.dump(y, x))
test_speed("marshal", "msh", lambda f,a : cPickle.dump(a, f%))

