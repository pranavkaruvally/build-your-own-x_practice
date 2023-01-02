import numpy as np

class NeuralNetwork:
    def __init__(self):
        
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def deriv_sigmoid(x):
        fx = sigmoid(x)
        return fx * (1 - fx)

    @staticmethod
    def mse(y_true, y_pred):
        return ((y_true - y_pred) ** 2).mean()

    def feedforward(self, x):
        self.h1 = self.sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        self.h2 = self.sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        self.output = self.sigmoid(self.w5 * self.h1 + self.w6 * self.h2 + self.b3)

        return self.output
