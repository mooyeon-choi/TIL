# Python을 통한 컴퓨터 조작

## 1. OS

`os(operation system)` 운영체제의 약자로, 파이썬에서는 `os` 모듈을 통해 컴퓨터를 조작할 수 있도록 도와준다.

* `getcwd()` : 현재 working directory의 절대위치를 나타낸다.

  ```python
  os.getcwd()
  #=> 'C:\\Users\\student\\Desktop\\startcamp'
  ```

* `chdir(경로)` : 해당하는 `경로`로 이동한다.

  ```python
  import os
  # 절대경로
  os.chdir(r'C:\Users\student\Desktop\startcamp\day2\dummy')
  # 상대경로
  os.chdir(r'./dummy/')
  print(os.getcwd())
  #=> 변경된 경로가 출력됨
  ```

* `listdir(경로)` : 해당하는 `경로` 에 있는 파일 및 폴더 이름들을 리스트로 반환한다.

  ```python
  import os
  print(os.listdir('.'))
  #=> ['a.py', 'b.py', 'day2']
  ```

* `rename(기존 파일명, 변경할 파일명)` : `기존 파일명`을 `변경할 파일명`으로 변경한다.

  ```python
  import os
  for filename in os.listdir('.'):
      os.rename(filename, 'hi_'+filename)
  ```

  

## 2. 파일 읽고 쓰기

### 1. 파일 쓰기

1. 기본 활용법

   ```python
   f = open('a.txt', 'w')
   f.write('안녕하세요')
   f.close()
   ```

   * `open(파일명, 옵션, 인코딩)`
     * 옵션 :
       * `w` : write (덮어쓰기)
       * `a` : append (이어쓰기)
       * `r` : read (읽기)
     * 인코딩 : 기본적으로 윈도우에서 한글은 `cp949` 이고, 일반적으로 많이 쓰는 인코딩은 `utf-8`이다.

2.  컨택스트 매니저 `with` 구문 활용

   ```python
   with open('a.txt', 'w', encoding='utf-8') as f(파일명):
       f(파일명).write('hi')
   ```



### 2. 파일 읽기

* `read()` : 전체 내용을 하나의 문자열(`string`)을 반환한다.

  ```python
  with open('a.txt', 'r', encoding='utf-8') as f:
      txt = f.read()
  print(txt)
  ```

* `readlines()` : 각 라인의 내용을 원소로 가지는 리스트를 반환한다.

  ```python
  with open('a.txt', 'r', encoding='utf-8') as f:
      lines = f.readlines()
      
  for line in lines:
      print(line)
  ```



