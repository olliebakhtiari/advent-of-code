from typing import List

class Solution:
    def __init__(self, dataset: str = 'full'):
        self._grid = self._get_grid(dataset)

        # {"target_position": (r_idx_move, c_idx_move)}
        self._movements = {
           "top_left": (-1, -1),
           "top": (-1, 0),
           "top_right": (-1, 1),
           "left": (0, -1),
           "right": (0, 1),
           "bottom_left": (1, -1),
           "bottom": (1, 0),
           "bottom_right": (1, 1), 
        }

    def solve_part_one(self) -> int:
        total = 0

        for r_idx in range(len(self._grid)):
            for c_idx, col in enumerate(self._grid[r_idx]):
                if col == '@':
                    total += int(self._can_be_accessed(r_idx, c_idx))
        
        return total

    def solve_part_two(self) -> int:
        total = 0

        removed_item_in_prev_iter = True
        while removed_item_in_prev_iter: 
            removed_item_in_prev_iter = False
            for r_idx in range(len(self._grid)):
                for c_idx, col in enumerate(self._grid[r_idx]):
                    if col == '@' and self._can_be_accessed(r_idx, c_idx):
                        total += 1
                        self._grid[r_idx][c_idx] = 'x'
                        removed_item_in_prev_iter = True

        return total 

    def _can_be_accessed(self, r_idx: int, c_idx: int) -> bool:
        return sum(
            int(self._is_grid_loc_a_roll(r_idx + r_move, c_idx + c_move))
            for r_move, c_move 
            in self._movements.values()
        ) < 4 
    
    def _is_grid_loc_a_roll(self, r_idx: int, c_idx: int) -> bool:
        if (r_idx < 0 or r_idx >= len(self._grid)) or (c_idx < 0 or c_idx >= len(self._grid[0])):
            return False

        return self._grid[r_idx][c_idx] == '@'

    def _get_grid(self, dataset: str) -> List[List[str]]:
        grid = []
        with open(f'./{dataset}.txt', 'r') as f:
            for row in f:
                grid.append(list(row.strip()))

        return grid


if __name__ == '__main__':
    solution = Solution()
    print('--- Day 4: Printing Department ---')
    print('PART ONE...')
    print(f'Answer: {solution.solve_part_one()}')
    print('PART TWO...')
    print(f'Answer: {solution.solve_part_two()}')