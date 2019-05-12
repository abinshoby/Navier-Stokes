#include<stdio.h>
 #include<stdlib.h>
void create(long long int []);
void down_adjust(long long int [],long long int);
 
int main()
{
	long long int heap[100000],n,i,last,temp;
	//printf("Enter no. of elements:");
	//scanf("%d",&n);
    n=100000;
	printf("\nEnter elements:");
	for(i=1;i<=n;i++)
		//scanf("%d",&heap[i]);
        heap[i]=rand()%10000;
	
	//create a heap
	heap[0]=n;
	create(heap);
	
	//sorting
	while(heap[0] > 1)
	{
		//swap heap[1] and heap[last]
		last=heap[0];
		temp=heap[1];
		heap[1]=heap[last];
		heap[last]=temp;
		heap[0]--;
		down_adjust(heap,1);
	}
 
	//print sorted data
	printf("\nArray after sorting:\n");
	for(i=1;i<=n;i++)
		printf("%lld ",heap[i]);
    return 0;
}
 
void create(long long int heap[])
{
	long long int i,n;
	n=heap[0]; //no. of elements
	for(i=n/2;i>=1;i--)
		down_adjust(heap,i);
}
 
void down_adjust(long long int heap[],long long int i)
{
	long long int j,temp,n,flag=1;
	n=heap[0];
	
	while(2*i<=n && flag==1)
	{
		j=2*i;	//j points to left child
		if(j+1<=n && heap[j+1] > heap[j])
			j=j+1;
		if(heap[i] > heap[j])
			flag=0;
		else
		{
			temp=heap[i];
			heap[i]=heap[j];
			heap[j]=temp;
			i=j;
		}
	}
}