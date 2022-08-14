import pandas as pd
import numpy as np
import heapq as hq
import time

dataFileName=''
chunksize=100000

class Point:
    def __init__(self, dis, index, arr):
        self.dis=-dis
        self.idx=index
        self.array=arr

    def __repr__(self):
        return '('+str(self.idx)+','+ str(-self.dis)+')'

    def __lt__(self, nxt):
        return self.dis<nxt.dis



class MaxHeapSol:
    def __init__(self, filename):
        self.dataFile=filename

    def solve(self, query_array):
        # row_num=0
        dist_list=[]
        hq.heapify(dist_list)

        for chunk in pd.read_csv(self.dataFile, chunksize=chunksize, header=None):
            for index, row in chunk.iterrows():
                # print(index, end=' ')
                row_np = row.to_numpy()
                euclid_dist = np.linalg.norm(query_array-row_np)
                if len(dist_list)<10:
                    hq.heappush(dist_list, Point(euclid_dist, index, row_np))
                else:
                    if dist_list[0].dis < euclid_dist:
                        hq.heapreplace(dist_list, Point(euclid_dist, index, row_np))

                # row_num+=1
            # print()

        dist_list.sort(key=lambda x: -x.dis)
        
        print(dist_list)
        print('******')

        # print()

        # nearest_indices= [x.idx for x in dist_list]
        # nearest_points = [0]*10       
        
        # # row_num=0

        # for chunk in pd.read_csv(self.dataFile, chunksize=chunksize, header=None):
        #     for idx, row in chunk.iterrows():
        #         row_np = row.to_numpy()
        #         if idx in nearest_indices:
        #             nearest_points[nearest_indices.index(idx)]=row_np
        #         # row_num+=1

        # # with open(self.dataFile, 'r') as data:
        # #     data=data.to_numpy()
        # #     for idx, line in enumerate(data):
        # #         if idx in nearest_indices:
        # #             nearest_points.append(line)
        
        nearest_indices=[]
        nearest_points=[]

        for pt in dist_list:
            nearest_indices.append(pt.idx)
            nearest_points.append(pt.array)

        return nearest_points, nearest_indices
        # return nearest_points,  

def printL(l):
    for ele in l:
        print(ele)

def main():
    sol = MaxHeapSol('data.csv')
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
