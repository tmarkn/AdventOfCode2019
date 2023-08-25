with open('input.txt', 'r') as f:
    inp = f.readlines()

total = 0
for line in inp:
    mass = int(line)
    fuel = (mass//3)-2
    total += fuel

print(total)