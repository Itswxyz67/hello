#include <iostream>
using namespace std;
void Pointers()
{
int var = 20;
int* ptr; // declare pointer variable
ptr = &var; // data type of ptr and var must be same
// assign the address of a variable to a pointer
cout << "Value at ptr = " << ptr << "\n";
cout << "Value at var = " << var << "\n";
cout << "Value at *ptr = " << *ptr << "\n";
}
int main()
{
Pointers();
return 0;
}