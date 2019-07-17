
# Python 2. 데이터 구조
* 학습해야 할 내용
    * 시퀀스 자료형
    * set, dictionary
    * 제어문

1. 아래 보기 중, 변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을 분류 하시오.

**String List Tuple Range Set Dictionary**

1. mutable : List, Set, Dictionary
2. immutable : String, Tuple, Range

2. range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.


```python
number = range(51)
print(list(number[1::2]))
```

    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
    

3. 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 딕셔너리를 만드시오.


```python
student = {'서현택' : 27, '조선행' : 27}
```
