// C++ code to linearly search x in arr[]. If x 
// is present then return its location, otherwise 
// return -1 

#include <stdio.h> 

int search(long long int arr[], long long int n, long long int x) 
{ 
	long long int i; 
	for (i = 0; i < n; i++) 
		if (arr[i] == x) 
			return i; 
	return -1; 
} 

int main(void) 
{ 
	long long int arr[10000]; 
    for(int i=0;i<10000;i++)
        arr[i]=i;
	long long int x = 999; 
	long long int n = sizeof(arr) / sizeof(arr[0]); 
	long long int result = search(arr, n, x); 
	(result == -1) ? printf("Element is not present in array") 
				: printf("Element is present at index %lld", 
							result); 
	return 0; 
} 
