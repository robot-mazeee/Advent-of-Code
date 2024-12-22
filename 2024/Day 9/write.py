with open('Day 9/output.txt', 'w') as out:
    with open('Day 9/input.txt', 'r') as file:
        i = 0
        ids = 0
        number = ''
        res = 0
        count = 0
        while True:
            char = file.read(1)  # Read one character at a time
            # print(char)
            if not char:  # EOF reached
                break
            # Se for par, eh um bloco
            n = int(char)
            if i % 2 == 0:
                out.write(str(ids)*n)
                count += n
                ids += 1
            else:
                out.write('.'*n)
            i += 1
            out.write('\n')