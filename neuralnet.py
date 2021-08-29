import numpy as np


class NeuralNetwork():

    def __init__(self):
        # seeding for random number generation
        # np.random.seed(1)

        # converting weights to a 3 by 1 matrix with values from -1 to 1 and mean of 0
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1
        # print(self.synaptic_weights)

    def sigmoid(self, x):
        # applying the sigmoid function
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        # computing derivative to the Sigmoid function
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        print("1.training_inputs", training_inputs)
        print("2.training_outputs", training_outputs)
        # training the model to make accurate predictions while adjusting weights continually
        for iteration in range(training_iterations):
            # siphon the training data via  the neuron
            output = self.think(training_inputs)
            # print("6.think: ", output)

            # computing error rate for back-propagation
            error = training_outputs - output
            # print("7.error (training_outputs - output): ", error)

            # performing weight adjustments
            adjustments = np.dot(training_inputs.T, error *
                                 self.sigmoid_derivative(output))
            # print("8.adjustments (training_inputs * err*sigmoid(output)): ", adjustments)

            self.synaptic_weights += adjustments
            # print("self.synaptic_weights+= adjustments: ", self.synaptic_weights)

    def think(self, inputs):
        # passing the inputs via the neuron to get output
        # converting values to floats

        inputs = inputs.astype(float)
        # print("3.think inputs: ", inputs)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        # print("4.self.synaptic_weights: ", self.synaptic_weights)
        # print("5.think output sigmoid(inputs*synaptic_weights): ", output)
        return output


if __name__ == "__main__":

    # initializing the neuron class
    neural_network = NeuralNetwork()

    # print("Beginning Randomly Generated Weights: ")
    # print(neural_network.synaptic_weights)

    # training data consisting of 4 examples--3 input values and 1 output
    training_inputs = np.array([[100, 25, 1],
                                [10, 10, 1],
                                [1, 5, 2],
                                [12, 10, 1]])

    training_outputs = np.array([[1, 0, 0, 1]]).T

    # print(training_inputs)
    # print(training_outputs)
    # training taking place
    neural_network.train(training_inputs, training_outputs, 1500)

    print("Ending Weights After Training: ")
    print(neural_network.synaptic_weights)

    user_input_one = str(input("User Input One: "))
    user_input_two = str(input("User Input Two: "))
    user_input_three = str(input("User Input Three: "))

    print("Considering New Situation: ", user_input_one,
          user_input_two, user_input_three)
    print("New Output data: ")
    print(neural_network.think(
        np.array([user_input_one, user_input_two, user_input_three])))
    print("Wow, we did it!")
