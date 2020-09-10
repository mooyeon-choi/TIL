#include <iostream>

using namespace std;

int N, M;
bool visit[9] = { false, };
int result[8] = { 0, };

void back(int count) {
	if (count == M) {
		for (int i = 0; i < count; i++) cout << result[i] << ' ';
		cout << '\n';
		return;
	}
	else {
		for (int i = 1; i <= N; i++) {
			if (!visit[i]) {
				visit[i] = true;
				result[count] = i;
				back(count + 1);
				visit[i] = false;
			}
		}
	}
}

int main() {
	cin >> N >> M;
	int count = 0;
	back(count);
	return 0;
}