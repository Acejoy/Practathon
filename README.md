# README

Practathon is a hackathon organised by Srikanth Verma Sir, IISC CSA alumnus.

__Problem Statement__: Given 10 million points, each of 100 dimensions and a query point of same dimension, find the 10-nearest neighbors with a latency of <1 sec.(Any programming languages allowed.) Each point can sample from a Gaussian Distribution with mean=0 and sigma=100.

## TODO

- [x] Create a Dataset
- [x] Generate Queries
- [x] Write a brute force algo
- [ ] Write optimised Algorithms
  - [x] Using Max Heap algorithm of size 10.
- [ ] Check correctness of algorithms against brute force algorithm
- [x] Check the latency
- [ ] Get the latency below 1 second

## Programming Setup and Execution

```
- Programming Language: Python
-Libraries:
    -Numpy
    -Pandas
    -Time
    -heapq
```

`Execution:Install python>=3.0 on your system`
`To run: python file_name.py`

## Folder Structure

.
├── algo1.py
├── brute_force.py
├── correctness.py
├── create_dataset.py
├── query_generation.py
└── README.md

## Pseudocode and Time Complexity

### Brute Force

let the data is NxD matrix.

- For all points in the dataset, calculate the euclidean distance with the query point and store it a list. - O(ND)
- sort the list in ascending order. -O(NlogN)
- Return first 10 entries. - O(1)

Total complexity: O(ND + NlogN)

### Algorith 1 ( Using Max Heap)

let the data is NxD matrix. and the heap size is k.

- For first 10 points in the dataset, calculate the euclidean distance with the query point and Create a MaxHeap of size 10 - O(D).
- Traverse the rest of points and check the following:
  - if current point's distance is less than the top element of MaxHeap then a max-extraction followed by insertion is performed - O(Nlogk)
  - else, that point is discarded.

Total Complexity: O(D+ Nlogk)

## Youtube Video link

the link of video is follows: [Video Solution](#readme).
