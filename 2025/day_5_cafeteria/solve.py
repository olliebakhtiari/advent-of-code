from typing import List, Tuple


RANGE_START = 0
RANGE_END = 1


def solve_part_one(dataset: str = 'full') -> int:
    id_ranges, ids = get_ingredients_db(dataset)
    ids.sort() 

    fresh_count = 0
    ids_idx = 0 
    id_ranges_idx = 0 

    while ids_idx < len(ids) and id_ranges_idx < len(id_ranges):
        start, end = id_ranges[id_ranges_idx]
        if ids[ids_idx] < start:
            ids_idx += 1
        elif ids[ids_idx] > end:
            id_ranges_idx += 1
        else:
            fresh_count += 1
            ids_idx += 1 

    return fresh_count


def solve_part_two(dataset: str = 'full') -> int:
    id_ranges, _ = get_ingredients_db(dataset)

    total = 0
    for id_range in id_ranges:
        total += id_range[RANGE_END] - id_range[RANGE_START] + 1

    return total


def get_ingredients_db(dataset: str) -> Tuple[List[Tuple[int, int]], List[int]]:
    add_to_ranges = True
    id_ranges = []
    ids = []

    with open(f'./{dataset}.txt', 'r') as f:
        for row in f:
            if row == '\n':
                add_to_ranges = False
            elif add_to_ranges:
                id_ranges.append(tuple(map(int, row.strip().split('-'))))
            else:
                ids.append(int(row.strip()))

    return merge_overlapping_ranges(id_ranges), ids


def merge_overlapping_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    merged = []
    sorted_ranges_by_start = sorted(ranges, key=lambda x: x[0])
    i = 0

    while i < len(sorted_ranges_by_start):
        curr_max_end = sorted_ranges_by_start[i][RANGE_END]
        j = i + 1
        while j < len(sorted_ranges_by_start) and curr_max_end >= sorted_ranges_by_start[j][RANGE_START]:
            curr_max_end = max(curr_max_end, sorted_ranges_by_start[j][RANGE_END])
            j += 1
        merged.append((sorted_ranges_by_start[i][RANGE_START], curr_max_end))
        i = j

    return merged


if __name__ == '__main__':
    print('--- Day 5: Cafeteria ---')
    print('PART ONE...')
    print(f'Answer: {solve_part_one()}')
    print('PART TWO...')
    print(f'Answer: {solve_part_two()}')