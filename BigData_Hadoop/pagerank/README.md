# PageRank

PageRank is a function that assigns real numbers to every page on the web. Google uses a variation of this algorithm in its serach queries. This repository contains my PageRank implementations in some ways.


### ``PageRank.py``
A naive approach to create a random graph and rank the nodes (pages) iteratively using the Matrix Power method and calculate PageRank score. <br />
Usage:  ``python PageRank.py``

### ``PageRank_efficient.py``
A modification of the above approach that uses ``numpy`` library for broadcasting and Matrix multiplication for time efficiency. This program also handles the cases of **Dangling Nodes** and **cycles** in graphs by introducing the **Damping Factor** ,``d``, unlike the previous implementation. <br />
Usage:  ``python PageRank_efficient.py``<br />

*Experimentally, Numpy vectorization and broadcasting in this implementation reduces the running time by a `factor of 10` as compared to the naive approach.*  

### Hadoop_MapReduce
This folder has an ``inputFile.txt`` where the ``pagerank_MapReduce.py`` script saves and modifies the matrix after each iteration. <br />
Usage: ``python pagerank_MapReduce.py`` <br />
Matrix multiplication is taken care of by the ``mapper`` and ``reducer`` scripts, though mapping and reducing part has not been included in the ``pagerank_MapReduce.py`` because the code will change depending on the Hadoop versions and dfs file name. <br />
Usage: ``cat <inputFile> | python mapper.py | sort | python reducer.py``
### Spark_implementation
The script `generateGraph.py` is used to generate a random graph with 100 edges (can be modified) and store the edges in `pagerank.txt` in the format: <br />
Node1  &ensp;&ensp;&ensp; Neighbour of node1 <br />
Node2  &ensp;&ensp;&ensp; Neighbour of node2 <br />
. <br />
. <br />

Copy the file to HDFS using: &ensp;
`hdfs dfs -put pagerank.txt <Name_of_HDFS_folder>`

`spark_pagerank.py` is a program that reads input from HDFS file `pagerank.txt`, calculates the PageRank score of pages using the hyperlinks method and computes their rank.<br />
Usage: `python spark_pagerank.py <pagerank.txt> <no. of iterations>` <br />
Requirement: HDFS nodes should be running <br />
