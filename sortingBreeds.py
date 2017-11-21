import os, shutil, random
import pandas as pd
path = '../dogbreed/train/'
testPath =  '../dogbreed/test/'

shuffleSampleTrainN = 4
shuffleSampleValidN = 2
shuffleValidN = 20

df = pd.read_csv('../dogbreed/labels.csv', sep=",")


if os.path.exists(path):

    if not os.path.exists('../dogbreed/sample'):
        os.makedirs('../dogbreed/sample')
        os.makedirs('../dogbreed/sample/train')
        os.makedirs('../dogbreed/sample/valid')

    if not os.path.exists('../dogbreed/valid'):
        os.makedirs('../dogbreed/valid')

    for f in os.listdir(path):
        breed = df[df["id"] == str.split(f, '.')[0]]["breed"].values[0]
        if not os.path.exists(path + breed):
            os.makedirs(path + breed)
        shutil.move(path + f , path + breed + '/' + f)
    

    for f in os.listdir(path):
        if not os.path.exists('../dogbreed/sample/train/' + f):
            os.makedirs('../dogbreed/sample/train/' + f)
        samples = random.sample(os.listdir(path + f), shuffleSampleTrainN)
        for s in samples:
            shutil.move(path + f + '/' + s , '../dogbreed/sample/train/' + f + '/' + s)

    for f in os.listdir(path):
        if not os.path.exists('../dogbreed/sample/valid/' + f):
            os.makedirs('../dogbreed/sample/valid/' + f)
        samples = random.sample(os.listdir(path + f), shuffleSampleValidN)
        for s in samples:
            shutil.move(path + f + '/' + s , '../dogbreed/sample/valid/' + f + '/' + s)

    for f in os.listdir(path):
        if not os.path.exists('../dogbreed/valid/' + f):
            os.makedirs('../dogbreed/valid/' + f)
        samples = random.sample(os.listdir(path + f), shuffleValidN)
        for s in samples:
            shutil.move(path + f + '/' + s , '../dogbreed/valid/' + f + '/' + s)
    
    if not os.path.exists('../dogbreed/test/unknown'):
        os.makedirs('../dogbreed/test/unknown')

    os.system("find ../dogbreed/test/ -type f -print0 | xargs -0 mv -t ../dogbreed/test/unknown")
    print("Finished sorting!")

else:
    print('Provide training data!')