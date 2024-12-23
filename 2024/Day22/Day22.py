with open("2024/Day22/input.txt", 'r') as file:
    lines = file.readlines()

def get_secret_number_sequences(sequences, secret_number, iters):
    changes = [None]
    prices = [secret_number % 10]
    visited = [] # to count only with a sequence the first time it appears
    for it in range(iters):
        # step one
        times64_number = secret_number * 64
        secret_number = (times64_number ^ secret_number) % 16777216
        # step two
        divide32_number = secret_number // 32
        secret_number = (divide32_number ^ secret_number) % 16777216
        # step three
        times2048_number = secret_number * 2048
        secret_number = (times2048_number ^ secret_number) % 16777216

        price = secret_number % 10 # calculate price
        changes.append(price-prices[-1]) # calculate change: price - prev_price
        prices.append(price) # add price to prices list

        # get price of each sequence
        if it > 2:
            key = (changes[-4], changes[-3], changes[-2], changes[-1])
            if key not in visited:
                visited.append(key)
                if key in sequences:
                    # if sequence already in sequences dict, add the price
                    sequences[key] += price
                else:
                    # if not, add sequences to dict
                    sequences[key] = price

    return secret_number, sequences

def main():
    sequences = {}
    res = 0
    for line in lines:
        number = int(line.strip())
        secret_number, sequences = get_secret_number_sequences(sequences, number, 2000)
        res += secret_number

    # get sequence with maximum price
    max_key = ()
    max_value = 0
    for key in sequences:
        if sequences[key] > max_value:
            max_value = sequences[key]
            max_key = key

    print('Part 1:', res)
    print('Part 2:', sequences[max_key])

main()