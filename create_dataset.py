import numpy as np

mean=0
sigma=100

size = (10000000, 100)
num_features=100
num_records=10000000

num_reduced_records=1000

with open('small_data.csv', 'a') as dataFile:
    for i in range(num_reduced_records):
        dataPoint = np.random.normal(mean, sigma, (1,num_features))
        np.savetxt(dataFile, dataPoint, delimiter=',', fmt='%.6f')

# data = np.random.normal(0,100, size)

# np.savetxt('data.csv', data, delimiter=',')
