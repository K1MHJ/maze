#pragma once
#include <vector>
using namespace std;

typedef pair<int, int> Pair;

// A structure to hold the necessary parameters
struct cell {
    // Row and Column index of its parent
    // Note that 0 <= i <= ROW-1 & 0 <= j <= COL-1
    int parent_i, parent_j;
    // f = g + h
    double f, g, h;
};
extern vector<pair<int, int>> traceStock;

// Creating a shortcut for int, int pair type
bool aStarSearch(
  int maxrow, int maxcol, 
  vector<vector<int>>& grid, 
  Pair src, Pair dest);

