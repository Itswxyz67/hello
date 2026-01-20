#include<iostream>
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
}