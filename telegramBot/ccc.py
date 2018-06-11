#!/usr/bin/env python3
import os
import sys
import numpy
import pandas
import json
import time
import tensorflow as tf
from keras.wrappers.scikit_learn import KerasRegressor
from keras.models import load_model
# import warnings

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# warnings.filterwarnings('ignore')
def run(number=50):
    start=int(number)
    end=int(start)+1

    # load dataset
    dataframe = pandas.read_csv('aaaaaa.csv',header=None)
    dataset = dataframe.values
    # split into input (X) and output (Y) variables
    X = dataset[:, 0:109]
    Y = dataset[:, 110]
    # load model
    model = load_model('keras_model2.h5')
    prediction=model.predict(X[start:end])
    print(int(prediction[0][0]))
    #pip install h5py==2.8.0rc1
    json.dumps({'bar': ('baz', None, 1.0, 2), 'hi':'1'})
    time.sleep(3)
    return int(prediction[0][0])