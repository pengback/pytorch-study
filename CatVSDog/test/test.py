import os


def show(arg):
    print('this is ' + arg);
    data = list(os.listdir(arg+'/'))
    print(data)

if __name__ == '__main__':
    # s = 'string'
    path = '/Users/aliber/workspace/python/pytorch-study/CatVSDog/data/'
    data = {x: show(os.path.join(path, x)) for x in ['train', 'val']}
