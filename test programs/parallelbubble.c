// For k = 0 to n-2
// If k is even then
//     for i = 0 to (n/2)-1 do in parallel
//         If A[2i] > A[2i+1] then
//             Exchange A[2i] ↔ A[2i+1]
// Else
//     for i = 0 to (n/2)-2 do in parallel
//         If A[2i+1] > A[2i+2] then
//             Exchange A[2i+1] ↔ A[2i+2]
// Next k
#include<stdio.h>
void swap(int *xp, int *yp) 
{ 
    int temp = *xp; 
    *xp = *yp; 
    *yp = temp; 
} 
  
// A function to implement bubble sort 
void bubbleSort(int A[], int n) 
{ 
   int i, j; 
   for (int k = 0; i < n-2; i++)  {     
  
       // Last i elements are already in place    
    //    for (j = 0; j < n-i-1; j++)  
    //        if (arr[j] > arr[j+1]) 
    //           swap(&arr[j], &arr[j+1]); 

    if(k%2==0){

        for( int i = 0 ;i<(n/2);i++) {
        if( A[2*i] > A[2*i+1] ){
           
            swap(&A[2*i],&A[2*i+1]);

    }
    }
    }
    else{
        for(int i = 0 ;i<= (n/2)-2 ;i++){
        if( A[2*i+1] > A[2*i+2]) 
            swap(&A[2*i+1] ,&A[2*i+2]);
        }

    }
   }

} 
void printArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", arr[i]); 
    printf("n"); 
} 
  
#include<stdio.h>
int main(){

     int arr[] = {64, 34, 25, 12, 22, 11, 90,100,20,10,30,10,22,44,50,99,1000,22,33,11}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    bubbleSort(arr, n); 
    printf("Sorted array: \n"); 
    printArray(arr, n); 
    return 0; 
}