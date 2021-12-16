import numpy as np

with open('day06.txt') as f:
    initial = np.array([f.read().split(',')], dtype=int)

# simulate one fish
days = 80
timer = 6
fish = [timer]
for i in range(80 + 6):
    timer -= 1
    if 