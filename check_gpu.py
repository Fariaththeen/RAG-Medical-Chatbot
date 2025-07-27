import os
import sys
import torch

print("--- System and Python Information ---")
print(f"Python Version: {sys.version}")
print(f"Python Executable: {sys.executable}")
print("-" * 35)

print("\n--- PyTorch and CUDA Information ---")
# Check if PyTorch was built with CUDA support
cuda_available = torch.cuda.is_available()
print(f"Is CUDA available to PyTorch? -> {cuda_available}")

if cuda_available:
    # If CUDA is available, print more details
    print(f"CUDA Version PyTorch was built with: {torch.version.cuda}")
    print(f"Number of GPUs available: {torch.cuda.device_count()}")
    current_device = torch.cuda.current_device()
    print(f"Current GPU Index: {current_device}")
    print(f"Current GPU Name: {torch.cuda.get_device_name(current_device)}")
else:
    print("PyTorch cannot find a compatible CUDA installation. This is the root of the problem.")
print("-" * 35)