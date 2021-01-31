#include <iostream>
using namespace std;
string A;
int B;
int main()
{
  cin >> A >> B;
  cout << (A + B) % C << '\n'
       << (A % C + B % C) % C << '\n'
       << A * B % C << '\n'
       << (A % C * (B % C)) % C;
}