# PageRank using Hadoop MapReduce
# Author: Manvi Gupta
# Roll no. B17092
# Course: CS561 - Big Data and MapReduce

import numpy as np
import random
import timeit

class Graph(object):
    def __init__(self, size):
        self.adjMatrix = np.zeros((size, size))
        self.size = size

    def addEdge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v2][v1] += 1

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __len__(self):
        return self.size

    def modifyGraph(self):
    	for i in range(self.size):
    		c=0
            # ch = 'A'
    		for j in range(self.size):
    			if self.containsEdge(j, i):
    				c += self.adjMatrix[j][i]

    		for j in range(self.size):
    			if self.containsEdge(j, i):
    				self.adjMatrix[j][i] /= c
                # f.write('{} {} {} {:.4f} \n'.format('A', i, j, self.adjMatrix[j][i]))

    def show(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:.2f}'.format(val)),
            print

    def findRank(self, n):
    	rankList = [(1.0/self.size) for i in range(self.size)]
        d = 0.85
        c = 'B'        
    	for j in range(n):
            f = open("inputFile.txt","w")
            print("Iteration: " +str(j+1))
            for i in range(self.size):
                for k in range(self.size):
                    f.write('{} {} {} {:.4f} \n'.format('A', i, k, self.adjMatrix[i][k]))
        	rankList = np.matmul(self.adjMatrix , rankList) * d + (1-d)/self.size
            for index, val in np.ndenumerate(rankList):
                print '{} {} {} {:.4f}'.format(c, index[0], 0, val)
                f.write('{} {} {} {:.4f} \n'.format(c, index[0], 0, val))
            f.close()
    	return rankList


def main():
    start = timeit.timeit()
    g = Graph(20)
    for i in range(100):
        g.addEdge(random.randint(0, 19), random.randint(0, 19))
	print("Transition Matrix: ")
	g.modifyGraph()
    g.show()
    print("Final PageRank score:")
    g.findRank(10)
    end = timeit.timeit()
    print "Execution time (in seconds): " +str(abs(end - start))  

if __name__ == '__main__':
   main()
