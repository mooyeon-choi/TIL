#include <iostream>

using namespace std;

int i, N, result = 0, num;

int main() {
	cin >> N;
	for (i = N/10; i < N; i++) {
		result = i;
		num = i;
		while (num > 0) {
			result += num % 10;
			num /= 10;
		}
		if (result == N) break;
	}
	if (i == N) i = 0;
	cout << i;
}