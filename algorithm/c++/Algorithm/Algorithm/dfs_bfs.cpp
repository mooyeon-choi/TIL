#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

int N, M, V;
bool visited[1001] = { false, };

vector < vector <int> > vec;

int dfs(int now_num) {
	visited[now_num] = true;
	cout << now_num << " ";
	for (int i = 0; i < vec[now_num].size(); i++) {
		if (!visited[vec[now_num][i]]) {
			dfs(vec[now_num][i]);
		}
	}
	return 0;
}

int main(void) {
	cin >> N >> M >> V;
	vec.resize(N + 1);

	int temp_a, temp_b;
	while (M--) {
		cin >> temp_a >> temp_b;
		vec[temp_a].push_back(temp_b);
		vec[temp_b].push_back(temp_a);
	}
	for (int i = 1; i < vec.size(); i++) {
		sort(vec[i].begin(), vec[i].end());
	}
	dfs(V);
	return 0;
}