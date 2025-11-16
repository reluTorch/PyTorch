import torch

tens = torch.arange(0, 100, 10)

# at what index do the min and max values lie at?
print(f'Positional min = {tens.argmin()}')
print(f'Positional max = {tens.argmax()}')