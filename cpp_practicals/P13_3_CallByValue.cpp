#include<iostream>
using namespace std;
void swapping(int c, int d)
{
int temp;
temp = c;
c = d;
d = temp;
cout << "In function:\n" << c << " \n " << d << " \n ";
}
int main()
{
int a,b;
a=5;
b=10;
cout << "Before Sapping :\n " << a << " \n " << b << " \n ";
swapping(a,b);
cout << "After Swapping:\n " << a << " \n " << b << " \n ";
return 0;
}