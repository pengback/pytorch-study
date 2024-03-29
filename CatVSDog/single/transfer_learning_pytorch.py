import os
import time

import torch
import torchvision
from torchvision import transforms, datasets, models
import matplotlib.pyplot as plt
from torch.autograd import Variable

path = '/Users/aliber/workspace/python/pytorch-study/CatVSDog/data/'
# path = '../data'
transform = transforms.Compose([
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])

data_image = {x: datasets.ImageFolder(root=os.path.join(path, x), transform=transform) for x in ['train', 'val']}
# data_image = datasets.ImageFolder(root="/Users/aliber/workspace/python/pytorch-study/CatVSDog/data/", transform=transform)

data_load_image = {x: torch.utils.data.DataLoader(dataset=data_image[x], batch_size=4, shuffle=True) for x in
                   ['train', 'val']}

use_gpu = torch.cuda.is_available()
print("Is use gpu: " , use_gpu)

classes = data_image['train'].classes
classes_index = data_image['train'].class_to_idx
print(classes)

print("train data set:", len(data_image['train']))
print("val data set:", len(data_image['val']))

X_train, y_train = next(iter(data_load_image['train']))
mean = [0.5, 0.5, 0.5]
std = [0.5, 0.5, 0.5]
img = torchvision.utils.make_grid(X_train)
img = img.numpy().transpose((1, 2, 0))
img = img * std + mean

print([classes[i] for i in y_train])
plt.imshow(img)

model = models.vgg16(pretrained=True)
print(model)

for parama in model.parameters():
    parama.requires_grad = False

model.classifier = torch.nn.Sequential(torch.nn.Linear(25088, 4096),
                                       torch.nn.ReLU(),
                                       torch.nn.Dropout(p=0.5),
                                       torch.nn.ReLU(),
                                       torch.nn.Dropout(p=0.5),
                                       torch.nn.Linear(4096, 2))
for index, parama in enumerate(model.classifier.parameters()):
    if index == 6:
        parama.requires_grad = True

if use_gpu:
    model = model.cuda()

cost = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.classifier.parameters())

print(model)

n_epoches = 1
for epoch in range(n_epoches):
    since = time.time()
    print("Epoch{}/{}".format(epoch, n_epoches))
    print("-" * 10)
    for param in ['train', 'val']:
        if param == 'train':
            model.train = True
        else:
            model.train = False

        running_loss = 0.0
        running_correct = 0
        batch = 0
        for data in data_load_image[param]:
            batch += 1
            X, y = data
            if use_gpu:
                X, y = Variable(X.cuda()), Variable(y.cuda())
            else:
                X, y = Variable(X), Variable(y)

            optimizer.zero_grad()
            y_pred = model(X)
            _, pred = torch.max(y_pred, 1)

            loss = cost(y_pred, y)
            if param == 'train':
                loss.backward()
                optimizer.step()

            running_loss += loss.data
            running_correct += torch.sum(pred == y.data)
            if batch % 5 == 0 and param == 'train':
                print("Batch {}, Train Loss: {:.4f}, Train ACC: {:.4f}".format(
                    batch, running_loss / (4 * batch), 100 * running_correct / (4 * batch)
                ))

        epoch_loss = running_loss / len(data_image[param])
        epoch_correct = 100 * running_correct / len(data_image[param])

        print("{} Loss: {:.4f}, Correct: {:.4f}".format(param, epoch_loss, epoch_correct))

    now_time = time.time() - since
    print("Training time is {:.0f}m {:.0f}s".format(now_time//60, now_time%60))

