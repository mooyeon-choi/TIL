#include <stdio.h>
int N, M, T;
int circles[51][51] = { 0, };

int back() {
	
	return 0;
}
int main() {
	scanf("%d %d %d", &N, &M, &T);
	int i, j, num;
	for (i = 1; i <= N; i++) {
		for (j = 1; j <= M; j++) {
			scanf("%d", &num);
			circles[i][j] = num;
		}
	}
	/*
	for (i = 1; i <= N; i++) {
		for (j = 1; j <= M; j++) {
			printf("%d", circles[i][j]);
		}
		printf("\n");
	}
	*/
}