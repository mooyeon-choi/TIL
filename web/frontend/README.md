# Front End

## 목차

* [같이 보면 좋은 자료들](#같이-보면-좋은-자료들)
* [Interactive Development](#interactive-development)
* [React](#react)
* [Angular vs React vs Vue](#angular-vs-react-vs-vue)

## 같이 보면 좋은 자료들

:loudspeaker: ​공부하면서 많은 도움이 되었던 유익한 자료들!

### Youtube 채널 드림코딩 by 엘리

* [채널 바로가기](https://www.youtube.com/channel/UC_4u-bXaba7yrRz_6x6kb_w)

```
호주에서 프론트앤드 개발자💼로 근무하고 계시는 엘리님의 유튜브 채널📺
프론트앤드 개발에 필요한 전반적인 지식🎓을 이해하기 쉽게 잘설명해준다.
드림코딩 아카데미 유료강의💰도 모두 듣는 것을 추천
```

### Youtube 채널 Interactive Developer

* [채널 바로가기](https://www.youtube.com/channel/UCdeWxKJuvtUG2xyN6pOJEvA)

```
구글에서 Interactive Developer💼로 근무하고 계시는 김종민님의 유튜브 채널📺
canvas🎨를 활용해 만든 재미있는 디자인의 Interactive 화면을 보고 따라할 수 있다.
JS class 활용법을 공부하고 이해하는데 많은 도움이 되었고 재미있게😂 따라할 수 있어 심심할때 보기 좋다.
```

## Interactive Development

* [바로가기](./Interactive)

```
canvas🎨에 JS event loop와 수학 공식을 더해주면 Interactive한 화면이?!
3D Cube부터 통통 튀어다니는 공까지 재미있는 실습을 통해 완성도 높은 페이지를 만들어보자!
```

![Canvas Example](./images/interactive_example.gif)

## React

* [바로가기](./react)

```
페이스북에서 만든 현재 가장 많은 사람들👪이 이용하는 Front-end Library
현업👔에서 많이 쓰이는 기술 스택을 익혀보자
```

![Example](./images/react_example.gif)

## Vue

* [바로가기](./vue)

```
최근 뜨고있는 Frontend Framework
공식문서📚가 잘 작성되어있어 처음 배울경우 공식문서만 보고도 어느정도 웹 페이지를 제작할 수 있어 진입장벽이 낮다
React 다음으로 현업👔에서 많이 쓰고있는 Vue에 대해 알아보자
```

## Angular vs. React vs. Vue

> **배경**
>
> 모바일의 시대가 도래하면서, 모바일 환경에 맞춰진 웹 페이지 즉 모바일 웹에 대한 니즈가 폭발적으로 증가하였고 그에 따른 성능 이슈도 함께 거론되었다. 데스크탑에 비해 성능이 낮은 모바일, 스마트폰을 통해 웹 페이지를 출력하기 위해서는 기존에 있었던 방식과는 다른 접근이 필요했고 그에 따라서 Single Page Web Application 기법(SPA)이 등장하게 되었다.
>
> SPA는 브라우저에 로드되고 난 뒤에 페이지 전체를 서버에 요청하는 것이 아니라 최초 한번 페이지 전체를 로딩한 이후 부터는 데이터만 변경하여 사용할 수 있는 웹 애플리케이션을 의미한다. 전통적인 웹 방식(서버 사이드 렌더링)은 이 SPA 방식에 비해 성능 문제를 보였다. 요청 시 마다 새로고침이 일어나며 페이지를 로딩할 때 마다 서버로부터 리소스를 전달받아 해석하고 화면에 렌더링 하는 방식이었기 때문이다.
>
> SPA는 트래픽을 감소시키고 사용자에게 더 나은 경험을 제공했다. 서버는 단지  JSON 파일만 보내주는 역할을 했고, HTML을 그리는 역할은 클라이언트 측에서 자바스크립트가 수행하게 된 것이다. 바로 이것이 클라이언트 사이드 렌더링(Client-side rendering)이다.

### Angular

MVC 구조 덕분에 Angular는 작업을 논리적 청크로 분할하여 웹 페이지의 초기 로드 시간을 줄일 수 있다. 클라이언트 측에서 View 부분이 표시되어 백그라운드에서 쿼리를 크게 줄이고 이는 비동기 모드에서 작동하므로 서버에 대한 호출이 더 적게 수행된다.

#### 특징

* **양방향 데이터 바인딩(Two-way data binding)** : Angular는 쉽고 효율적이며 직관적인 방식으로 모델에 대한 변경 사항을 즉식 뷰에 복제한다.

#### 단점

* **Heavier applications** : React 와 Vue에 비해 무겁고 초기 구동 속도가 느리다.
* **지속적인 업데이트Constantly updating**
* **어렵다(Steep learning curve)** : React 와 Vue에 비해 학습하기가 어렵다.



### React

 React 는 상태 저장 및 재사용 가능한 UI 구성 요소를 만드는 데 사용되는 Front-end Library이다. 이를 통해 개발자는 페이지를 다시 로드 하지 않고도 데이터를 변경할 수 있는 대규모 웹 응용 프로그램을 만들 수 있다.

 MVC templete을 모두 구현하지 않고, View 부분만을 다룬다. 간단하고 확장 가능하며 빠르다는 특성이 있다.

#### 특징

* **성능(performance)** : gzip 파일로 43KB 밖에 되지 않는 크기와 빠른 속도, 많은 기능
* **가상 DOM 사용(Using a virtual DOM)** : 필요한 node만을 re-rendering 한다.
* **번들링, 트리 쉐이킹 지원(Support for bundling and tree-shaking)** : User resource load 를 최소화
* **서버 사이드 렌더링(Server-side rendering)**
* **단방향 데이터 바인딩(One-way data binding)**
* **쉽게 테스트 가능(Easily testable)** : 작업의 출력을 모니터링하고 전체 개발 프로세스를 개선하는 것이 쉬워진다.

#### 단점

* **MVC를 모두 구현하지 않음(Doesn’t implement MVC)** : 상태(state) 및 모델(model)을 구현하기 위해 추가적으로 Library를 사용해야 한다.
* **Poor documentation** : 꾸준한 업데이트와 이를 지원하기위해 생성되는 Library들로 인해 빠르게 변화하여 적절한 지침을 작성할 시간이 없다.
* **Always changing** : 위에서 언급한 것처럼 지속적으로 변경되므로 개발자도 새로운 작업 방식에 적응해야한다.

#### React는 Framework인가? Library인가?

>  React는 JavaScript Library 라고 소개한다. Framework와 Library에 대한 명확한 구분이 없어 이 부분은 아직까지 많은 개발자들 사이에서 갑론을박 되는 내용인것 같다. 따라서 이 내용은 내 나름대로 검색을 통해 찾은 내용들을 정리한 것이다.

* Framework와 Library의 구분

  Framework와 Library의 차이는 Flow(흐름)에 대한 제어 권한이 어디에 있느냐의 차이이다. Framework는 전체적인 흐름을 자체적으로 가지고 있으며, 프로그래머가 그 안에 필요한 코드를 작성한다. 반면, Library는 사용자가 흐름에 대해 제어를 하며 필요한 상황에 가져다 쓰기만 한다.

* React의 Library적 특성

  * React는 단일 npm 설치로 배포되며 한가지 작업을 실행한다.
  * React 자체가 MVC 모든 부분을 수행하지 않는다. View만 rendering한다.
  * 확장 불가능 하다.

* React의 Framework적 특성

  * 클라이언트에서 수행하려는 작업의 대부분은 React 내에서만 수행 할 수 있다.
  * 완전한 기능을 갖춘 DOM 조작 및 상태 엔진이다.
  * Companion libraries가 어떻게 작동해야 하는지 따라야할 옵션이 있다.



### Vue.js

 기능, 비교적 쉬운 learning curve, 효율적이고 빠르며 정교한 SPA를 생성할 수 있어 Github에서 가장 많은 Stars를 받은 JavaScript Framework 중 하나이다.

 Vue에 대해 설명할 때 상대적으로 유사한 React 와 많이 비교한다. Vue와 React의 유사점을 비교해보면 다음과 같다.

* 가상 DOM을 사용한다.
* reactive, composable 한 Veiw component 를 가진다.
* 핵심 라이브러리에 집중하고 routing과 같은 다른 중요한 작업들의 처리를 남겨두었다.

#### 특징

* **성능(Overall performance)** : 매우 빠르고 압축후 18KB 밖에 되지 않는 작은 크기이다.
* **사용하기 쉽다(Ease of use)** : Angular 와 다른 Framework 들과 비교했을때 배우기 쉽다.
* **잘 정리된 공식 문서(Great documentation)** : 공식 문서가 체계적으로 잘 정리되어있어 사용자에게 유용하다.
* **손쉬운 프로젝트 통합(Easy project integration)** : 프로젝트에서 Vue를 즉시 사용할 수 있다.

#### 단점

* 소규모 커뮤니티 : 출시된지 얼마 되지않아 공식 문서가 아닌 다른 곳에서 React, Angular에 비해 정보를 얻기 힘들다.