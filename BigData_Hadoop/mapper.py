#!/usr/bin/python

import sys


#------------------------PHRASE/WORD COUNT----------------------------------------
# def phrases(l, n):
# 	for i in range(0, len(l)-n+1, 1):
# 		yield l[i:i+n]

# phrase_len = 4
# temp = []
# words = []
# #Word Count Example
# # input comes from standard input STDIN
# for line in sys.stdin:
# 	line = line.strip() #remove leading and trailing whitespaces
# 	temp = (line.split()) #split the line into words and returns as a list
# 	words += list(phrases(temp, phrase_len))


# #write the results to standard output STDOUT
# for word in words:
# 	print'%s    %s' % (word,1) #Emit the word

#-----------------------------MATRIX MULTIPLICATION-----------------------------------
A = []
B = []
for line in sys.stdin:
	R1, C1, R2, C2 = map(int,' '.join(str(line)).split())
	break
print(R1, C1, R2, C2)

i = 0
for line in sys.stdin:
	if i==R1:
		temp = map(int,' '.join(str(line)).split())
		B.append(temp)
	else:
		temp = map(int,' '.join(str(line)).split())
		A.append(temp)
		i += 1

print(A)
print(B)

AMap = []
i=0
j=0
for row in enumerate(A ,i):
	for elem in enumerate(row, j):
		temp = []
		for k in range(C2):
			temp.append(((i, k),  (A, j, elem)))
		AMap.append(temp)

# print(AMap)

k=0
j=0
i=0
BMap = []
for row in enumerate(B ,j):
	for elem in enumerate(row, k):
		temp = []
		for i in range(R1):
			temp.append(((i, k), (B, j, elem)))
		BMap.append(temp)


k=list(range(C2))
j=list(range(C1))
i=list(range(R1))


final = list(map((A, j, A[i][j]), (B, j, B[j][k])))
# final[(i, k)].append(((A, j, A[i][j]), (B, j, B[j][k])))