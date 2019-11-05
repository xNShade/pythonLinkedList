#create (4) data sets of 100 random integers each with values of 0 to 99.
#create (1) data set of 100 random integers values of 1 to 3.
#create them each run.
import numpy as np
np.set_printoptions(linewidth=33)

#Turn into function later
dataset1 = np.random.randint(0,100,100)
dataset2 = np.random.randint(0,100,100)
dataset3 = np.random.randint(0,100,100)
dataset4 = np.random.randint(0,100,100)
dataset5 = np.random.randint(1,4,100)

print(dataset1)
print(dataset2)
print(dataset3)
print(dataset4)
#Change precision
np.set_printoptions(linewidth=22)
print(dataset5)
