#include<iostream>
using namespace std;
int main ()
{
int a;
int * ptr_b;
int ** ptr_c;
a = 1;
ptr_b = &a;
ptr_c = &ptr_b; //Get address of ptr_b
cout << a << "\n"; //print value of a
cout << *ptr_b << "\n"; //print value where pointer ptr_b points to
cout << ptr_b << "\n"; //print value of pointer ptr_b
cout << *ptr_c << "\n"; //print address of ptr_b
cout << **ptr_c << "\n"; //print value where ptr_c points to
return 0;
}