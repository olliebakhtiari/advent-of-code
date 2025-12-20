#include <vector>
#include <numeric>
#include <algorithm>
#include <array>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cmath>

class CircuitNetwork {
    public:
        explicit CircuitNetwork(std::size_t network_size)
        : representative_of_circuit_(std::vector<std::size_t>(network_size)), 
          circuit_size_(std::vector<std::size_t>(network_size, 1)) {
            std::iota(representative_of_circuit_.begin(), representative_of_circuit_.end(), 0);
          }
       
        bool is_representative(std::size_t circuit) const {
            return representative_of_circuit_[circuit] == circuit;
        }

        std::size_t find_representative(std::size_t circuit) {
            if (is_representative(circuit)) {
                return circuit;
            }

            return representative_of_circuit_[circuit] = find_representative(representative_of_circuit_[circuit]);
        }

        std::size_t get_circuit_size(std::size_t representative) const {
            return circuit_size_[representative];
        }

        void union_circuits(std::size_t a, std::size_t b) {
            std::size_t a_rep = find_representative(a);
            std::size_t b_rep = find_representative(b);

            if (a_rep != b_rep) {
                if (circuit_size_[a_rep] < circuit_size_[b_rep]) {
                    std::swap(a_rep, b_rep);
                }
                representative_of_circuit_[b_rep] = a_rep;
                circuit_size_[a_rep] += circuit_size_[b_rep];
            }
        }

    private:
        std::vector<std::size_t> representative_of_circuit_;
        std::vector<std::size_t> circuit_size_;
};

struct Connection {
    std::size_t from;
    std::size_t to;
    long long distance_squared;
};

std::vector<std::array<int, 3>> get_junction_boxes(const std::string &dataset = "full") {
	std::string path = "./" + dataset + ".txt";
	std::ifstream fin(path);

	std::vector<std::array<int, 3>> rows;
	std::string line;
	while (getline(fin, line)) {
		if (line.empty()) continue;

		std::stringstream ss(line);
		std::string token;
		std::array<int, 3> vals = {0,0,0};

		int i = 0;
		while (getline(ss, token, ',') && i < 3) {
			auto l = token.find_first_not_of(" \t\r\n");
			auto r = token.find_last_not_of(" \t\r\n");
			token = l == std::string::npos ? "" : token.substr(l, r - l + 1);
			vals[i] = std::stoi(token);
			++i;
		}
		rows.emplace_back(vals);
	}

	return rows;
}

long long compute_distance_squared(const std::array<int, 3>& a, const std::array<int, 3>& b) {
    return std::pow(a[0] - b[0], 2) + std::pow(a[1] - b[1], 2) + std::pow(a[2] - b[2], 2);
}

long long solve_part_one(const std::vector<std::array<int, 3>>& junction_boxes) {
    std::vector<Connection> connections;
    for (size_t i = 0; i < junction_boxes.size(); ++i) {
        for (size_t j = i + 1; j < junction_boxes.size(); ++j) {
            connections.emplace_back(
                Connection{i, j, compute_distance_squared(junction_boxes[i], junction_boxes[j])}
            );
        }
    }
    std::sort(
        connections.begin(), 
        connections.end(), 
        [](const Connection& a, const Connection& b){ return a.distance_squared < b.distance_squared;}
    );

    CircuitNetwork network(junction_boxes.size());
    for (size_t i = 0; i < 1000; ++i) {
        network.union_circuits(connections[i].from, connections[i].to);
    }

    std::vector<std::size_t> unique_circuit_sizes;
    for (size_t i = 0; i < junction_boxes.size(); ++i) {
        if (network.is_representative(i)) {
            unique_circuit_sizes.emplace_back(network.get_circuit_size(i));
        }
    }
    std::sort(unique_circuit_sizes.rbegin(), unique_circuit_sizes.rend());

    long long answer = 1;
    for (size_t i = 0; i < 3; ++i) {
        answer *= unique_circuit_sizes[i];
    }

    return answer;
}

long long solve_part_two(const std::vector<std::array<int, 3>>& junction_boxes) {
	return 0;
}

int main(int argc, char **argv) {
	std::string dataset = "full";

	if (argc > 1) {
        dataset = argv[1];
    }

	std::cout << "--- Day 8: Playground ---\n";
    auto junction_boxes = get_junction_boxes(dataset);
	std::cout << "PART ONE..." << '\n';
	std::cout << "Answer: " << solve_part_one(junction_boxes) << '\n';
	std::cout << "PART TWO..." << '\n';
	std::cout << "Answer: " << solve_part_two(junction_boxes) << '\n';

	return 0;
}
