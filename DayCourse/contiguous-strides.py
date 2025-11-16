import torch

x = torch.arange(9).view(3, 3)
print(x, "\n", x.stride())

# the stride here is telling us for each dimension, how many steps in memory
#   you have to take to get to the next element in that dimension

# for example, for dim=0 (aka our rows), you have to skip 3 to get to the next
#   element. And for dim=1 (columns), you only have to skip one to get to the
#   next element. This is because the elements are stored in memory as 
#   "0, 1, 2, 3...", therefore contiguous


y = x.T
print(y, "\n", y.stride())

# now the tensor has been transposed. The stride output shows us that for dim=0,
#   we have to only take one step to get to the next element, and for dim=1,
#   we have to take three steps to get to the next element. This is because
#   in memory it is still stored as "0, 1, 2, 3..." so non-contiguous. If it were
#   still contiguous we would now expect it to be stored as "0, 3, 6, 1, 4..."

print(y.reshape(1, 9))

z = y.contiguous()
print(z, "\n", z.stride())

print(z.view(1, 9))