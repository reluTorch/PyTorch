import torch

# One of the most common errors in deep learning is shape errors
# `torch.matmul(tens, tens)` can be replaced with `tens @ tens`


# matrix multiplication rules:
#  -take example matrices of shapes (a, b) @ (c, d)
#  -b must = c
#  -the resulting matrix is shape (a, d)
 
tens1 = torch.rand(3, 6)

tens2 = torch.rand(6, 10)

print(tens1 @ tens2)