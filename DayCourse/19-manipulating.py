import torch

# tensor operations include:
#  addition
#  subtraction
#  multiplication (element wise)
#  division
#  matrix multiplication

tens = torch.tensor([1, 2, 3])
print(f'Tensor + 10 = {tens + 10}')
print(f'Tensor - 10 = {tens - 10}')

# python multiplication
print(f'Tensor * 10 = {tens * 10}')

# torch multiplication
print(f'Pytorch method of tensor * 10 = {torch.mul(tens, 10)}')



