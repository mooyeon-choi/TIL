# 단계별로 풀어보기

> https://www.acmicpc.net/step

## 목록

* [입출력과 사칙연산](#입출력과-사칙연산)
* [if문](#if문)
* [for문](#for문)
* [while문](#while문)
* [일차원 배열](#일차원-배열)
* [함수](#함수)
* [문자열](#문자열)
* [수학 1](#수학-1)
* [수학 2](#수학-2)
* [재귀](#재귀)
* [브루트 포스](#브루트-포스)



## 입출력과 사칙연산

> 입력, 출력과 사칙연산을 연습해 봅시다. Hello World!!

* [Python 바로가기](./inputOutput_python)
* [Cpp 바로가기](./inputOutput_cpp)

| 순번 |                       문제 링크                        | 분류 |                            난이도                            |                             풀이                             |
| :--: | :----------------------------------------------------: | :--: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  1   |  [Hello World](https://www.acmicpc.net/problem/2557)   | 구현 | <img src="https://static.solved.ac/tier_small/1.svg" width="26px"> | [<img src="https://icongr.am/devicon/python-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_python#hello-world)  [<img src="https://icongr.am/devicon/cplusplus-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_cpp#hello-world) |
|  2   | [We love kriii](https://www.acmicpc.net/problem/10718) | 구현 | <img src="https://static.solved.ac/tier_small/1.svg" width="26px"> | [<img src="https://icongr.am/devicon/python-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_python#we-love-kriii)  [<img src="https://icongr.am/devicon/cplusplus-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_cpp#we-love-kriii) |
|  3   |    [고양이](https://www.acmicpc.net/problem/10171)     | 구현 | <img src="https://static.solved.ac/tier_small/1.svg" width="26px"> | [<img src="https://icongr.am/devicon/python-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_python#%EA%B3%A0%EC%96%91%EC%9D%B4)  [<img src="https://icongr.am/devicon/cplusplus-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_cpp#%EA%B3%A0%EC%96%91%EC%9D%B4) |
|  4   |      [개](https://www.acmicpc.net/problem/10172)       | 구현 | <img src="https://static.solved.ac/tier_small/1.svg" width="26px"> | [<img src="https://icongr.am/devicon/python-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_python#%EA%B0%9C)  [<img src="https://icongr.am/devicon/cplusplus-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_cpp#%EA%B0%9C) |
|  5   |      [A+B](https://www.acmicpc.net/problem/1000)       | 구현 | <img src="https://static.solved.ac/tier_small/1.svg" width="26px"> | [<img src="https://icongr.am/devicon/python-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_python#a+b)  [<img src="https://icongr.am/devicon/cplusplus-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_cpp#a+b) |
|  6   |      [A-B](https://www.acmicpc.net/problem/1001)       | 구현 | <img src="https://static.solved.ac/tier_small/1.svg" width="26px"> | [<img src="https://icongr.am/devicon/python-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_python#a-b)  [<img src="https://icongr.am/devicon/cplusplus-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_cpp#a-b) |
|  7   |      [A×B](https://www.acmicpc.net/problem/10998)      | 구현 | <img src="https://static.solved.ac/tier_small/1.svg" width="26px"> | [<img src="https://icongr.am/devicon/python-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_python#a*b)  [<img src="https://icongr.am/devicon/cplusplus-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_cpp#a*b) |
|  8   |      [A/B](https://www.acmicpc.net/problem/1008)       | 구현 | <img src="https://static.solved.ac/tier_small/2.svg" width="26px"> | [<img src="https://icongr.am/devicon/python-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_python#a/b)  [<img src="https://icongr.am/devicon/cplusplus-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_cpp#a/b) |
|  9   |   [사칙연산](https://www.acmicpc.net/problem/10869)    | 구현 | <img src="https://static.solved.ac/tier_small/1.svg" width="26px"> | [<img src="https://icongr.am/devicon/python-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_python#%EC%82%AC%EC%B9%99%EC%97%B0%EC%82%B0)  [<img src="https://icongr.am/devicon/cplusplus-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_cpp#%EC%82%AC%EC%B9%99%EC%97%B0%EC%82%B0) |
|  10  |    [나머지](https://www.acmicpc.net/problem/10430)     | 구현 | <img src="https://static.solved.ac/tier_small/1.svg" width="26px"> | [<img src="https://icongr.am/devicon/python-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_python#%EB%82%98%EB%A8%B8%EC%A7%80)  [<img src="https://icongr.am/devicon/cplusplus-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_cpp#%EB%82%98%EB%A8%B8%EC%A7%80) |
|  11  |      [곱셈](https://www.acmicpc.net/problem/2588)      | 구현 | <img src="https://static.solved.ac/tier_small/2.svg" width="26px"> | [<img src="https://icongr.am/devicon/python-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_python#%EA%B3%B1%EC%85%88)  [<img src="https://icongr.am/devicon/cplusplus-original.svg?size=128&color=currentColor" width="30px">](https://github.com/mooyeon-choi/TIL/tree/master/problemSolving/baekjoon/step/inputOutput_cpp#%EA%B3%B1%EC%85%88) |

## if문

> python if문 사용법

* [Python 바로가기](./if_python)

## for문

> python for문 사용법

* [Python 바로가기](./for_python)

## while문

> python while문 사용법

* [Python 바로가기](./while_python)

## 일차원 배열

> Python List 활용법

* [Python 바로가기](./1DArray_python)

## 함수

> Python Function 활용법

* [Python 바로가기](./function_python)

## 문자열

> Python 문자열 처리

* [Python 바로가기](./string_python)

## 수학 1

> 수식을 사용해서 풀수있는 문제들을 풀어보자

* [Python 바로가기](./math_1_python)

## 수학 2

> 수식을 찾아서 문제를 풀어보자

* [Python 바로가기](./math_2_python)

## 재귀

* [Python 바로가기](./recursion_python)

## 브루트 포스

> 가능한 경우의 수를 모두 탐색하며 찾는 방법이다.

* [Python 바로가기](./bruteforce_python)