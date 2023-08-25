with open('input.txt', 'r') as f:
    inp = f.readlines()

total = 0
for line in inp:
    prev = int(line)
    while True:
        prev = (prev//3)-2
        if prev <= 0:
            break
        total += prev

print(total)