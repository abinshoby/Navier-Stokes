#include<stdio.h>
 
void DFS(long long int);
long long int G[10000][10000],visited[10000],n;    //n is no of vertices and graph is sorted in array G[10][10]
 
int main()
{
    long long int i,j;
    //printf("Enter number of vertices:");
   
	//scanf("%d",&n);
    n=10000;
    //read the adjecency matrix
	//printf("\nEnter adjecency matrix of the graph:");
   
	for(i=0;i<n;i++)
       for(j=0;j<n;j++)
			//scanf("%d",&G[i][j]);
            G[i][j]=1;
 
    //visited is initialized to zero
   for(i=0;i<n;i++)
        visited[i]=0;
 
    DFS(0);
    return 0;
}
 
void DFS(long long int i)
{
    long long int j;
	printf("\n%lld",i);
    visited[i]=1;
	
	for(j=0;j<n;j++)
       if(!visited[j]&&G[i][j]==1)
            DFS(j);
}