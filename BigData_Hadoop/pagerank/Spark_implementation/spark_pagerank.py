# PageRank using Apache Spark
# Author: Manvi Gupta
# Roll no. B17092
# Course: CS561 - Big Data and MapReduce

from __future__ import print_function

import re
import sys
from operator import add
import timeit

from pyspark.sql import SparkSession


def computeContribs(urls, rank):
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)


def parseNeighbors(urls):
    parts = re.split(r'\s+', urls)
    # print(parts)
    return parts[0], parts[1]


if __name__ == "__main__":
    tic = timeit.timeit()
    if len(sys.argv) != 3:
        print("Usage: pagerank <file> <iterations>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonPageRank")\
        .getOrCreate()


    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])


    links = lines.map(lambda urls: parseNeighbors(urls)).distinct().groupByKey().cache()


    ranks = links.map(lambda url_neighbors: (url_neighbors[0], 1.0))

    d = 0.85
    for i in range(int(sys.argv[2])):
        contribs = links.join(ranks).flatMap(lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))
        ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * d + (1-d))


    for (link, rank) in ranks.collect():
        print("%s has rank: %s." % (link, rank))

    spark.stop()
    toc = timeit.timeit()
    print(toc - tic)
