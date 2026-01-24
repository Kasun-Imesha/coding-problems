import torch
import torch.nn as nn
import torch.nn.functional as F


model = nn.Sequential(
    nn.Linear(n_input, n_hidden),
    nn.ReLU(),
    nn.Linear(n_hidden, n_out),
    nn.Sigmoid()
)


criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

model.train()
for epoch in range(n_epochs):
    pred = model(x_train)
    loss = criterion(pred, y_train)
    
    optimizer.zero_grad()
    loss.backward()

    optimizer.step()

class Net(nn.Model):
    def __init__(self):
        super(Net, self).__init__()



