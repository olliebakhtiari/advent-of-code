def solve_part_one(dataset: str = 'full') -> int:
    total = 0

    for start, end in get_id_ranges(dataset):
        for i in range(int(start), int(end)):
            if is_twice_repeating_seq(str(i)):
                total += i
    
    return total


def is_twice_repeating_seq(num: str) -> bool:
    return num[:len(num) // 2] == num[len(num) // 2::] if len(num) % 2 == 0 else False


def solve_part_two(dataset: str = 'full') -> int:
    total = 0

    for start, end in get_id_ranges(dataset):
        for i in range(int(start), int(end) + 1):
            if is_at_least_twice_repeating_seq(str(i)):
                total += i
    
    return total


def is_at_least_twice_repeating_seq(num: str) -> bool:
    possibilities = []
    poss_len = len(num) // 2
    while poss_len:
        if len(num) % poss_len == 0: 
            possibilities.append(num[:poss_len])
        poss_len -= 1

    for i in range(len(possibilities)):
        is_valid = True
        for j in range(len(possibilities[i]), len(num), len(possibilities[i])):
            if num[j:j + len(possibilities[i])] != possibilities[i]:
                is_valid = False
                break
        if is_valid:
            return True
    
    return False 


def get_id_ranges(dataset):
    with open(f'./{dataset}.txt', 'r') as f:
        for r in f.read().strip().split(','):
            start, end = r.strip().split('-')
            yield start, end


if __name__ == '__main__':
    print('--- Day 2: Gift Shop ---')
    print('PART ONE...')
    print(f'Answer: {solve_part_one()}')
    print('PART TWO...')
    print(f'Answer: {solve_part_two()}')