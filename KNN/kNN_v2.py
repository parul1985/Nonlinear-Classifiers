from math import sqrt
import numpy as np
import csv
import random


# Load a CSV file
# randomly divide into test ad train dataset
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            # convert first four column to float
            for y in range(5):
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
    for i_var in range(1,5):
        print(train_data_row[i_var])
        squareddiff += (train_data_row[i_var] - test_data[i_var]) ** 2
    print('\n')
    return sqrt(squareddiff)


trainingSet = []
testSet = []
split = 0.67
loadDataset('C:\\Users\\Parul\\PycharmProjects\\Nonlinearclassifiers\\KNN\\iris.csv', split, trainingSet, testSet)
print 'Train set: ' + repr(len(trainingSet))
print 'Test set: ' + repr(len(testSet))

# generate predictions
predictions = []
k = 3

for i_test_row in range(len(testSet)):
    eqlidian_dis = []
    for i_row in range(len(trainingSet)):
        dataset_row = trainingSet[i_row]
        temp_dist = similarity_metric(dataset_row, testSet[i_test_row])
        eqlidian_dis.append(temp_dist)

    neighbors = get_neighbors(eqlidian_dis, k)
    class_dataset = []
    for x in neighbors:
        class_dataset.append(trainingSet[x][-1])
    a = max(set(class_dataset), key=class_dataset.count)
    print('Expected %s, Got %s.' % (testSet[i_test_row][-1], a))
