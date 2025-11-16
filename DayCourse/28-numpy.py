import torch
import numpy as np

# converting between numpy and torch

array = np.arange(1.0, 8.0)
tensor = torch.from_numpy(array)
numpy_tensor = tensor.numpy()

print(array, tensor, numpy_tensor)