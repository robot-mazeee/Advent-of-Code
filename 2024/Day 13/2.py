# import numpy as np

# clicar no botao B o maximo de vezes, se for 3 vezes menos do que o A
with open("Day 13/input.txt", 'r') as file:
    inp = file.readlines()

lines = []
for line in inp:
    line = line.strip()
    line = line.replace('Button A: X+', '')
    line = line.replace('Button B: X+', '')
    line = line.replace('Prize: X=', '')
    line = line.split(', Y+')
    if ', Y=' in line[0]:
        line[0] = line[0].split(', Y=')
    lines.append(line)

tokens = 0

def calculate(x, y, target_x, target_y, a_x, a_y, b_x, b_y, cost, memo):
    # Base case: If the target coordinates are reached
    if (x, y) == (target_x, target_y):
        return cost
    
    # Base case: If coordinates exceed the target (no solution)
    if x > target_x or y > target_y:
        return float('inf')  # Indicating an impossible solution
    
    # Check if this state has already been computed (memoization)
    if (x, y, cost) in memo:
        return memo[(x, y, cost)]
    
    # Recursive case: Try pressing Button A
    cost_a = calculate(x + a_x, y + a_y, target_x, target_y, a_x, a_y, b_x, b_y, cost + 3, memo)
    
    # Recursive case: Try pressing Button B
    cost_b = calculate(x + b_x, y + b_y, target_x, target_y, a_x, a_y, b_x, b_y, cost + 1, memo)
    
    # Take the minimum cost between the two options
    result = min(cost_a, cost_b)
    
    # Store the result in the memoization dictionary
    memo[(x, y, cost)] = result
    
    return result

def get_det(a, b, c, d):
    return a * d - b * c

for i in range(0, len(lines), 4):
    a_x = int(lines[i][0])
    a_y = int(lines[i][1])
    b_x = int(lines[i+1][0])
    b_y = int(lines[i+1][1])
    prize_x = int(lines[i+2][0][0]) + 10000000000000
    prize_y = int(lines[i+2][0][1]) + 10000000000000
    det = get_det(a_x, a_y, b_x, b_y)
    if det != 0:
        det1 = get_det(prize_x, prize_y, b_x, b_y)
        det2 = get_det(a_x, a_y, prize_x, prize_y)
        button_a = det1 / det
        button_b = det2 / det
        print(button_a, button_b)
        if button_b > 0 and button_a > 0 and button_a.is_integer() and button_b.is_integer():
            tokens += 3*button_a + button_b

print(tokens)