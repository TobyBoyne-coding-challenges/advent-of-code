import numpy as np

with open('day07.txt') as f:
    x = np.array(f.read().split(','), dtype=int)
    
    
pos = np.median(x)
fuel = np.abs(x - pos).sum()
print(fuel)

# minimise tri(|x-m|)