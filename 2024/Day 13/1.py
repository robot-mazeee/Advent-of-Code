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

def is_possible(a_x, a_y, b_x, b_y, prize_x, prize_y):
    if prize_x < 0 or prize_y < 0:
        return False
    if prize_x == 0 and prize_y == 0:
        return True
    return is_possible(a_x, a_y, b_x, b_y, prize_x - a_x, prize_y - a_y) \
        or is_possible(a_x, a_y, b_x, b_y, prize_x - b_x, prize_y - b_y)

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

for i in range(0, len(lines), 4):
    a_x = int(lines[i][0])
    a_y = int(lines[i][1])
    b_x = int(lines[i+1][0])
    b_y = int(lines[i+1][1])
    prize_x = int(lines[i+2][0][0])
    prize_y = int(lines[i+2][0][1])
    memo = {}
    # Call the recursive function starting from (0, 0) with initial cost 0
    min_cost = calculate(0, 0, prize_x, prize_y, a_x, a_y, b_x, b_y, 0, memo)
    print(min_cost)
    if min_cost != float('inf'):
        tokens += min_cost

print(tokens)