
# Python 3. 함수
1. Python에서 기본으로 사용할 수 있는 Built in function 5개를 찾아서 작성하세요.

print(), input(), set(), dict(), abs()

2. 다음과 같이 함수가 정의되어 있다. 보기 중, 오류가 발생하는 코드를 고르시오.


```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')
```


```python
ssafy(location='대전', name='철수')
```

    철수의 지역은 대전입니다.
    


```python
ssafy('길동', location='광주')
```

    길동의 지역은 광주입니다.
    


```python
ssafy(name='허준', '구미')
```


      File "<ipython-input-4-c613e123d6bf>", line 1
        ssafy(name='허준', '구미')
                            ^
    SyntaxError: positional argument follows keyword argument
    


3. 다음과 같이 코드가 작성되어 있을 때, 변수 result에 저장된 값을 작성하시오.


```python
def my_func(a,b):
    c = a + b
    print( c )
result = my_func(4,7)
```

    11
    
