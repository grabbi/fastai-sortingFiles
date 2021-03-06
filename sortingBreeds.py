import os, shutil, random
import pandas as pd
path = 'dogbreed'
trainPath = '../' + path +'/train/'
testPath =  '../' + path +'/test/'

shuffleSampleTrainN = 4
shuffleSampleValidN = 2
shuffleValidN = 20

df = pd.read_csv('../' + path + '/labels.csv', sep=",")


if os.path.exists(trainPath):

    if not os.path.exists('../' + path + '/sample'):
        os.makedirs('../' + path + '/sample')
        os.makedirs('../' + path + '/sample/train')
        os.makedirs('../' + path + '/sample/valid')

    if not os.path.exists('../' + path + '/valid'):
        os.makedirs('../' + path + '/valid')
    
    if not os.path.exists('../' + path + '/test/unknown'):
        os.makedirs('../' + path + '/unknown')

    for f in os.listdir(trainPath):
        breed = df[df["id"] == str.split(f, '.')[0]]["breed"].values[0]
        if not os.path.exists(trainPath + breed):
            os.makedirs(trainPath + breed)
        shutil.move(trainPath + f , trainPath + breed + '/' + f)
    

    for f in os.listdir(trainPath):
        if not os.path.exists('../' + path + '/sample/train/' + f):
            os.makedirs('../' + path + 'sample/train/' + f)
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
    
    for f in os.listdir(testPath):
        shutil.move(testPath + f , '../' + path + '/unknown/' + f)
    
    shutil.move('../' + path + '/unknown', '../' + path + '/test/')

    print("Finished sorting!")

else:
    print('Provide training data!')