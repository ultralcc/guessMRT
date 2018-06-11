import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy
import pickle
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras import backend as K
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
def root_mean_squared_error(y_true, y_pred):
        return K.sqrt(K.mean(K.square(y_pred - y_true), axis=-1)) 

# load dataset
dataframe = pandas.read_csv('aaaaaa.csv',header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:, 0:109]
Y = dataset[:, 110]
# define base mode


def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(1000, input_dim=109,  kernel_initializer="normal", activation='relu'))
    model.add(Dense(1000, kernel_initializer="normal", activation='relu'))
    model.add(Dense(1000, kernel_initializer="normal", activation='relu'))
    model.add(Dense(1000, kernel_initializer="normal", activation='relu'))
    model.add(Dense(1000, kernel_initializer="normal", activation='relu'))
    model.add(Dense(1000, kernel_initializer="normal", activation='relu'))
    model.add(Dense(1000, kernel_initializer="normal", activation='relu'))
    model.add(Dense(1000, kernel_initializer="normal", activation='relu'))

    model.add(Dense(1,  kernel_initializer="normal"))
    # Compile model
    model.compile(loss=root_mean_squared_error, optimizer='adam')
    return model

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# evaluate model with standardized dataset
estimator = KerasRegressor(build_fn=baseline_model, nb_epoch=20000, batch_size=100, verbose=0)

# use 10-fold cross validation to evaluate this baseline model
kfold = KFold(n_splits=10, random_state=seed)
results = -cross_val_score(estimator, X, Y, cv=kfold)


print("Standardized: %.2f (%.2f) MSE" % (results.mean(), results.std()))

estimator.fit(X, Y)
estimator.model.save('keras_model3.h5')
