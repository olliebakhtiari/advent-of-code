from typing import List


def solve_part_one(dataset: str = 'full') -> int:
    worksheet = get_worksheet_for_part_one(dataset)
    equations = [f'{worksheet[-1][c_idx]}'.join(worksheet[r_idx][c_idx] for r_idx in range(len(worksheet) - 1)) for c_idx in range(len(worksheet[0]))]
    return sum(eval(eq) for eq in equations) 


def solve_part_two(dataset: str = 'full') -> int:
    worksheet = get_worksheet_for_part_two(dataset)

    columns = [[worksheet[r_idx][c_idx] for r_idx in range(len(worksheet) - 1)] + [worksheet[-1][c_idx]] for c_idx in range(len(worksheet[0]))]
    equations = []

    for col_idx in range(len(columns) - 1, -1, -1):
        symbol = columns[col_idx].pop(-1)[0]
        max_len = len(max(columns[col_idx], key=len))
        nums = []
        for ch_idx in range(max_len - 1, -1, -1):
            num = []
            for r_idx in range(len(columns[col_idx])):
                r = columns[col_idx][r_idx]
                if ch_idx < len(r):
                    num.append(r[ch_idx].strip())
            nums.append(''.join(num))
        equations.append(f'{symbol}'.join(n for n in nums if n))

    return sum(eval(eq) for eq in equations) 


def get_worksheet_for_part_one(dataset: str) -> List[List[str]]:
    worksheet = []
    with open(f'./{dataset}.txt', 'r') as f:
        for row in f:
            worksheet.append([v for v in row.strip('\n').split(' ') if v != ''])

    return worksheet 


def get_worksheet_for_part_two(dataset: str) -> List[List[str]]:
    worksheet = []
    with open(f'./{dataset}.txt', 'r') as f:
        for row in f:
            worksheet.append(row.strip('\n'))

    symbol_indices = []
    for idx, el in enumerate(worksheet[-1]):
        if el != ' ':
            symbol_indices.append(idx) 

    for idx, row in enumerate(worksheet):
        worksheet[idx] = []
        for i in range(len(symbol_indices) - 1):
            worksheet[idx].append(row[symbol_indices[i]:symbol_indices[i + 1]])
        worksheet[idx].append(row[symbol_indices[-1]::])

    return worksheet 


if __name__ == '__main__':
    print('--- Day 6: Trash Compactor ---')
    print('PART ONE...')
    print(f'Answer: {solve_part_one()}')
    print('PART TWO...')
    print(f'Answer: {solve_part_two()}')