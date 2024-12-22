with open("Day 14/input.txt", 'r') as file:
    inp = file.readlines()

lines = []
for line in inp:
    line = line.split()
    line[0] = line[0].replace('p=', '')
    line[1] = line[1].replace('v=', '')
    line[0] = line[0].split(',')
    line[1] = line[1].split(',')
    lines.append(line)

num_robots = len(inp)
tiles_wide = 103
tiles_tall = 101
iters = 100

def get_pos(x, y, v_x, v_y, seconds):
    # for _ in range(iters):
    x = (x + v_x*seconds) % tiles_tall
    y = (y + v_y*seconds) % tiles_wide
    return (x, y)

pos = []
seconds = 0
while True:
    seconds += 1
    for line in lines:
        y, x = line[0]
        v_y, v_x = line[1]
        x, y = get_pos(int(x), int(y), int(v_x), int(v_y), seconds)
        pos.append((x, y))
    pos = []
    if len(set(pos)) == num_robots:
        print(seconds)
        break

# time = 1
# pics = 5
# while True:
#     robots_pos  = set()
#     christmas = True
#     for line in lines:
#         y, x = line[0]
#         v_y, v_x = line[1]
#         final_coords = get_pos(int(x), int(y), int(v_x), int(v_y), time)
#         if final_coords in robots_pos:
#             christmas = False
#             break
#         robots_pos.add(final_coords)
#     if christmas:
#         break
#     time += 1

# print(time)

# quad1 = []
# quad2 = []
# quad3 = []
# quad4 = []
# tall = tiles_tall // 2
# wide = tiles_wide // 2
# for p in pos:
#     x, y = p[0], p[1]
#     if x < tall and y < wide:
#         quad1.append(pos)
#     if x >= (tiles_tall - tall) and y < wide:
#         quad2.append(pos)
#     if x < tall and y >= (tiles_wide-wide):
#         quad3.append(pos)
#     if x >= (tiles_tall - tall) and y >= (tiles_wide-wide):
#         quad4.append(pos)

# res = len(quad1) * len(quad2) * len(quad3) * len(quad4)
# print(res)