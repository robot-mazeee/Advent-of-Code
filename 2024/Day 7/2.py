# result: 637696070419031

with open("Day 7/input.txt", 'r') as file:
    lines = file.readlines()

def parse_input():
    final_input = []
    for line in lines:
        l = line.split(': ')
        values = l[1].replace('\n', '').split(' ')
        for i in range(len(values)):
            values[i] = int(values[i])
        final = [int(l[0]), values]
        final_input.append(final)
    return final_input       

def test_all(values, res, index, wanted):
    length = len(values)
    # caso base
    if index == length-1:
        if res == wanted:
            print(res)
            return True
    
    # caso resursivo
    else:
        for i in range(index+1, length):
            v = values[i]
            combined = int(str(res) + str(v))
            return test_all(values, v*res, index+1, wanted) or \
            test_all(values, v+res, index+1, wanted) or \
            test_all(values, combined, index+1, wanted)

    return False

inp = parse_input()
# print(inp)
res = 0
# line[1] vetor de values
# line[0]: resultado pretendido

cur = 0
for line in inp:
    cur += 1
    print('\nline: ', cur, '\n')
    if test_all(line[1], line[1][0], 0, line[0]):
        print('\nfound\n')
        res += line[0]

print(res)
