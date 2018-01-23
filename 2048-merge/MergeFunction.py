test_line = [2,2,0,4]

def merge(line):
    '''
    helper function that merges a single row or column in 2048
    '''
    lenght_of_line = len(line)

    while 0 in line:
        line.remove(0)

    for block in range(len(line)):
        if block + 1 > len(line) - 1:
            break
        if line[block] == line[block + 1]:
            line[block] *= 2
            line.remove(line[block + 1])
            line.insert(block + 1, 0)

    while 0 in line:
        line.remove(0)
    while len(line) != lenght_of_line:
        line.append(0)

    return line

print(merge(test_line))
