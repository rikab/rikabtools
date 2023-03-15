import numpy as np


# Function to load and concatenate multiple numpy files togetehr
def load_numpy_batches(dataset, batches, start=0):

    f = np.load("%s_%d.npy" % (dataset, start))
    for i in range(start + 1, batches):
        t = np.load("%s_%d.npy" % (dataset, i))
        f = np.concatenate((f, t), axis=0)

    return f
