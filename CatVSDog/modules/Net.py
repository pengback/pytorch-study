import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.conv2d(3, 6, 5);
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 18 * 18, 800)
        self.fc2 = nn.Linear(800, 120)
        self.fc3 = nn.Linear(120, 2)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 18 * 18)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
