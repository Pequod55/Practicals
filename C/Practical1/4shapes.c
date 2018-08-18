#include <stdio.h>
#include <conio.h>
void main(){
  int area, shape, unit1, unit2;
  printf("Which shape to find area of?:\nSquare(1) Rectangle(2) Rhombus(3) or Parallelogram(4): ");
  scanf("%d",&shape);
  if (shape=1){
    printf("Please enter the side of the square in cm: ");
    scanf("%d",&unit1);
    area=unit1*unit1;
    printf("%d cm^2 is the area of the Square.\n\n\n",area);
  }
  else if (shape=2){;
    printf("Enter the width and breadth of the rectangle in cm: ");
    scanf("%d %d",&unit1,&unit2);
    area=unit1*unit2;
    printf("%d cm^2 is the area of the Rectangle.\n\n\n",area);
  }
  else if (shape=3) {
    printf("Enter the two diagonals of the Rhombus: ");
    scanf("%d %d",&unit1,&unit2);
    area=(unit1*unit2)/2;
    printf("%d cm^2 is the area of the Rhombus.\n\n\n",area);
  }
  else if (shape=4) {
    printf("Enter the base and height of the Parallelogram");
    scanf("%d %d",&unit1,&unit2);
    area=unit1*unit2;
    printf("%d cm^2 is the area of the Parallelogram.",area);
  }
}
