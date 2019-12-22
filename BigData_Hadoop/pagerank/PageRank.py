# PageRank Naive Approach
# Author: Manvi Gupta
# Roll no. B17092
# Course: CS561 - Big Data and MapReduce

import random
import timeit

class Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
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
    		for j in range(self.size):
    			if self.containsEdge(j, i):
    				c += self.adjMatrix[j][i]

    		for j in range(self.size):
    			if self.containsEdge(j, i):
    				self.adjMatrix[j][i] = 1.0/c

    def display(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:.2f}'.format(val)),
            print('\n')
            
    def findRank(self, n):
    	rankList = [(1.0/self.size) for i in range(self.size)]
    	
    	for j in range(n):
    		# print("Iteration: " +str(j+1)) 
    		for i in range(len(self.adjMatrix)): 
        		for k in range(len(rankList)):
        			rankList[i] += self.adjMatrix[i][k] * rankList[k] 
        		print(i+1, '{:.4f}'.format(rankList[i]))
        	
        # for i in range(self.size):
        #     print(i+1 '{:.4f}'.format(rankList[i]))
    	return rankList

        
def main():
    tic = timeit.timeit()
    g = Graph(20)
    for i in range(100):
        g.addEdge(random.randint(0, 19), random.randint(0, 19))
    # g.display()
    g.modifyGraph();
    print("Transition Matrix: ")
    g.display()
    print("Final PageRank score:")
    g.findRank(50)
    toc = timeit.timeit()
    print "Execution time (in seconds): " +str(abs(toc - tic))
            
if __name__ == '__main__':
   main()