
import shutil
import os

if __name__ == '__main__':
    path = '/Users/aliber/workspace/python/pytorch-study/CatVSDog/data/train/'
    data_file = list(os.listdir(path))
    print(data_file)
    # for x in data_file:
    #     arr = x.split(".")
    #     print(arr)
    #     if len(arr) == 3:
    #         os.rename(path + x, path + arr[0] + arr[1] + '.' + arr[2])
