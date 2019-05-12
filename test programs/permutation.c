#include<stdio.h>
#include<string.h>
#define N 400
 
void print(long long int *num, long long int n)
{
    long long int i;
    for ( i = 0 ; i < n ; i++)
        printf("%lld ", num[i]);
    printf("\n");
}
int main()
{
    long long int num[N];
    long long int *ptr;
    long long int temp;
    long long int i, n, j;
    //printf("\nHow many number you want to enter: ");
      //  scanf("%d", &n);
      n=400;
    //printf("\nEnter a list of numbers to see all combinations:\n");
    for (i = 0 ; i < n; i++)
        num[i]=i;
    for (j = 1; j <= n; j++) {
        for (i = 0; i < n-1; i++) {
            temp = num[i];
            num[i] = num[i+1];
            num[i+1] = temp;
            print(num, n);
	}
    }
    return 0;
}