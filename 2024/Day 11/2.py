import functools

# parse input
with open("Day 11/input.txt", 'r') as file:
    matrix = [list(line.split()) for line in file]

for line in matrix:
    for elem in line:
        if elem == ' ':
            line.remove(elem)

# using built-in memo
@functools.cache
def get_number(num, iters, splits):
    if iters == 0:
        return splits
    elif num == 0:
        return get_number(1, iters-1, splits)
    elif len(str(num)) % 2 == 0:
        num = str(num)
        num1 = int(num[:len(num)//2])
        num2 = int(num[len(num)//2:])
        # we only count a split once
        return get_number(num1, iters-1, splits+1) + get_number(num2, iters-1, 0)
    else:
        return get_number(num*2024, iters-1, splits)
    
# using manual memo
def get_number_memo(num, iters, splits, memo):
    if iters == 0:
        return splits
    
    if (num, iters, splits) in memo:
        return memo[(num, iters, splits)]
    elif num == 0:
        result = get_number_memo(1, iters-1, splits, memo)
        memo[(1, iters-1, splits)] = result
        return result
    elif len(str(num)) % 2 == 0:
        num = str(num)
        num1 = int(num[:len(num)//2])
        num2 = int(num[len(num)//2:])
        
        result1 = get_number_memo(num1, iters-1, splits+1, memo)
        result2 = get_number_memo(num2, iters-1, 0, memo)
        memo[(num1, iters-1, splits+1)] = result1
        memo[(num2, iters-1, 0)] = result2
        return result1 + result2
    else:
        result = get_number_memo(num*2024, iters-1, splits, memo)
        memo[(num*2024, iters-1, splits)] = result
        return result

res = 0
iters = 75
for line in matrix:
    for elem in line:
        # in the beggining we have only one element and empty memo dict
        res += get_number_memo(int(elem), iters, 1, {})
        # res += get_number(int(elem), iters, 1) 

print('Result:', res)