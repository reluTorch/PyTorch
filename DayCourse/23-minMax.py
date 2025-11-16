import torch

tens = torch.arange(0, 100, 10)

print(f'Min = {torch.min(tens)}')
print(f'Max = {torch.max(tens)}')

print(f'Mean = {torch.mean(tens.type(torch.float32))}')

# torch.mean requires float32 dtype
