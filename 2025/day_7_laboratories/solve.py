from typing import List


def solve_part_one(dataset: str = 'full') -> int:
    diagram = get_tachyon_manifold(dataset)
    beam_splits = 0

    def extend_beam_to_next_level(curr_row_idx: int, curr_col_idx: int) -> int:
        beam_splits = 0

        next_row_idx = curr_row_idx + 1
        left_col_idx = curr_col_idx - 1
        right_col_idx = curr_col_idx + 1

        if diagram[next_row_idx][curr_col_idx] == '.':
            diagram[next_row_idx][curr_col_idx] = '|'
        if diagram[next_row_idx][curr_col_idx] == '^':
            diagram[next_row_idx][left_col_idx] = '|'
            diagram[next_row_idx][right_col_idx] = '|'
            beam_splits += 1
        
        return beam_splits

    for idx, el in enumerate(diagram[0]):
        if el == 'S':
            beam_splits += extend_beam_to_next_level(0, idx)

    for r_idx in range(1, len(diagram) - 1):
        for c_idx in range(len(diagram[r_idx])):
            if diagram[r_idx][c_idx] == '|':
                beam_splits += extend_beam_to_next_level(r_idx, c_idx)

    return beam_splits


def solve_part_two(dataset: str = 'full') -> int:
    pass


def get_tachyon_manifold(dataset: str) -> List[List[str]]:
    diagram = []

    with open(f'./{dataset}.txt', 'r') as f:
        for row in f:
            diagram.append(list(row.strip('\n')))

    return diagram 


if __name__ == '__main__':
    print('--- Day 7: Laboratories ---')
    print('PART ONE...')
    print(f'Answer: {solve_part_one()}')
    print('PART TWO...')
    print(f'Answer: {solve_part_two()}')
