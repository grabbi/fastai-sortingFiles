import os, shutil, random

path = 'plants'
trainPath = '../' + path +'/train/'
testPath =  '../' + path +'/test/'

shuffleSampleTrainN = 4
shuffleSampleValidN = 2
shuffleValidN = 20


if os.path.exists(trainPath):

    if not os.path.exists('../' + path + '/sample'):
        os.makedirs('../' + path + '/sample')
        os.makedirs('../' + path + '/sample/train')
        os.makedirs('../' + path + '/sample/valid')

    if not os.path.exists('../' + path + '/valid'):
        os.makedirs('../' + path + '/valid')

    for f in os.listdir(trainPath):
        if not os.path.exists('../' + path + '/sample/train/' + f):
            os.makedirs('../' + path + '/sample/train/' + f)
        samples = random.sample(os.listdir(trainPath + f), shuffleSampleTrainN)
        for s in samples:
            shutil.copy(trainPath + f + '/' + s , '../' + path + '/sample/train/' + f + '/' + s)

    for f in os.listdir(trainPath):
        if not os.path.exists('../' + path + '/sample/valid/' + f):
            os.makedirs('../' + path + '/sample/valid/' + f)
        samples = random.sample(os.listdir(trainPath + f), shuffleSampleValidN)
        for s in samples:
            shutil.copy(trainPath + f + '/' + s , '../' + path + '/sample/valid/' + f + '/' + s)

    for f in os.listdir(trainPath):
        if not os.path.exists('../' + path + '/valid/' + f):
            os.makedirs('../' + path + '/valid/' + f)
        samples = random.sample(os.listdir(trainPath + f), shuffleValidN)
        for s in samples:
            shutil.move(trainPath + f + '/' + s , '../' + path + '/valid/' + f + '/' + s)

    print("Finished sorting!")

else:
    print('Provide training data!')