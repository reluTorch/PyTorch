import torch

# getting information from tensors

# 1.To get dtype, use `tensor.dtype`
# 2.To get shape, use `tensor.shape`
# 3.To get device, use `tensor.device`


# .size() is a function, .shape is an attribute

some_tensor = torch.rand((3, 4), device="cuda")

cpu_tensor = torch.rand((3, 4), device=None)

print(some_tensor)
print(f'Datatype of tensor: {some_tensor.dtype}')
print(f'Shape of tensor: {some_tensor.shape}')
print(f'Device of tensor: {some_tensor.device}')

print(f'Passing `device=None` makes the tensor live on the cpu: {cpu_tensor.device}')