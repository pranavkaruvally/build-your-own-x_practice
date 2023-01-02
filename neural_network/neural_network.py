import numpy as np
import neuron

class OurNeuralNetwork:
    def __init__(self):
        weights = np.array([1, 1])
        bias = 0

        self.h1 = neuron.Neuron(weights, bias)
        self.h2 = neuron.Neuron(weights, bias)
        self.o = neuron.Neuron(weights, bias)

    def feedforward(self, x):
        intermediate_input_h1 = self.h1.feedforward(x)
        intermediate_input_h2 = self.h2.feedforward(x)
        total = np.array([intermediate_input_h1, intermediate_input_h2])
        return self.o.feedforward(total)


if __name__ == "__main__":
    network = OurNeuralNetwork()
    x = np.array([-2, -1])
    print(f"{network.feedforward(x): 0.3f}")
