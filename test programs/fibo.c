#include <stdio.h>
 
int main()
{
  long long int n, first = 0, second = 1, next, c;
 
  //printf("Enter the number of terms\n");
  //scanf("%d", &n);
  n=1000000;
 
  //printf("First %d terms of Fibonacci series are:\n", n);
 
  for (c = 0; c < n; c++)
  {
    if (c <= 1)
      next = c;
    else
    {
      next = first + second;
      first = second;
      second = next;
    }
    printf("%lld\n", next);
  }
 
  return 0;
}