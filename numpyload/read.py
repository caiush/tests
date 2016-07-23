#!/bin/env python

import numpy
import pickle
import cPickle
import time 
test = numpy.random.normal(0, 1, (100, 100, 100))

def test_speed(title, ext, func):

    r = []
    for i in xrange(10):
        fout = open("test." + ext, "r")
        s = time.time()
        test = func(fout)
        fout.close()
        r.append(time.time() - s)
    results = numpy.mean(r), numpy.min(r), numpy.max(r)
    print "%15s   %.3f  %.3f  %.3f " % (title, results[0], results[1], results[2])
    return results

print "%15s   mean  min  max " % ("title")
#test_speed("bin no pickle" , "nopickle.npy", lambda x : numpy.load(x))
#test_speed("bin w/ pickle" , "pickle.npy", lambda x  : numpy.load(x))
#test_speed("python pickle", "pkl", lambda x  : pickle.load(x))
#test_speed("c pickle", "cpkl", lambda x  : cPickle.load(x))
test_speed("marshal", "msh", lambda f : cPickle.load(f))
