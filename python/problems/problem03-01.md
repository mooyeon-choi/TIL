
# 버거지수
> 한 도시의 발전 수준은 `(버거킹의 개수 + 맥도날드의 개수 + KFC의 개수) / 롯데리아의 개수` 로 나타낼 수 있다고 한다.
>
> locationA 에 있는 딕셔너리를 인자로 받아 버거지수를 계산하는 함수를 만들고 호출하시오.


```python
locationA = {
    'king': 2,
    'mc': 4,
    'kfc': 1,
    'ria': 3
}

# 아래에 코드를 작성하세요.
def fastfood(king, mc, kfc, ria):
    return (king + mc + kfc) / ria
```


```python
print(fastfood(**locationA))
```

    2.3333333333333335
    

# 종합소득세 계산하기
> A라는 나라에서 종합소득세는 과세표준 금액 구간에 따라 다른 세율이 적용됩니다.

|과세표준액|세율|
|-------|---|
|1,200이하|6%|
|1,200 ~ 4,600|15%|
|4,600 ~ |35%|

```
즉, 1,300원을 벌었을 경우 1,200\*0.06 + 100\*0.15를 계산한 결과가 납부해야 하는 세액입니다.

함수 tax를 만들고 납부해야하는 세금의 결과를 반환하는 함수를 만들어보세요.
```


```python
# 아래에 코드를 작성하세요
def tax(money):
    tax_money = 0
    if money > 4600:
        tax_money += (money - 4600) * 0.35 + 3400 * 0.15 + 1200 * 0.06
    elif money > 1200:
        tax_money += (money - 1200) * 0.15 + 1200 * 0.06
    else:
        tax_money += money * 0.06
    return tax_money
```


```python
def tax(money):
    tax_money = 0
    for count in range(1, money + 1):
        if count > 4600:
            tax_money += 0.35
        elif count > 1200:
            tax_money += 0.15
        else:
            tax_money += 0.06
    return round(tax_money)
```


```python
tax(5000)
```




    722



# 텔레그램 챗봇

> 텔레그램 메신져를 이용하여 챗봇을 개발하려고한다.
>
> api를 사용하기 위해 공식문서를 찾아보니 `https://api.telegram.org/bot<token>/METHOD_NAME`와 같은 경로로 
>
> token과 사용할 method의 이름을 넣어서 요청으로 보내라고 한다.
>
> 사용자에게 토큰과 사용할 메소드 이름을 받아 url을 만들어주는 함수를 만들어보시오.
>
> 개발자가 발급받은 토큰은 길이가 41자 라는 규칙을 따른다. 사용자가 잘못된 토큰을 넣었다면 '403'을 반환하시오

```
예시)
https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
```


```python
# 아래에 코드를 작성하세요
def tele(token, method):
    if len(token) < 41:
        return 403
    else:
        base_url = 'https://api.telegram.org/bot<token>/METHOD_NAME'
        base_url = base_url.replace('<token>', token)
        base_url = base_url.replace('METHOD_NAME', method)
        return base_url

tele('123123:afjio;wef', 'getMe')
tele('123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11', 'getMe')
```




    'https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe'



# 솔로 천국
> 리스트가 주어집니다. 리스트의 각 요소는 숫자 0부터 9까지로 이루어져 있습니다.
> 
> 이때, 리스트에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
> 
> 리스트에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 반환하는 lonely 함수를 작성해 주세요.
> 
> 단, 제거된 후 남은 수들을 반환할 때는 리스트의 요소들의 순서를 유지해야 합니다.

```
예시)

lonely([1, 1, 3, 3, 0, 1, 1]) #=> [1, 3, 0, 1]
lonely([4,4,4,3,3]) #=> [4,3]
```


```python
# 여기에 코드를 작성하세요
def lonely(list_in):
    # result 빈통
    result = []
    result.append(list_in[0])
    # 하나씩 비교하면서
    for number in list_in:
        # result의 마지막 값과 지금 숫자가 다르다면
        if number != result[-1]:
            result.append(number)
    return result
```


```python
lonely([4,4,4,3,3])
```




    [4, 3]


