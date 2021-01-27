# 브루트 포스

> 가능한 경우의 수를 모두 탐색하며 정답을 찾아보자

## 목차

* [블랙잭](#블랙잭)
* [분해합](#분해합)
* [덩치](#덩치)
* [체스판 다시 칠하기](#체스판-다시-칠하기)
* [영화감독 숌](#영화감독-숌)

## 블랙잭

> 난이도 : Bronze II

* 문제

  카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.

  한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.

  김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.

  이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

  N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

* 입력

  첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는다.

  합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

* 풀이

  ```python
  N, M = map(int, input().split())
  nums = list(map(int, input().split()))
  answer = 0
  for i in range(N):
    for j in range(i + 1, N):
      for k in range(j + 1, N):
        if nums[i] + nums[j] + nums[k] <= M:
          if M - answer > M - (nums[i] + nums[j] + nums[k]):
            answer = nums[i] + nums[j] + nums[k]
  print(answer)
  ```

  * 3중 for문을 통해 모든 경우의 수를 찾아주었다.
  * 이때 두번째, 세번째 숫자의 범위를 주의하며 풀자

## 분해합

> 난이도 : Bronze II

* 문제

  어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

  자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

* 입력

  첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

* 풀이

  ```python
  def find(N):
    for i in range(N):
      num = i
      for j in str(i):
        num += int(j)
      if num == N:
        return i
    return 0
  
  print(find(int(input())))
  ```

  * `1`부터 `N - 1` 까지의 모든 숫자를 확인하며 생성자를 찾아주었다.

    처음 찾은 생성자가 가장 작으므로 바로 리턴해주어 반복문을 종료해준다.

## 덩치

> Silver V

* [문제 링크](https://www.acmicpc.net/problem/7568)

* 입력

  첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다. 단, 2 ≤ N ≤ 50, 10 ≤ x,y ≤ 200 이다.

* 풀이

  ```python
  N = int(input())
  people = []
  tier = [1] * N
  for _ in range(N):
    people.append(tuple(map(int, input().split())))
  for i in range(N):
    for j in range(N):
      if i != j:
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
          tier[i] += 1
  
  print(' '.join(map(lambda x: str(x), tier)))
  ```

## 체스판 다시 칠하기

> 난이도 : Silver V

* 문제

  지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.

  체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

  보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

* 풀이

  ```python
  N, M = map(int, input().split())
  board = [input() for _ in range(N)]
  answer = N * M
  for x in range(N - 7):
    for y in range(M - 7):
      for white_start in range(2):
        cnt = 0
        for i in range(8):
          for j in range(8):
            if white_start:
              if (i + j) % 2:
                if board[x + i][y + j] != 'B':
                  cnt += 1
              else:
                if board[x + i][y + j] != 'W':
                  cnt += 1
            else:
              if (i + j) % 2:
                if board[x + i][y + j] != 'W':
                  cnt += 1
              else:
                if board[x + i][y + j] != 'B':
                  cnt += 1
        if cnt < answer:
          answer = cnt
  print(answer)
  ```

  * `8 * 8` 체스판에서 `i + j` 의 값이 홀수일 때와 짝수일 때 색이 다르게 칠해주면 된다.
  * `1 = True` , `0 = False` 를 이용하여 흰색으로 시작할 때와 검정색으로 시작할 때를 for문으로 나눠주었다.
  * 완전탐색으로 모든 경우에 대해 체크해주었다.

## 영화감독 숌

> 난이도 : Silver V

* [문제 링크](https://www.acmicpc.net/problem/1436)

* 입력

  첫째 줄에 숫자 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.

* 풀이

  ```python
  N = int(input())
  num = 665
  cnt = 0
  while True:
    num += 1
    if str(num).count('666'):
      cnt += 1
    if cnt == N:
      print(num)
      break
  ```

  * 숫자를 1씩 증가시키며 `666`이 포함되는 경우에만 `cnt`를 증가시켜주고 `cnt` 가 `N`이 되었을 때 출력해주었다.

