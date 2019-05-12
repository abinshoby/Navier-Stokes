#include<stdio.h>
int main(){
    int n=20;
    long long int f=1;
    for(long long int i=1;i<=n;i++)
        f*=i;
    printf("%lld",f);
    return 0;
}