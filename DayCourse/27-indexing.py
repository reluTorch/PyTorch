import torch

x = torch.arange(1, 10, 1).reshape(1, 3, 3)
print(x)


# Dimensions:
#       0  1  2
#       |  |  | 
#       ^  ^  ^
print(x[0][0][1])

print(x[:, :, 1])

print(x[0, :, 2])