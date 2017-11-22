import os, shutil, random
path = '../kaggle/train/'
shuffleSampleTrainN = 8
shuffleSampleValidN = 4
shuffleValidN = 1000

if os.path.exists('../kaggle/train'):

    if not os.path.exists('../kaggle/sample'):
        os.makedirs('../kaggle/sample')
        os.makedirs('../kaggle/sample/train')
        os.makedirs('../kaggle/sample/valid')
        os.makedirs('../kaggle/sample/train/dog')
        os.makedirs('../kaggle/sample/train/cat')
        os.makedirs('../kaggle/sample/valid/dog')
        os.makedirs('../kaggle/sample/valid/cat')

    if not os.path.exists('../kaggle/valid'):
        os.makedirs('../kaggle/valid')
        os.makedirs('../kaggle/valid/dog')
        os.makedirs('../kaggle/valid/cat')


    if not os.path.exists(path + 'cat'):
        os.makedirs(path + 'cat')

    if not os.path.exists(path + 'dog'):
        os.makedirs(path + 'dog')

    if not os.path.exists('../kaggle/test/unknown'):
        os.makedirs('../kaggle/unknown')

    for filename in os.listdir(path):
        if os.path.isfile(path + filename):
            if filename[:3] == 'cat':
                shutil.move(path + filename , path + 'cat/' + filename)
            else:
                shutil.move(path + filename , path + 'dog/' + filename)
    
    sampleCats = random.sample(os.listdir(path + 'cat/'), shuffleSampleTrainN)
    sampleDogs = random.sample(os.listdir(path + 'dog/'), shuffleSampleTrainN)

    for cat, dog in zip(sampleCats, sampleDogs):
        shutil.copy(path + 'cat/' + cat, '../kaggle/sample/train/cat/' + cat)
        shutil.copy(path + 'dog/' + dog, '../kaggle/sample/train/dog/' + dog)

    sampleCats = random.sample(os.listdir(path + 'cat/'), shuffleSampleValidN)
    sampleDogs = random.sample(os.listdir(path + 'dog/'), shuffleSampleValidN)

    for cat, dog in zip(sampleCats, sampleDogs):
        shutil.copy(path + 'cat/' + cat, '../kaggle/sample/valid/cat/' + cat)
        shutil.copy(path + 'dog/' + dog, '../kaggle/sample/valid/dog/' + dog)

    sampleCats = random.sample(os.listdir(path + 'cat/'), shuffleValidN)
    sampleDogs = random.sample(os.listdir(path + 'dog/'), shuffleValidN)

    for cat, dog in zip(sampleCats, sampleDogs):
        shutil.move(path + 'cat/' + cat, '../kaggle/valid/cat/' + cat)
        shutil.move(path + 'dog/' + dog, '../kaggle/valid/dog/' + dog)

    
    shutil.move('../kaggle/unknown', '../kaggle/test/')

    print("Finished sorting!")
    
else:
    print('Provide training data!')