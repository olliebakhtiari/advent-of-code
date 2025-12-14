from typing import List


def solve_part_one(dataset: str = 'full') -> int:
   total = 0

   for bank in get_banks(dataset):
      total += find_largest_joltage_from_turning_on_two_batteries(bank) 

   return total


def find_largest_joltage_from_turning_on_two_batteries(bank: List[str]) -> int:
    first, second = bank[0], '0' 

    for i in range(1, len(bank)):
        if bank[i] > first and i != len(bank) - 1:
            first = bank[i]
            second = '0'
        elif bank[i] > second:
            second = bank[i]

    return int(first + second)


def solve_part_two(dataset: str = 'full') -> int:
    return sum(find_largest_with_exactly_12_batteries(bank) for bank in get_banks(dataset))


def find_largest_with_exactly_12_batteries(bank: str) -> int:
    optimal_bank = ['0' for _ in range(12)]
    i = 0
    while i < len(bank):
        j = max(0, i - len(bank) + 12) 
        while j < len(optimal_bank):
            if bank[i] > optimal_bank[j]:
                optimal_bank[j] = bank[i]
                for k in range(j + 1, len(optimal_bank)):
                    optimal_bank[k] = '0'
                j = len(optimal_bank) 
            else:
                j += 1
        i += 1

    total = 0
    for i in range(len(optimal_bank)):
        total += (int(optimal_bank[i]) * pow(10, len(optimal_bank) - i - 1))

    return total


def get_banks(dataset: str):
   with open(f'./{dataset}.txt', 'r') as f:
      for bank in f:
          yield bank.strip()


if __name__ == '__main__':
    print('--- Day 3: Lobby ---')
    print('PART ONE...')
    print(f'Answer: {solve_part_one()}')
    print('PART TWO...')
    print(f'Answer: {solve_part_two()}')
