#include <stdio.h>
#include <conio.h>
void main(){
  int a, b, c;
  printf("Please enter 3 numbers a, b and c: ");
  scanf("%d %d %d",&a,&b,&c);
  if (a>b && a>c){
    printf("Number A is the greatest.");
  }
  else if (b>a && b>c) {
    printf("Number B is the greatest.");
  }
  else{
    printf("The number C is the greatest.");
  }
}
