
# Python 3. 함수
* Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, 'a' 'nan' '토마토' 모두 palindrome에 해당합니다.
* 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요


```python
def palindrome(word):
    for number in range(len(word) // 2):
        if word[number] != word[-number - 1]:
            return False
    return True            
```


```python
palindrome('토마토')
```




    True



[::-1] 뒤에서부터 읽어옴


```python
def palindrome(word):
    return word == word[::-1]
```
