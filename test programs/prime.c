#include<stdio.h>
 
int main()
{
   long long int n, i = 3, count, c;
 
   n=100000;
 
   if ( n >= 1 )
   {
      //printf("First %lld prime numbers are :\n",n);
      //printf("2\n");
   }
 
   for ( count = 2 ; count <= n ;  )
   {
      for ( c = 2 ; c <= i - 1 ; c++ )
      {
         if ( i%c == 0 )
            break;
      }
      if ( c == i )
      {
         //printf("%lld\n",i);
         count++;
      }
      i++;
      
   }     
   return 0;
}    
 
  