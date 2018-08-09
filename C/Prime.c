#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
  int number, root, x=2, r, y;
  printf("Please enter the number: ");
  scanf("%d", &number);
  root=sqrt(number);
  while (x<root) {
    r=number%x;
    y=number/x;
    if (r==0) {
      printf("The given number is not a Prime.");
      exit(0);
    }
    else {
      x=x+1;
    }
  }
  printf("The given number is a Prime.\n");
  return 0;
}
