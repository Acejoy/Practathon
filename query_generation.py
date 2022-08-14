import numpy as np

mean=0
sigma=100

num_features=100
num_records=100

with open('queries.csv', 'a') as dataFile:
    for i in range(num_records):
        dataPoint = np.random.normal(mean, sigma, (1,num_features))
        np.savetxt(dataFile, dataPoint, delimiter=',', fmt='%.6f')
