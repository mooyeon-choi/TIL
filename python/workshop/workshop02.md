
# Python 2. 데이터구조
## problem

* 두 개의 정수 n과 m이 주어질 때, 반복문을 사용하여 별(\*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 M인 사각형을 출력하시오


```python
n = 5
m = 9
for number in range(m):
    for num in range(n):
        print('*', end='')
    print('')
```

    *****
    *****
    *****
    *****
    *****
    *****
    *****
    *****
    *****
    

* 과목명과 점수가 담긴 딕셔너리가 있을 때, 평균 점수를 출력하시오.


```python
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
```


```python
total = 0
for value in student.values():
    total += value
print(total / len(student))
```

    87.75
    

* 다음은 여러 사람의 혈액형(A, B, AB, O)에 대한 데이터이다. 반복문을 사용하여 key는 혈액형의 종류, value는 인원 수인 딕셔너리를 만들고 출력하시오.


```python
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
```


```python
blood_dict = {}
for blood in blood_types:
    if blood not in blood_dict:
        blood_dict[blood] = 1
    else:
        blood_dict[blood] += 1
print(blood_dict)
```

    {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
    
