import torch 

tens = torch.tensor([1, 2, 3])

# element wise multiplication
print(tens, '*', tens)
print(f'Equals: {tens * tens}')


# matrix multiplication
print(torch.matmul(tens, tens))