with open("2024/Day 7/input.txt", 'r') as file:
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

def test_all_p1(values, res, index, wanted):    
    length = len(values)
    # caso base
    if index == length-1:
        if res == wanted:
            return True
    
    # caso resursivo
    else:
        for i in range(index+1, length):
            return test_all_p1(values, values[i]*res, index+1, wanted) or \
            test_all_p1(values, values[i]+res, index+1, wanted)
        
    return False

def test_all_p2(values, res, index, wanted):
    length = len(values)
    # base case
    if index == length-1:
        if res == wanted:
            return True
    
    # recursive case
    else:
        for i in range(index+1, length):
            v = values[i]
            combined = int(str(res) + str(v))
            return test_all_p2(values, v*res, index+1, wanted) or \
            test_all_p2(values, v+res, index+1, wanted) or \
            test_all_p2(values, combined, index+1, wanted)  
        
    return False

def main():
    inp = parse_input()
    res1 = 0
    res2 = 0

    cur = 0
    for line in inp:
        cur += 1
        if test_all_p1(line[1], line[1][0], 0, line[0]):
            res1 += line[0]
        if test_all_p2(line[1], line[1][0], 0, line[0]):
            res2 += line[0]

    print('Part 1:', res1)
    print('Part 2:', res2)

main()