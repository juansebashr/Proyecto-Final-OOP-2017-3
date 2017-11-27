# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
class Neural_Network():
   def __init__(self,model,model_type,epochs,batch_size):
        # fix random seed for reproducibility
        numpy.random.seed(7)
        # load pima indians dataset
        dataset = numpy.loadtxt("C:\\Users\\Liliana Reyes\\PycharmProjects\\OOP_Final_Project\\Neural_Network\\TrainingData.txt", delimiter=",")
        # split into input (X) and output (Y) variables
        X = dataset[:,0:7]
        Y = dataset[:,7:10]
        # create model
        model = Sequential()
        model.add(Dense(12, input_dim=7, activation='relu'))
        model.add(Dense(10,activation="relu"))
        model.add(Dense(8,activation="relu"))
        model.add(Dense(5, activation='relu'))
        model.add(Dense(3, activation='sigmoid'))
        # Compile model
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        # Fit the model
        model.fit(X, Y, epochs=181, batch_size=100)
        # evaluate the model
        scores = model.evaluate(X, Y)
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100),)
        # Fit the model
        history = model.fit(X, Y, validation_split=0.33, epochs=181, batch_size=100, verbose=0)
        # list all data in history
        print(history.history.keys())
        self.History = history

