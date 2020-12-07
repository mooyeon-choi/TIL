#include <iostream>
using namespace std;
int A, B;
int main()
{
  cin >> A >> B;
  cout << B % 10 * A << '\n'
       << B / 10 % 10 * A << '\n'
       << B / 100 * A << '\n'
       << B * A;
}