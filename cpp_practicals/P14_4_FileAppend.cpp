#include <iostream>
#include <fstream>
using namespace std;
int main()
{
ofstream my_file("InfoOnCpp.txt", ios::app); // open a text file for appending
// if the file doesn't open successfully, print an error message
if(!my_file) {
cout << "Failed to open the file for appending." << endl;
return 1;
}
// append multiple lines to the file
my_file << "Attempted to open file in append mode" << endl;
my_file << "and type the data" << endl;
my_file << "It’s a Success" << endl;
my_file.close(); // close the file
return 0;
}