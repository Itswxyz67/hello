import os

cpp_code = {
    "P11_1_FunctionOverloading": """#include <iostream>
using namespace std;
class Temp
{
private:
int x = 10;
double x1 = 10.1;
public:
void add(int y)
{
cout << "Value of x + y is: " << x + y << endl;
}
// Differ in the type of argument.
void add(double d)
{
cout << "Value of x1 + d is: " << x1 + d << endl;
}
// Differ in the number of arguments.
void add(int y, int z)
{
cout << "Value of x + y + z is: " << x + y + z << endl;
}
};
int main()
{
Temp t1;
t1.add(10);
t1.add(11.1);
t1.add(12,13);
return 0;
}""",
    "P11_2_OperatorOverloading": """#include <iostream>
using namespace std;
class Math
{
int num;
public:
// setter to set value
void setValue(int val)
{
num = val;
}
// overloading + operator to add values in two objects
Math operator + (Math &obj) {
Math temp;
temp.num = num + obj.num;
return (temp);
}
// overloading - operator to subtract values in two objects
Math operator - (Math &obj){
Math temp;
temp.num = num - obj.num;
return (temp);
}
// overloading * operator to multiply values in two objects
Math operator * (Math &obj){
Math temp;
temp.num = num * obj.num;
return (temp);
}
// overloading / operator to divide values in two objects
Math operator / (Math &obj){
Math temp;
temp.num = num / obj.num;
return (temp);
}
// display result value getter
void getValue(){cout << num;
}
};
int main ()
{
// created objects obj1 and obj2 to perform mathematical operations and resObj to store results
Math obj1, obj2, resObj;
// accepting the values
obj1.setValue(20);
obj2.setValue(10);
cout << "Obj 1: ";
obj1.getValue();
cout << "\\nObj 2: ";
obj2.getValue();
// assign result of obj1 and obj2 to resObj addition
resObj = obj1 + obj2;
cout << "\\n\\nObj1 + Obj2 : " ;
resObj.getValue();
// subtraction
resObj = obj1 - obj2;
cout << "\\nObj1 - Obj2 : " ;
resObj.getValue();
// multiplication
resObj = obj1 * obj2;
cout << "\\nObj1 * Obj2 : " ;
resObj.getValue();
// division
resObj = obj1 / obj2;
cout << "\\nObj1 / Obj2 : " ;
resObj.getValue();
return 0;
}""",
    "P11_3_FunctionOverriding": """#include <iostream>
using namespace std;
class Exam { // base class declaration.
public:
void colorP(){
cout<<"Black";
}
};
class Atkt: public Exam // inheriting Exam class.
{
public:
void colorP(){
cout<<"Grey";
}
};
int main(void) {
Atkt kt;
kt.colorP();
}""",
    "P11_4_PureVirtualFunction": """#include <iostream>
using namespace std;
// Abstract class
class Shape
{
public:
virtual float calculateArea() = 0; // pure virtual function.
};
class Square : public Shape
{
float a;
public:
Square(float l)
{
a = l;
}
float calculateArea()
{
return a*a;
}
};
class Circle : public Shape
{
float r;
public:
Circle(float x)
{
r = x;
}
float calculateArea()
{
return 3.14*r*r ;
}
};
class Rectangle : public Shape
{
float l;
float b;
public:
Rectangle(float x, float y)
{
l=x;
b=y;
}
float calculateArea()
{
return l*b;
}
};
int main()
{
Shape *shape;
Square s(3.4);
Rectangle r(5,6);
Circle c(7.8);
shape =&s;
int a1 =shape->calculateArea();
shape = &r;
int a2 = shape->calculateArea();
shape = &c;
int a3 = shape->calculateArea();
cout << "Area of the square is " <<a1<< endl;
cout << "Area of the rectangle is " <<a2<< endl;
cout << "Area of the circle is " <<a3<<endl;
return 0;
}""",
    "P12_ThisPointer": """#include <iostream>
using namespace std;
class Employee {
public:
int id; //data member (also instance variable)
string name; //data member(also instance variable)
float salary;
Employee(int id, string name, float salary)
{
this->id = id;
this->name = name;
this->salary = salary;
}
void display()
{
cout<<id<<" "<<name<<" "<<salary<<endl;
}
};
int main(void) {
Employee e1 =Employee(101, "Pinocchio", 890000); //creating an object of Employee
Employee e2=Employee(102, "Naruto", 59000); //creating an object of Employee
e1.display();
e2.display();
return 0;
}""",
    "P13_1_PointersBasics": """#include <iostream>
using namespace std;
void Pointers()
{
int var = 20;
int* ptr; // declare pointer variable
ptr = &var; // data type of ptr and var must be same
// assign the address of a variable to a pointer
cout << "Value at ptr = " << ptr << "\\n";
cout << "Value at var = " << var << "\\n";
cout << "Value at *ptr = " << *ptr << "\\n";
}
int main()
{
Pointers();
return 0;
}""",
    "P13_2_PointerToPointers": """#include<iostream>
using namespace std;
int main ()
{
int a;
int * ptr_b;
int ** ptr_c;
a = 1;
ptr_b = &a;
ptr_c = &ptr_b; //Get address of ptr_b
cout << a << "\\n"; //print value of a
cout << *ptr_b << "\\n"; //print value where pointer ptr_b points to
cout << ptr_b << "\\n"; //print value of pointer ptr_b
cout << *ptr_c << "\\n"; //print address of ptr_b
cout << **ptr_c << "\\n"; //print value where ptr_c points to
return 0;
}""",
    "P13_3_CallByValue": """#include<iostream>
using namespace std;
void swapping(int c, int d)
{
int temp;
temp = c;
c = d;
d = temp;
cout << "In function:\\n" << c << " \\n " << d << " \\n ";
}
int main()
{
int a,b;
a=5;
b=10;
cout << "Before Sapping :\\n " << a << " \\n " << b << " \\n ";
swapping(a,b);
cout << "After Swapping:\\n " << a << " \\n " << b << " \\n ";
return 0;
}""",
    "P13_4_CallByReference": """#include<iostream>
using namespace std;
void swapping(int *ptr_c, int *ptr_d)
{
int tmp;
tmp = *ptr_c;
*ptr_c = *ptr_d;
*ptr_d = tmp;
cout << "In function:\\n" << *ptr_c << "\\n " << *ptr_d << '\\n';
}
int main()
{
int a,b;
a=5;
b=10;
cout << "Before:\\n" << a << " \\n" << b << "\\n";
swapping(&a,&b);
cout << "After:\\n" << a << "\\n " << b << " \\n ";
}""",
    "P14_1_FileReadWrite": """#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
fstream newfile,newfile1;
newfile.open("testFile.txt",ios::out); // open a file to perform write operation using file object
if(newfile.is_open()) //checking whether the file is open
{
newfile<<"Hello World from CPP \\n"; //inserting text
newfile.close(); //close the file object
}
newfile.open("testFile.txt",ios::in); //open a file to perform read operation using file object
if (newfile.is_open()){ //checking whether the file is open
string tp;
while(getline(newfile, tp)){ //read data from file object and put it into string.
cout << tp << "\\n"; //print the data of the string
}
newfile.close(); //close the file object.
}
}""",
    "P14_2_FileWrite": """#include <iostream> // Include the input/output stream library
#include <fstream> // Include the file stream library
int main() {
// Create a new file named "InfoOnCpp.txt"
std::ofstream outputFile("InfoOnCpp.txt"); // Open/create a file named "test.txt" for writing
if (outputFile.is_open()) { // Check if the file was successfully opened
// Write some text into the file
outputFile << "C++ is a high-level, general-purpose programming language created by Danish computer scientist Bjarne Stroustrup. \\n"; // Write a line of text to the file
outputFile << "First released in 1985 as an extension of the C programming language, it has since expanded significantly over time. \\n"; // Write a line of text to the file
outputFile << "Modern C++ currently has object-oriented, generic, and functional features, in addition to facilities for low-level memory manipulation.\\n"; // Write a line of text to the file
outputFile << "It is almost always implemented in a compiled language.\\n"; // Write a line of text to the file
outputFile << "Many vendors provide C++ compilers, including the Free Software Foundation, LLVM, Microsoft, Intel, Embarcadero, Oracle, and IBM."; // Write a line of text to the file

// Close the file
outputFile.close(); // Close the file after writing
std::cout << "Text has been written to the file." << std::endl; // Display a success message
} else {
std::cout << "Failed to create the file." << std::endl; // Display an error message if file creation failed
}
return 0; // Return 0 to indicate successful execution
}""",
    "P14_3_FileRead": """#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
fstream newfile;

newfile.open("InfoOnCpp.txt",ios::in); //open a file to perform read operation using file object
if (newfile.is_open()){ //checking whether the file is open
string tp;
while(getline(newfile, tp)){ //read data from file object and put it into string.
cout << tp << "\\n"; //print the data of the string
}
newfile.close(); //close the file object.
}
return 0;
}""",
    "P14_4_FileAppend": """#include <iostream>
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
}""",
    "P14_5_BinaryFile": """#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
using namespace std;
struct Student
{
int roll_no;
char name[50]; // Changed string to char array for binary safety
};
int main() {
ofstream wbf("student.dat", ios::out | ios::binary);
if (!wbf) {
cout << "Cannot open file!" << endl;
return 1;
}
Student wstu[3];
wstu[0].roll_no = 101;
strcpy(wstu[0].name, "Ambika");
wstu[1].roll_no = 102;
strcpy(wstu[1].name, "Chandra");
wstu[2].roll_no = 103;
strcpy(wstu[2].name, "Madhu");
for (int i = 0; i < 3; i++)
wbf.write((char * ) & wstu[i], sizeof(Student));
wbf.close();

ifstream rbf("student.dat", ios::in | ios::binary);
if (!rbf)
{
cout << "Cannot open file!" << endl;
return 1;
}

Student rstu[3];
for (int i = 0; i < 3; i++)
rbf.read((char * ) & rstu[i], sizeof(Student));
rbf.close();

cout << "Student's Details:" << endl;
for (int i = 0; i < 3; i++)
{
cout << "Roll No: " << rstu[i].roll_no << endl;
cout << "Name: " << rstu[i].name << endl;
cout << endl;
}
return 0;
}"""
}

os.makedirs("cpp_practicals", exist_ok=True)
for name, code in cpp_code.items():
    with open(f"cpp_practicals/{name}.cpp", "w") as f:
        f.write(code)
print("Extracted 14 C++ files.")
