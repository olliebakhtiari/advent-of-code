#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

struct Position {
	long long x;
	long long y;
};

std::vector<Position> get_red_tile_positions(std::string dataset) {
	std::string line;
	std::size_t comma_pos{0};
	std::vector<Position> positions;
	std::ifstream tile_positions("./" + std::move(dataset) + ".txt");

	while (getline(tile_positions, line)) {
		comma_pos = line.find(",");
		Position pos{
			std::stoll(line.substr(0, comma_pos)), 
			std::stoll(line.substr(comma_pos + 1))
		};
		positions.emplace_back(pos);
	}

	return positions;
}

long long solve_part_one(std::vector<Position> positions) {
	long long largest_area{0};
	long long curr_area{0};

	for (std::size_t i = 0; i < positions.size(); ++i) {
		for (std::size_t j = i + 1; j < positions.size(); ++j) {
			curr_area = (std::abs(positions[j].x - positions[i].x) + 1)
					* (std::abs(positions[j].y - positions[i].y) + 1);
			largest_area = std::max(largest_area, curr_area);
		}
	}

	return largest_area;
}

long long solve_part_two() {
	return 0;
}

int main() {
	std::string dataset = "full";

	std::cout << "--- Day 9: Movie Theater ---\n";
	auto red_tile_positions = get_red_tile_positions(dataset);

	for (auto& p : red_tile_positions) {
		std::cout << p.x << ", " << p.y << "\n";
	}

	std::cout << "PART ONE..." << '\n';
	std::cout << "Answer: " << solve_part_one(red_tile_positions) << '\n';
	std::cout << "PART TWO..." << '\n';
	std::cout << "Answer: " << solve_part_two() << '\n';

	return 0;
}
