#!/usr/bin/env python 
import csv

dataFolder = "data/"

clientTable = "../data/cliente_tabla.csv"
productTable = "../data/producto_tabla.csv"
townState = "../data/town_state.csv"
testData = "../data/test.csv"
trainData = "../data/train.csv"


def breakCSVFile(filename):
	result = []
	with open(filename, 'rb') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		for row in csvreader:
			result.append(row)
	return result


counter = 0
file = open(trainData)
for line in file:
	counter += 1

file.close()

print counter

# pFile = breakCSVFile(trainData)

# print pFile

# pFile.pop(0)

# pFileNum = [float(x[0]) for x in pFile]

#print len(pFile)

# plt.plot(pFileNum)
# plt.ylabel('some numbers')
# plt.show()

# with open(productTable, 'r') as file:
    # print file.read()










