from math import sqrt
import numpy as np
import csv
import random

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


def get_neighbors(eqlidian_dis, k):
    sort_index = np.argsort(eqlidian_dis)
    neighbors = []
    for x in range(k):
        neighbors.append(sort_index[x])
    return neighbors


def similarity_metric(train_data_row, test_data):
    squareddiff = 0
    for i_var in range(len(train_data_row)):
        squareddiff += (train_data_row[i_var]-test_data[i_var])**2
    return sqrt(squareddiff)




filename = 'Iris.csv'
split = 0.7
trainingSet=[]
testSet=[]
loadDataset(filename, split, trainingSet, testSet)

eqlidian_dis = []
k = 3
for i_row in range(len(trainingSet)):
    dataset_row = trainingSet[i_row]
    temp_dist = similarity_metric(dataset_row, testSet)
    eqlidian_dis.append(temp_dist)

neighbors = get_neighbors(eqlidian_dis,k )
class_dataset = []
for x in neighbors:
    class_dataset.append(trainingSet[x][-1])
a = max(set(class_dataset), key=class_dataset.count)
print('Expected %d, Got %d.' % (trainingSet[8][-1], a))


# Test on Iris dataset
filename = 'Iris.csv'
dataset = loadDataset(filename)
print('Train set: ' + repr(len(trainingSet)))
print('Test set: ' + repr(len(testSet)))
for i in range(1, len(dataset[0])):
str_column_to_float(dataset, i)
# convert first column to integers
str_column_to_int(dataset, 0)
# evaluate algorithm
n_folds = 5
num_neighbors = 5
