#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main()
{
  int number=3, x=2, r, y, root;
  while (number>2) {
    r=number%x;
    y=number/x;
    root=sqrt(number);
    if (r==0){
      number=number+1;
      x=2;
      continue;
    }
    if (x>root) {
      printf("Found Prime: %d.\n", number);
      number=number+1;
      x=2;
      continue;
    }
    else{
      x=x+1;
      continue;
    }
  }
  return 0;
}
