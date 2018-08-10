#include "stdio.h"
int main() {
  int a;
  int* p;
  a=1000;
  p=&a;
  printf("%d \n",*p);
  return 0;
}
