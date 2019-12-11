import numpy as np

class Model(object):
	def __init__(self,filename):
		self.file_name = filename
		self.weights,self.biases = self.load_model()


	def feed_forward(self, data):
		data = np.array([data])
		data = data.transpose()
		Z = self.weights[0] @ data + self.biases[0]
		A = self.sigmoid_array(Z)
		num_layers = 4
		for i in range(num_layers - 2):
			i += 1
			Z = self.weights[i] @ A + self.biases[i]
			A = self.sigmoid_array(Z)
		return A

	def predict(self, data):
		return self.feed_forward(data)


	def load_model(self):
		file = open(self.file_name, 'rb')
		data = np.load(file, allow_pickle = True)
		weights, biases = data[0], data[1]
		return weights,biases

	def sigmoid_array(self, x):
		return 1 / (1 + np.exp(-x))

if __name__=='__main__':
	model = Model('model3')
	data = model.predict([0.82224265,0.34969363,0.13866422])
	print(data)




