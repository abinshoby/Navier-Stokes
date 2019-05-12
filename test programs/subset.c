#include<stdio.h>
#include<math.h>
#include<stdlib.h>

void subset(long long  int set[],long long  int n){
	
	long long int s_n=pow(2,n);
	long int subsets[s_n][n];
	
	for(long long int t=0;t<s_n;t++){
		for(long long int j=0;j<n;j++)
			subsets[t][j]=-1;
	}
	for( long long int i=0;i<s_n;i++){
		long long int p=i;
		long long int j=n-1;
		long long int k=n-1;
		while(p>0){
			long long int q=p>>1;//shifted value
			long long int c=(p-(q<<1));//carry
			printf("%lld\n",c);
			if(c==1){
				subsets[i][k--]=set[j];
				
				}
			p=q;
			j--;
		}
	}
	for(long long int t=0;t<s_n;t++){
		for(long long int j=0;j<n;j++)
			printf("%lld\t",subsets[t][j]);
		printf("\n");
	}
}
				
	
int main(){
	long long int set[10];
	for(long long  int i=0;i<10;i++)
		set[i]=i;
	subset(set,10);
	return 0;
	
	
	
}
