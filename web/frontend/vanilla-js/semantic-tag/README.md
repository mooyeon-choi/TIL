# Semantic Tag

> `<div>`로만 요소들을 나눠주면 어떠한 내용이 들어있는지 알 수 없다. 따라서 HTML5에서는 웹 사이트의 내용을 구분해주기 위해 여러 Semantic tag들이 추가되었다.
>
> 이러한 Semantic tag 들의 의미와 어떤 때에 MDN Guide를 보며 이해하자.
>
> [MDN Using HTML sections and outlines](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Using_HTML_sections_and_outlines)

## 목차

* [HTML5에 추가된 Section Elements](#html5에-추가된-section-elements)
* [그 밖의 Semantic HTML element](#그-밖의-Semantic-html-element)
* [Sectional Elements의 사용법](#sectional-elements의-사용법)

## HTML5에 추가된 Section Elements

* **HTML Navigational Element** (`<nav>`)

  네비게이션 링크를 포함하고 있는 Section을 나타낸다. `<nav>`안에 다른 menu를 추가해주어도 되지만, 또 다른 `<nav>`를 추가해 주어선 안된다.

* **HTML Article Element** (`<article>`)

  그 하나로 자체적인 완전한 개별 컨텐츠가 될 때 사용된다. 신문으로 생각하면 하나의 신문 기사는 다른 내용들과 전혀 연관되어 있지 않고 그 하나만으로 완전한 글이 되고 그 하나의 기사를 article이라 한다.

  하지만, main content 하나로만 이루어져있을 때는 사용되지 않는다.

* **HTML Section Element**(`<section>`)

  서로 연관되어 있는 컨텐츠를 구분할 때 사용된다. 하나의 상위 요소에서 추가 context를 제공할 때 주로 사용된다.

* **HTML Aside Element**(`<aside>`)

  Explanation box나 광고와 같이 Main 요소에 포함되지만 Main 요소의 흐름에는 관련되어 있지 않은 컨텐츠를 구분할 때 사용된다. `<aside>`에는 Outline이 있지만 Main 요소에 속하지는 않는다.

## 그 밖의 Semantic HTML element

* **HTML Body Element**(`<body>`)

  문서의 모든 컨텐츠 내용을 정의한다. 모든 컨텐츠들과 HTML tag들이 들어있다.

* **HTML Header Element**(`<header>`)

  보통 로고, 제목, Navigation을 포함하는 영역을 구분할 때 사용된다. `<header>`는 다른 요소 안에도 사용될 수 있어 `<article>`, `<section>`의 제목을 넣어줄 때도 사용할 수 있다.

  이러한 역할 때문에 `<header>`를 꼭 넣어줘야 한다고 생각할 수 있다. 하지만 `<header>`가 반드시 필요한 요소는 아니다.

* **HTML Footer Element**(`<footer>`)

  보통 페이지 가장 아래 저작권이나 특정 링크를 표시할 때 사용한다. 위와 마찬가지로 다른 요소 안에도 사용될 수 있다.

## Sectional Elements의 사용법

```html
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">link</a></li>
                <li><a href="#">link</a></li>
                <li><a href="#">link</a></li>
            </ul>
        </nav>
        <h1>
            Page Title
        </h1>
    </header>

    <section>
        <h2>
            My Blog Posts
        </h2>
        <article>
            <header>
                <p>
                    Article Title
                </p>
            </header>
            <p>
                content
            </p>
        </article>
        <article>
            <header>
                <p>
                    Article Title
                </p>
            </header>
            <p>
                content
            </p>
        </article>
        <aside>
            <p>
                Author info
            </p>
        </aside>
    </section>

    <footer>
        Copyright Info
    </footer>
</body>
```

### Nav Element

> `<nav>` element 은 navigation block나 navigational menus를 표시하기 위해 사용된다.

```html
<nav>
  <ul>
    <li><a href="#">link</a></li>
    <li><a href="#">link</a></li>
  </ul>
</nav>
```

