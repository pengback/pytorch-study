import os
from PIL import Image


def main():
    img_path = '../data/Cat/0.jpg'
    path = os.path.join(os.getcwd(), img_path)
    img = Image.open(path)

    print("图片格式为：", img.format)
    print("图片大小为：", img.size)

if __name__ == '__main__':
    main()