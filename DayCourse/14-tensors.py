import torch
import numpy as np

# random tensors

random_tensor = torch.rand(3, 4)
print(random_tensor)

# expand it to the third dimension

print(torch.rand(2, 3, 4))




# creating np and torch zeros are similar
print(np.zeros((3, 3), dtype=int))

print(torch.zeros(3, 3, dtype=int))


# creating np random is different to torch

print(np.random.rand(3, 4))