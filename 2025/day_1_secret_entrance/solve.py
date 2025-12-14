def solve_part_one(dataset: str = 'full') -> int:
    hit_zero_count = 0
    dial_position = 50

    for rotation in get_rotations(dataset):
        rotation_direction = rotation[0]
        rotation_distance = int(''.join(rotation[1::]))

        dial_position += rotation_distance * (-1 if rotation_direction == 'L' else 1)
        dial_position %= 100

        hit_zero_count += int(dial_position == 0) 
    
    return hit_zero_count


def solve_part_two(dataset: str = 'full') -> int:
    hit_zero_count = 0
    dial_position = 50
    prev_pos_was_zero = False

    for rotation in get_rotations(dataset):
        rotation_direction = rotation[0]
        rotation_distance = int(''.join(rotation[1::]))

        dial_position += rotation_distance * (-1 if rotation_direction == 'L' else 1)
        
        if dial_position == 0:
            hit_zero_count += 1
        elif dial_position >= 100:
            hit_zero_count += int(dial_position / 100)
        elif dial_position < 0:
            hit_zero_count += (int(dial_position / 100) * -1) + (int(not prev_pos_was_zero))
    
        dial_position %= 100
        prev_pos_was_zero = dial_position == 0

    return hit_zero_count 


def get_rotations(dataset: str):
   with open(f'./{dataset}.txt', 'r') as f:
      for rotation in f:
          yield rotation.strip()


if __name__ == '__main__':
    print('--- Day 1: Secret Entrance ---')
    print('PART ONE...')
    print(f'Answer: {solve_part_one()}')
    print('PART TWO...')
    print(f'Answer: {solve_part_two()}')
