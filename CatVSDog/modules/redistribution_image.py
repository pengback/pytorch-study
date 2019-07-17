#
# 重新分配完整的数据，将90%条数据作为训练数据， 10%条数据作为验证数据
#

import os
import shutil

def redistribution():
    data_file = os.listdir('../data/dogs_vs_cats')
    # print(filter(lambda x: x[:3] == 'Cat', data_file))
    cats_file = list(os.listdir('../data/dogs_vs_cats/Cat'))
    dogs_file = list(os.listdir('../data/dogs_vs_cats/Dog'))

    data_root = '../data/dogs_vs_cats'
    train_root = '../data/train'
    test_root = '../data/test'

    print(len(dogs_file))
    print(len(cats_file))

    for i in range(len(dogs_file)):
        image_path = data_root + '/Dog/' + dogs_file[i]
        if i < (len(dogs_file) * 0.9):
            new_path = train_root + '/Dog/' + dogs_file[i]
        else:
            new_path = test_root + '/Dog/' + dogs_file[i]
        shutil.move(image_path, new_path)

    for i in range(len(cats_file)):
        image_path = data_root + '/Cat/' + cats_file[i]
        if i < (len(cats_file) * 0.9):
            new_path = train_root + '/Cat/' + cats_file[i]
        else:
            new_path = test_root + '/Cat/' + cats_file[i]
        shutil.move(image_path, new_path)



if __name__ == '__main__':
    redistribution()