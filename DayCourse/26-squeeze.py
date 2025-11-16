import torch

# squeeze - removes all `1` dimensions from a tensor
# unsqueeze - add a `1` dimension to a tensor
# permute - return a view of the input dimensions permuted (swapped) in a certain
#   way

tens = torch.zeros((2, 1, 2, 1, 2), dtype=torch.int32)

print(tens)
print(tens.squeeze())

small = torch.randint(size=(9,), low=0, high=10)

print(small, small.shape)
print(small.unsqueeze(dim=1))


colour = torch.rand(size=(224, 224, 3)) # [height, width, colour channels]

perm = colour.permute(2, 0, 1)

print(f'Original shape: {colour.shape}')
print(f'Permute shape: {perm.shape}')