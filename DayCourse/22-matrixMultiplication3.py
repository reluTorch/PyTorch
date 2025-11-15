import torch

# torch.mm is the same as torch.matmul

tensA = torch.randint(size=(3, 2), high=10, low=0)

tensB = torch.randint(size=(3, 2), high=10, low=0)

print(tensA)
print(tensB)
# these can't be multiplied

# to fix tensor shape issues we can transpose a tensor

print(tensA.T @ tensB)