"""
So here it is: Shogun does not for a distance tree, but always uses
brute force.

So on low dimensions we can have the factor we want, just augment the
number of samples :-)

On the other hand, their brute force is somehow faster than ours ...

"""


from shogun.Classifier import KNN
from shogun.Features import RealFeatures, Labels
from shogun.Distance import EuclidianDistance
from datetime import datetime
import numpy as np

from scikits.learn import neighbors

n_samples = 3000
n_dim = 5
n_neighbors = 9
X = 100 * np.random.randn(n_samples, n_dim)
y = 10 * np.random.randn(n_samples).astype(np.int).astype(np.float)


def bench():
    """
    put as function for easy profiling
    """

    start = datetime.now()
    feat = RealFeatures(X.T)
    distance = EuclidianDistance(feat, feat)
    labels = Labels(y)

    knn = KNN(n_neighbors, distance, labels)
    knn.train()
    knn.classify(feat).get_labels()
    print 'shogun: ', datetime.now() - start


    start2 = datetime.now()
    clf = neighbors.Neighbors(n_neighbors=n_neighbors)
    clf.fit(X, y)
    clf.predict(X)
    print 'skl: ', datetime.now() - start2


if __name__ == '__main__':
    bench()
