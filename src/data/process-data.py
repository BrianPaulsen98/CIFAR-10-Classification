import os
import pickle
import numpy as np

def unpickle(file):
    with open(file, 'rb') as f:
        dict = pickle.load(f, encoding='bytes')
    return dict

def create_master_dataset(directory):
    trainFormat = os.path.join(directory, 'data_batch_{}')
    testFile = os.path.join(directory, 'test_batch')

    trainDicts = []
    for i in range(1, 6):
        data = unpickle(trainFormat.format(i))
        trainDicts.append(data)

    trainSize = sum(len(l[b'labels']) for l in trainDicts)
    trainLabels = np.zeros((trainSize,))
    trainData = np.zeros((trainSize,3072))
    
    nextEmpty = 0
    for d in trainDicts:
        n = len(trainDicts[0][b'labels'])
        trainLabels[nextEmpty:(nextEmpty+n)] = d[b'labels']
        trainData[nextEmpty:(nextEmpty+n),] = d[b'data']

    testDict = unpickle(testFile)
    testSize = len(testDict[b'labels'])
    testLabels = np.zeros((testSize,))
    testData = np.zeros((testSize,3072))

    return trainData, trainLabels, testData, testLabels

create_master_dataset('../../data/raw/cifar-10-batches-py')

