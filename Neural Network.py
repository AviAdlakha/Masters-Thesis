import keras
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Code to build the model

keras.backend.clear_session()
model = keras.Sequential(
    [
     layers.Dense(8, input_shape=(25,), activation='relu'),
     layers.Dense(1, activation='sigmoid')
    ]
)
model.summary()

# Code to train the model

data = pd.read_csv('./Data KO 26.csv') # The data to train on
Actual= pd.read_csv('./values.csv')    # Ground truth labels
model.compile( optimizer='adam',loss='bce', metrics='accuracy')
history = model.fit(x=data,y=Actual,batch_size=50,epochs=100,validation_split=0.2)
model.save('Model_KO_26.hdf5') # to save the model

# Code to evaluate the model accuracy for test data

test_x = pd.read_csv('./Data WT 10.csv') # Data to test
test_y = pd.read_csv('./values.csv')     # Ground truth labels
model.evaluate(test_x,test_y)
