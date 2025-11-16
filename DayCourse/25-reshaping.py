import torch

# reshaping -  reshapes an input tensor to a defined shape
# viewing - return a view of an input tensor of a certain shape but keep the same 
#   memory as the original tensor
# stacking - combine multiple tensors on top of each other


x = torch.arange(1., 10.)
print(x, x.shape)

print(x.reshape(9, 1))

z = x.view(1, 9)
print(z, z.shape)

# changing z changes x because z is a view of x
z[:, 0] = 5
print(z, x)


# stack tensors on top of each other

x_stacked = torch.stack([x, x, x, x], dim=1)
print(x_stacked)