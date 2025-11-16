import torch

randA = torch.rand(3, 4)

randB = torch.rand(3, 4)

print(randA, randB, randA == randB)


RANDOM_SEED = 16    

torch.manual_seed(RANDOM_SEED)
randC = torch.rand(3, 4)
torch.manual_seed(RANDOM_SEED)
randD = torch.rand(3, 4)

print(randC, randD, randC == randD)