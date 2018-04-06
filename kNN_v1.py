from math import sqrt
import numpy as np

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



dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]

test_data = dataset[8]
eqlidian_dis = []
k = 3
for i_row in range(len(dataset)):
    dataset_row = dataset[i_row]
    temp_dist = similarity_metric(dataset_row, test_data)
    eqlidian_dis.append(temp_dist)

neighbors = get_neighbors(eqlidian_dis,k )
class_dataset = []
for x in neighbors:
    class_dataset.append(dataset[x][-1])
a = max(set(class_dataset), key=class_dataset.count)
print('Expected %d, Got %d.' % (dataset[8][-1], a))

