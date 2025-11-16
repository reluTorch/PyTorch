import torch

device = 'cuda'

tens = torch.tensor([1, 2, 5])
print(tens, tens.device)

gpu_tens = tens.to(device)
print(gpu_tens)

cpu_tens = tens.to('cpu')
print(cpu_tens, tens.device)