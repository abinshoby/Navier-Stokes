// #include <math.h>
// double derive(double (*f)(double), double x0)
// {
//     const double delta = 1.0e-6; // or similar
//     double x1 = x0 - delta;
//     double x2 = x0 + delta;
//     double y1 = f(x1);
//     double y2 = f(x2);
//     return (y2 - y1) / (x2 - x1);
// }

// // call it as follows:
// int main(){

// double der = derive(sin, 0.0);
// printf("%lf\n", der); // should be around 1.0
// return 0;
// }


/* CPP Program to find approximation 
of a ordinary differential equation 
using euler method.*/
#include <stdio.h> 

// Consider a differential equation 
// dy/dx=(x + y + xy) 
float func(float x, float y) 
{ 
	return (x + y + x * y); 
} 

// Function for Euler formula 
void euler(float x0, float y, float h, float x) 
{ 
	float temp = -0; 

	// Iterating till the point at which we 
	// need approximation 
	while (x0 < x) { 
		temp = y; 
		y = y + h * func(x0, y); 
		x0 = x0 + h; 
	} 

	// Printing approximation 
	printf( "Approximate solution at x = %f is %f\n" ,x,y); 
} 

// Driver program 
int main() 
{ 
	// Initial Values 
	float x0 = 0; 
	float y0 = 1; 
	float h = 0.025; 

	// Value of x at which we need approximation 
	float x = 0.1; 

	euler(x0, y0, h, x); 
	return 0; 
} 
