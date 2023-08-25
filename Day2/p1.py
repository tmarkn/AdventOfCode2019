with open('input.txt', 'r') as f:
    inp = f.readline()

# 1 = add
# 2 = multiply
# 99 = stop

values = [int(x) for x in inp.split(',')]
values[1] = 12
values[2] = 2

index = 0

while True:
    # stop
    if values[index] == 99:
        break
    # add
    pos1,pos2,pos3 = values[index+1:index+4]
    if values[index] == 1:
        values[pos3] = values[pos1] + values[pos2]
    # multiply
    elif values[index] == 2:
        values[pos3] = values[pos1] * values[pos2]
    # error
    else:
        raise Exception("We shouldn't be here")
    # jump to next instruction
    index += 4

print(values[0])