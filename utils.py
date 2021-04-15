from contextlib import contextmanager
import numpy as np
import time
import pandas as pd


#Save data to Null Object
class DevNullStore:
    def __init__(self):
        pass
    def __setitem__(*args, **kwargs):
        pass

class DiagnosticTimer:
    def __init__(self):
        self.diagnostics = []
    @contextmanager
    def time(self, **kwargs):
        tic = time.time()
        yield
        toc = time.time()
        kwargs["runtime"] = toc - tic
        self.diagnostics.append(kwargs)
    def dataframe(self):
        return pd.DataFrame(self.diagnostics)

def total_nthreads(c):
    return sum([v for v in c.nthreads().values()])

def total_ncores(client):
    return sum([v for v in client.ncores().values()])

def total_workers(client):
    return len(client.ncores())

def get_chunksize(data):
    return(np.prod(data.chunksize) * data.dtype.itemsize)