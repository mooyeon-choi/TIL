# ALGORITHM - DAY 3

## 2. 배열 2(Array 2)

* 배열 : 2차 배열
* 부분집합 생성 : 비트 연산자
* 바이너리 서치 (Binary Search)
* 셀렉션 알고리즘 (Selection Algorithm)
* 선택 정렬 (Selection Sort)
* 실습 1,2



### 2차원 배열

1. 2차원 배열의 선언

   * 1차원 List를 묶어놓은 List
   * 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
   * 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
   * Python 에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

   ```python
   arr = [[0,1,2,3],[4,5,6,7]]
   ```

2. 2차원 배열의 접근

   * 배열 순회

     * n X m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법

   * 행 우선 순회

     ```python
     # i 행의 좌표
     # j 열의 좌표
     for i in range(len(Array)):
         for j in range(len(Array[i])):
             Array[i][j] #필요한 연산 수행
     ```

   * 열 우선 순회

     ```python
     # i 행의 좌표
     # j 열의 좌표
     for j in range(len(Array[0])):
         for i in range(len(Array)):
             Array[i][j] #필요한 연산 수행
     ```

   * 지그재그 순회

     ```python
     # i 행의 좌표
     # j 열의 좌표=
     for i in range(len(Array)):
         for j in range(len(Array[0])):
             Array[i][j + (m-1-2*j) * (i%2)] 
             #필요한 연산 수행
     ```
     
   * 대각선 순회

     ```python
     N, M = len(arr), len(arr[0])
     for diag in range(0, N + M - 1):   # diag : 사선의 수 # x, y : 시작 좌표
         
         x = 0 if diag < M else (diag - M + 1)
         y = diag if diag < M else M - 1
         
         while x < N and y >= 0:
             print('%2d' % arr[x][y], end='')
             x += 1
             y -= 1
         print()
     ```

   * 델타를 이용한 2차 배열 탐색

     * 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

     ```python
     ary[0...n-1][0...n-1]
     dx[] <- [0, 0, -1, 1] # 상하좌우
     dy[] <- [-1, 1, 0, 0]
     
     for x in range(len(ary)):
         for y in range(len(ary[x])):
             for I in range(4):
                 testX <- x + dx[mode]
                 testY <- y + dy[mode]
                 test(ary[testX][testY])
     ```

   * 전치 행렬

     ```python
     # i : 행의 좌표, len(arr)
     # j : 열의 좌표, len(arr[0])
     arr = [[1,2,3],[4,5,6],[7,8,9]] # 3*3 행렬
     
     for i in range(3):
         for j in range(3):
             if i < j :
                 arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
     ```
   
3. 부분집합

   * 부분집합 생성하기

     * 완전검색 기법으로 부분집합 합 문제를 풀기 위해서는, 우선 집합의 모든 부분집합을 생성한 후에 각 부분집합의 합을 계산해야 한다.

     * 주어진 집합의 부분집합을 생성하는 방법에 대해서 생각해보자.

     * 부분집합의 수

       * 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2<sup>n</sup>개 이다.
       * 이는 각 원소를 부분집합에 포함시키거나 포함시키지 않는 2가지 경우를 모든 원소에 적용한 경우의 수와 같다.

     * 각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 부분집합을 생성하는 방법

       ```python
       arr 'ABC'
       bits = [0] * 3
       
       for i in range(2):
           bits[0] = i
           for j in range(2):
               bits[1] = j
               for k in range(2):
                   bits[2] = k
                   print(bits, end='> ')
                   for x in range(len(bits)):
                       if bits[x]: print(arr[x], end=' ')
                   print()
       ```

       ```python
       # 재귀호출
       arr 'ABC'
       bits = [0] * 3
       
       def subset(k, n):
           if k == n:
               print(bits, end='> ')
               for i in range(len(bits)):
                   if bits[i]: print(arr[i],end=' ')
               print()
               return
           
           for i in range(2):
               subset(k + 1, n)
       ```

4. 비트 연산자

   * 비트 연산자

     ```python
     0b(2진수) # 2진수 비트단위 표기법
     & # 비트 단위로 and 연산을 한다.
     | # 비트 단위로 or 연산을 한다.
     << # 피연산자의 비트 열을 왼쪽으로 이동시킨다.
     >> # 피연산자의 비트 열을 오른쪽으로 이동시킨다.
     ```

5. 검색(Search)

   * 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
   * 목적하는 탐색 키를 가진 항목을 찾는 것
     * 탐색 키(search key) : 자료를 구별하여 인식할 수 있는 키
   * 검색의 종류
     * 순차 검색(sequential search)
     * 이진 검색(binary search)
     * 해쉬(hash)
   * 일렬로 되어 있는 자료를 순서대로 검색하는 방법
     * 가장 간단하고 직관적인 검색 방법
     * 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
     * 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임
   * 2가지 경우
     * 정렬되어 있지 않은 경우
     * 정렬되어 있는 경우
   * 정렬되어 있지 않은 경우

       * 검색 과정
         * 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.
         * 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
         * 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패
       * 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
         * 첫 번째 원소를 찾을 때는 1번 비교, 두 번째 원소를 찾을 때는 2번 비교..
         * 정렬되지 않은 자료에서의 순차 검색의 평균 비교 회수
         * 시간 복잡도 : O(n)
   * 정렬되어 있는 경우
     * 검색 과정
       * 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정하자.
       * 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료한다.
