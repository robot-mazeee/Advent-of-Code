# Result: 6257

with open("Day 5/input.txt", 'r') as file:
    content = file.read()
        
    split_index = content.find('W')
    part1 = (content[:split_index-1]).split('\n')
    part2 = (content[split_index+2:]).split('\n')

# check num1 before num2
def check_before(num1, num2):
    for line in part1:
        nums = line.split('|')
        if int(nums[0]) == num1 and int(nums[1]) == num2:
            return True
    return False

# check num1 after num2
def check_after(num1, num2):
    for line in part1:
        nums = line.split('|')
        if int(nums[0]) == num2 and int(nums[1]) == num1:
            return True
    return False

def bubble_sort(line):
    for i in range(len(line)-1):
        for j in range(len(line)-1-i):
            if check_before(int(line[j+1]), int(line[j])):
                line[j], line[j+1] = line[j+1], line[j]

result = 0
lines = []
for line in part2:
    nums = line.split(',')
    add = False
    for i in range(1, len(nums)):
        for j in range(i):
            if not check_before(int(nums[j]), int(nums[i])):
                add = True
                break

        for j in range(i+1, len(nums)):
            if not check_after(int(nums[j]), int(nums[i])):
                add = True
                break
    if add:
        lines.append(nums)

for line in lines:
    bubble_sort(line)
    
    result += int(line[len(line)//2])

print(result)