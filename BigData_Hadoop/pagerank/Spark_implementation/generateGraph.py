import random

f = open("pagerank.txt", "w+")

n = int(input("Enter no. of nodes: "))

for i in range(100):
	f.write(str(random.randint(0, n-1)) + " " + str(random.randint(0, n-1)) + "\n")

f.close()
