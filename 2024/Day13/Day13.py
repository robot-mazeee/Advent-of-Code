def parse_input():
    with open("2024/Day13/input.txt", 'r') as file:
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

    return lines

def calculate(x, y, target_x, target_y, a_x, a_y, b_x, b_y, cost, memo):
    if (x, y) == (target_x, target_y):
        return cost
    
    if x > target_x or y > target_y: # if solution is impossible
        return float('inf')
    
    if (x, y, cost) in memo:
        return memo[(x, y, cost)]
    
    # try pressing A
    cost_a = calculate(x + a_x, y + a_y, target_x, target_y, a_x, a_y, b_x, b_y, cost + 3, memo)
    
    # try pressing B
    cost_b = calculate(x + b_x, y + b_y, target_x, target_y, a_x, a_y, b_x, b_y, cost + 1, memo)
    
    # take the minimum cost between the two buttons
    result = min(cost_a, cost_b)
    memo[(x, y, cost)] = result
    
    return result

def get_det(a, b, c, d):
    return a * d - b * c

def main():
    lines = parse_input()
    tokens1 = 0
    tokens2 = 0

    for i in range(0, len(lines), 4):
        a_x = int(lines[i][0])
        a_y = int(lines[i][1])
        b_x = int(lines[i+1][0])
        b_y = int(lines[i+1][1])

        # Part 1 with memoization
        prize_x = int(lines[i+2][0][0])
        prize_y = int(lines[i+2][0][1])
        memo = {}
        # initial cost 0
        min_cost = calculate(0, 0, prize_x, prize_y, a_x, a_y, b_x, b_y, 0, memo)
        
        # print(min_cost)
        if min_cost != float('inf'):
            tokens1 += min_cost

        # Part 2 with Cramer's rule
        prize_x += 10000000000000
        prize_y += 10000000000000
        det = get_det(a_x, a_y, b_x, b_y)
        if det != 0:
            det1 = get_det(prize_x, prize_y, b_x, b_y)
            det2 = get_det(a_x, a_y, prize_x, prize_y)
            button_a = det1 / det
            button_b = det2 / det
            # print(button_a, button_b)
            if button_b > 0 and button_a > 0 and button_a.is_integer() and button_b.is_integer():
                tokens2 += 3*button_a + button_b

    print("Part 1:", tokens1)
    print("Part 2:", int(tokens2))

main()