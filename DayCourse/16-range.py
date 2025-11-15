import torch

seq = torch.arange(start=0, end=1000, step=77)


zeros_tens = torch.zeros_like(input=seq)

rand_tens = torch.rand_like(seq, dtype=torch.float32)

rand_ints = torch.randint_like(seq, high=10, low=0)

tens = torch.full_like(seq, 5) # general case for `zeroes` and `ones`

print(seq, zeros_tens, rand_tens, rand_ints, tens)

print(rand_tens[0].item())