import torch

float_32_tensor = torch.tensor([3.0, 6.0, 9.0], 
                               dtype=None, # what datatype is the tensor
                               device=None, # what device is the tensor on
                               requires_grad=False) # whether or not to track gradients with this tensor's operations

print(float_32_tensor.dtype) # returns float32 because float32 is the default dtype

# Main errors in PyTorch:
# 1.Tensors not right datatype
# 2.Tensors not right shape
# 3. Tensors not on the right device (tensors must be on the same device to interact)

float_16_tensor = float_32_tensor.type(torch.float16)
print(float_16_tensor)