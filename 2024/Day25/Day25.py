'''
locks - top row filled (#) and the bottom row empty (.);
keys - top row empty and the bottom row filled.
'''

def get_key_or_lock(lines, keys, locks):
    matrix = []
    for line in lines:
        chars = []
        line = line.strip()
        for char in line:
            chars.append(char)
        matrix.append(chars)

    is_lock = True
    for top in matrix[0]:
        if top != '#':
            is_lock = False
            break

    if is_lock:
        locks.append(matrix)
    else:
        keys.append(matrix)

    return keys, locks

def parse_input(file_in):    
    with open(file_in, 'r') as file:
        inp = [line.strip() for line in file]

    keys = []
    locks = []
    lines = []
    for line in inp:
        if line == '':
            keys, locks = get_key_or_lock(lines, keys, locks)
            lines = []
        else:
            lines.append(line)
    keys, locks = get_key_or_lock(lines, keys, locks)

    return keys, locks

def get_key_height(key):
    heights = []
    for col in range(len(key[0])):
        row = len(key)-1
        height = 0
        while row > 1 and key[row-1][col] != '.':
            height += 1
            row -= 1
        heights.append(height)

    return heights

def get_lock_height(lock):
    heights = []
    for col in range(len(lock[0])):
        row = 1
        height = 0
        while row < len(lock)-1 and lock[row][col] != '.':
            height += 1
            row += 1
        heights.append(height)

    return heights

def get_heights(keys, locks):
    keys_heights = []
    locks_heights = []

    for key in keys:
        keys_heights.append(get_key_height(key))
    for lock in locks:
        locks_heights.append(get_lock_height(lock))

    return keys_heights, locks_heights

def overlap(key_heights, lock_heights, size):
    length = len(key_heights)
    for i in range(length):
        key_height = key_heights[i]
        lock_height = lock_heights[i]
        if key_height+lock_height > size-2:
            return True
    return False

def get_key_lock_pairs(keys, locks):
    size = len(keys[0])
    keys_heights, locks_heights = get_heights(keys, locks)
    key_lock_pairs = 0

    for key_height in keys_heights:
        for lock_height in locks_heights:
            if not overlap(key_height, lock_height, size):
                key_lock_pairs += 1

    return key_lock_pairs

def main():
    keys, locks = parse_input("2024/Day25/input.txt")
    key_lock_pairs = get_key_lock_pairs(keys, locks)

    print("Answer:", key_lock_pairs)

main()