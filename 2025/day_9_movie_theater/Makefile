CXX = g++
CXXFLAGS = -std=c++20 -Wall -Wextra -Wpedantic -O2

BIN = $(HOME)/.cache/aoc-build/day9/day9
SRC = solve.cpp

build:
	mkdir -p $(dir $(BIN))
	$(CXX) $(CXXFLAGS) $(SRC) -o $(BIN)

run: build
	$(BIN)

clean:
	rm -f $(BIN)

.PHONY: build run clean
