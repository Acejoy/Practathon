import numpy as np
import pandas as pd
import time 

chunksize=10000

class BFSol:
    def __init__(self, filename):
        self.dataFile=filename

    def solve(self, query_array):
        row_num=0
        dist_list=[]

        for chunk in pd.read_csv(self.dataFile, chunksize=chunksize, header=None):
            for index, row in chunk.iterrows():
                # print(index, end=' ')
                row_np = row.to_numpy()
                euclid_dist = np.linalg.norm(query_array-row_np)
                dist_list.append((index, euclid_dist))
                # row_num+=1
            # print()

        dist_list.sort(key=lambda x: x[1])
        
        print(dist_list[0:10])
        print('******')

        print()

        nearest_indices= [x[0] for x in dist_list[0:10]]
        nearest_points = [0]*10       
        
        # row_num=0

        for chunk in pd.read_csv(self.dataFile, chunksize=chunksize, header=None):
            for idx, row in chunk.iterrows():
                row_np = row.to_numpy()
                if idx in nearest_indices:
                    nearest_points[nearest_indices.index(idx)]=row_np
                # row_num+=1

        # with open(self.dataFile, 'r') as data:
        #     data=data.to_numpy()
        #     for idx, line in enumerate(data):
        #         if idx in nearest_indices:
        #             nearest_points.append(line)
        

        return nearest_points, nearest_indices
        # return nearest_points, 

# def check_sol(q_a, neigh, l):
#     l_k = l[0:10]

#     for n, dis in zip(neigh, l_k):
#         distance=0;
#         # ndarray_n = n.to_numpy()
#         for i in range(100):
#             distance+= (n[i]-q_a[i])**2
        
#         distance = distance**0.5

#         print(dis[1]-distance)

def printL(l):
    for ele in l:
        print(ele)

def main():
    sol = BFSol('data.csv')
    demo_query = np.random.normal(0,100, 100)

    # neighbors, distances = sol.solve(demo_query)
    start = time.time()
    neighbors, _ = sol.solve(demo_query)
    end = time.time()
    print(end-start)
    # check_sol(demo_query, neighbors, distances)
    printL(neighbors)


if __name__=="__main__":
    main()


