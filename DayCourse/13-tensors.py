import torch

scalar = torch.tensor(6)


vector = torch.tensor([1, 5])

MATRIX = torch.tensor([[5, 6],
                       [1, 2]])


TENSOR = torch.tensor([[[1, 2, 3],
                        [3, 6, 9],
                        [2, 4, 5]]])

# raw
print(scalar)
print(vector)
print(MATRIX)
print(TENSOR)

# get tensor back as python int:
print(f'Scalar as python int: {scalar.item()}')



# the number of dimensions is determined by the number of sets of []


print(f'Scalar dim: {scalar.ndim}')

print(f'Vector dim: {vector.ndim}')

print(f'Matrix dimensions: {MATRIX.ndim}')

print(f'Tensor dimensions: {TENSOR.ndim}')

print(f'Shapes: {scalar.shape, vector.shape, MATRIX.shape, TENSOR.shape}')


# zeroth dimension of the TENSOR:

print(TENSOR[0])