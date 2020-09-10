#include <iostream>

using namespace std;

int N;
int n1, n2, n3, n4;

int bf(int num) {
	int answer = 99;
	if (num < 100) {
		answer = num;
	}
	else if (num > 100) {
		if (num == 1000) num = 999;
		for (int i = 100; i <= num; i++) {
			n1 = i % 10;
			n2 = i / 10 % 10;
			n3 = i / 100;
			if (n1 - n2 == n2 - n3) answer++;
		}
	}
	return answer;
}

int main() {
	cin >> N;
	int result = bf(N);
	cout << result;
	return 0;
}