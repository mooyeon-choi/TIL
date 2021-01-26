# 02. CSS(Cascading Style Sheets)

* Style sheet language

> HTML이 기본적인 구조를 만든다면 CSS는 꾸며주기 위한 language

## 목차

* [CSS 활용하기](#css-활용하기)
* [Selector](#selector)
* [Unit](#unit)

## CSS 활용하기

### CSS 사용법

#### Inline(인라인)

>  인라인으로 작성이 가능하지만 그 한줄에만 적용 가능하고 나중에 찾기 힘드므로 권장하지 않음

```html
<p id="green" style="color: purple;">인라인 CSS 활용</p> 
```

* HTML 요소의 style에 CSS를 넣기



#### embed(내부참조)

> head 태그 내에 style 태그

```html
<head>
  <style>
   내용
  </style>
</head>
```

* HTML 내부에 CSS를 포함시키기



#### link file(외부참조)

> 재사용이 가능하므로 일반적으로 사용한다.

```html
<link rel="stylesheet" href="01_style.css">
```

* 외부에 있는 CSS 파일을 로드하기



#### CSS 단위

[자주 사용하는 CSS 속성값들](https://developer.microsoft.com/en-us/microsoft-edge/platform/usage/)

프로퍼티 값의 단위

```css
h1 {color:blue;font-size:15px;}
```

* `blue`, `15px` : 값(Value)

* `color`, `font-size` : 키워드(크기단위, 색깔 등)

  > 크롬 우클릭 > 검사 > styles에서 개발자 도구로 확인 가능



1. 크기 단위

   1. px : 화면을 구성하는 단위 (디바이스 별로 픽셀의 크기가 다르다.)

   2. % : 백분율 단위의 상대 단위

      요소에 지정된 사이즈(상속된 사이즈나 디폴트 사이즈)에 상대적인 사이즈를 설정한다.

      ![01_css](./image/01_css.jpg)

   3. **em과 rem** :

      * em: 배수 단위로 상대 단위이다





### 선택자 우선순위

```html
<body>
  <!-- 선택자는 우선순위가 있다.
        id > class > tag
        id는 문서에서 반드시 한번만 등장!
        class는 문서에서 여러번 등장!
        따라서 중복으로 사용할 때에는 class를 사용한다.
  -->
  <h1>Hello, CSS!</h1>
  <h2 class="blue">선택자</h2>
  <h3 class="blue">태그 선택자</h3> <!-- 우선순위: 클래스 선택자 > 태그 선택자 -->
  <h3 id="green">클래스 선택자</h3> <!-- id 선택자 > 태그 선택자 -->
  <h3 id="green" class="blue">아이디 선택자</h3> <!-- 아이디 선택자 > 클래스 선택자 -->
  <!-- style에서 선언하지 않고 < >내에서 정해준게 우선 -->
  <p id="green" style="color: purple;">인라인 CSS 활용</p> 
  <!-- !important가 CSS 적용이 가장 우선된다.
      하지만, 사용에 주의하자. 남발하지 말자.
  -->
  <p id="green" class="blue brown" style="color: purple">무슨 색일까요?</p>
</body>
```

* `!important` : 우선 순위를 가장 높게 바꿔준다. 사용할 경우 코드가 꼬일 수 있어 거의 사용하지 않는다. (같은 선택자라면 가장 아래에 있는 것이 우선, 다른 선택자라면 선택자들 간의 우선순위에 따라 결정)
* 기본적으로 id > class > tag 순이다.
* id 선택자의 경우 한번만 사용하야하므로 우선순위가 가장 높다.
* inline(인라인)으로 사용해 준 경우 우선순위가 가장 높다.

## Selector

### 선택자 적용법

#### 그룹 선택자

```css
h1, h2, h3, h4, h5, h6, .silver {
  color: silver;
}
```

* 요소들을 묶어서 한번에 처리해줄 수 있다.

#### 인접 선택자

```css
.blue + .red + div {
  background-color: purple;
}
```

```html
  <div class="blue"></div>
  <div class="red"></div>
  <div>CSS is awesome!</div>
```

* `.blue` -> `.red` -> `div` 순으로 코드가 실행될 경우 지정해준 style로 나타나도록 정해줄 수 있다.

#### 자식 선택자 vs 후손 선택자

> 자식 선택자의 경우 지정해준 순서로 포함된 경우에만 실행이 되도록 하고,
>
> 후손 선택자의 경우 지정해준 클래스 아래에 속해있다면 모두 실행된다.

```css
/* 자식 선택자 (바로 밑에 있을 경우) */
.parent > li {
  color: red;
}

/* 후손 선택자 (속해있다면 모두) */
.ancestor li {
  color: blue
}
```

```html
  <ol class="parent">
    <ul>
      <li>ol>ul>li</li>
    </ul>
  </ol>
  <ol class="parent">
    <li>ol>li</li>
  </ol>
  <ol class="ancestor">
    <ul>
      <li>ol>ul>li</li>
    </ul>
  </ol>
  <ol class="ancestor">
    <li>ol>li</li>
  </ol>
```

* 실행 결과

![01](./image/01.png)

> 자식 선택자를 사용하였을 경우 `ol`바로 아래에 `li`가 있는 경우만 실행 되는 것을 확인 할 수 있고,
>
> 후손 선택자를 사용하였을 경우 `ol` 안에 `li` 가 속한경우 모두 실행되는 것을 알 수 있다.

## Unit

### rem과 em

```css
ol, ol li {
  font-size: 2rem;
}

ul, ul li {
  font-size: 2em;
}
```

```html
<!-- rem -->
<ol>
    <li>2rem</li>
</ol>
<!-- em -->
<ul>
    <li>2em</li>
</ul>
```

1. rem

   * root 요소의 배수
   * html : 16px (브라우저 기본)
   * ol : 2rem -> 32px (16px * 2)
   * li : 2rem -> 32px (16px * 2)

2. em

   * 상위 요소의 배수

   * html : 16px

   * ul : 2em -> 32px

   * li : 원래 ul 밑에 있어서 32px

     ​	2em -> 32px * 2 -> 64px

## 4. Box_model





## 5. Display

