In our code we used two major python libraries :

1. NUMPY
2. Sklearn

NumPy ,
is the fundamental package for scientific computing with Python. It contains among other things:

    -a powerful N-dimensional array object
    -sophisticated (broadcasting) functions
    -tools for integrating C/C++ and Fortran code
    -useful linear algebra, Fourier transform, and random number capabilities

Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. 
Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of
databases.


In scikit-learn, 
an estimator for classification is a Python object that implements the methods fit(X, y) and predict(T).

An example of an estimator is the class sklearn.svm.SVC that implements support vector classification. The constructor of an estimator 
takes as arguments the parameters of the model, but for the time being, we will consider the estimator as a black box:

>>> from sklearn import svm
>>> clf = svm.SVC(gamma=0.001, C=100.)

