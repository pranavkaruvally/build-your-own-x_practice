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
        #fx = sigmoid(x)
        #return fx * (1 - fx)
        return np.exp(-x)/((1 + np.exp(-x)) ** 2)

    @staticmethod
    def mse(y_true, y_pred):
        return ((y_true - y_pred) ** 2).mean()

    def feedforward(self, x):
        self.h1 = self.sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        self.h2 = self.sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        self.output = self.sigmoid(self.w5 * self.h1 + self.w6 * self.h2 + self.b3)

        return self.output

    def sgd(self, y_true, y_pred, sum_h1, sum_h2, h1, h2, sum_output, learning_rate):


        d_L__d_ypred = -2 * (y_true - y_pred)

        d_ypred__d_h1 = self.w5 * self.deriv_sigmoid(sum_output)
        d_h1__d_w1 = self.w1 * self.deriv_sigmoid(sum_h1)
        d_L__d_w1 = d_L__d_ypred * d_ypred__d_h1 * d_h1__d_w1

        d_h1__d_w2 = self.w2 * self.deriv_sigmoid(sum_h1)
        d_L__d_w2 = d_L__d_ypred * d_ypred__d_h1 * d_h1__d_w2


        d_ypred__d_h2 = self.w6 * self.deriv_sigmoid(sum_output)    
        d_h2__d_w3 = self.w3 * self.deriv_sigmoid(sum_h2)
        d_L__d_w3 = d_L__d_ypred * d_ypred__d_h2 * d_h2__d_w3

        d_h2__d_w4 = self.w4 * self.deriv_sigmoid(sum_h2)
        d_L__d_w4 = d_L__d_ypred * d_ypred__d_h2 * d_h2__d_w4

        
        d_ypred__d_w5 = h1 * self.deriv_sigmoid(sum_output)
        d_L__d_w5 = d_L__d_ypred * d_ypred__d_w5

        d_ypred__d_w6 = h2 * self.deriv_sigmoid(sum_output)
        d_L__d_w6 = d_L__d_ypred * d_ypred__d_w6


        d_h1__d_b1 = self.deriv_sigmoid(sum_h1)
        d_L__d_b1 = d_L__d_ypred * d_ypred__d_h1 * d_h1__d_b1

        d_h2__d_b2 = self.deriv_sigmoid(sum_h2)
        d_L__d_b2 = d_L__d_ypred * d_ypred__d_h2 * d_h2__d_b2

        d_L__d_b3 = d_L__d_ypred * self.deriv_sigmoid(sum_output)


        self.w1 -= learning_rate * d_L__d_w1
        self.w2 -= learning_rate * d_L__d_w2
        self.w3 -= learning_rate * d_L__d_w3
        self.w4 -= learning_rate * d_L__d_w4
        self.w5 -= learning_rate * d_L__d_w5
        self.w6 -= learning_rate * d_L__d_w6

        self.b1 -= learning_rate * d_L__d_b1
        self.b2 -= learning_rate * d_L__d_b2
        self.b3 -= learning_rate * d_L__d_b3

    def train(self, data, labels):
        learning_rate = 0.1
        epochs = 1000

        for epoch in range(epochs):
            for X, y_true in zip(data, labels):
                sum_h1 = self.w1 * X[0] + self.w2 * X[1] + self.b1
                sum_h2 = self.w3 * X[0] + self.w4 * X[1] + self.b2

                h1 = self.sigmoid(sum_h1)
                h2 = self.sigmoid(sum_h2)

                sum_output = self.w5 * h1 + self.w6 * h2 + self.b3
                y_pred = self.sigmoid(sum_output)

                self.sgd(y_true, y_pred, sum_h1, sum_h2, h1, h2, sum_output, learning_rate)

            if epoch % 10 == 0:
                y_preds = np.apply_along_axis(self.feedforward, 1, data)
                loss = self.mse(labels, y_preds)
                print(f"Epoch {epoch} loss: {loss: 0.3f}")

# First column is weight and 2nd is height
data = np.array([
    [-2, -1],
    [25, 6],
    [17, 4],
    [-15, -6]
])

#Using height and weight gender is predicted
#0 for female and 1 for male
labels = np.array([
    1,
    0,
    0,
    1
])

network = NeuralNetwork()
network.train(data, labels)
print()
#Now to test
emily = np.array([-7, -3]) # 128 pounds, 63 inches
frank = np.array([20, 2])  # 155 pounds, 68 inches
print("Emily: %.3f" % network.feedforward(emily)) # 0.951 - F
print("Frank: %.3f" % network.feedforward(frank)) # 0.039 - M
