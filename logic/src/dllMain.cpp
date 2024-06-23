#include <stdio.h>
#include "map.hpp"
#include "mylogic.hpp"
#include <vector>

using namespace std;

typedef unsigned char byte;

extern "C" int DllMain_Run(
  int COL, int ROW, 
  unsigned char* map_data, 
  int *x, int *y)
{
  vector<vector<int>> map(ROW, vector<int>(COL));
  Pair src, dst;
  for(int i = 0;i<ROW;++i){
    for(int j = 0;j<COL;++j){
      map[i][j] = map_data[COL * i + j];
    }
  }

  for(int i = 0;i<ROW;++i){
    for(int j = 0;j<COL;++j){
      if(map[i][j] == PLAYER){
        src.first = i;
        src.second = j;
        map[i][j] = EMPTY;
      }
      else if(map[i][j] == DESTINATION){
        dst.first = i;
        dst.second = j;
        map[i][j] = EMPTY;
      }
    }
  }
  traceStock.clear();
  printf("dst: %d,%d\nsrc: %d,%d\n\n", 
         dst.first, dst.second, src.first, src.second);
  if(aStarSearch(ROW, COL, map, src, dst)){
    if(traceStock.size() >= 2){
      *x = traceStock[1].second;
      *y = traceStock[1].first;
      printf("B %d,%d B\n", *x, *y);
      return 1;
    }
  }else{
  }
  return 0;
}
