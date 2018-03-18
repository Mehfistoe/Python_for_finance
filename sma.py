import numpy as np

dataset = np.random.randint(5,9,20)

def movingaverage(values, window):
	weights = np.repeat(1.0, window)/window
	smas = np.convolve(values,weights,'valid')
	return smas

print(movingaverage(dataset, 3))