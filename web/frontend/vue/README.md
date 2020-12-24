# Vue

## 목차

* [필요한 툴 설치](#필요한-툴-설치)
* [Getting Started](#getting-started)



## 필요한 툴 설치

### node.js

* node.js 란?

  * 어느곳에서나 JavaScript로 프로그래밍이 가능하게 하는 framework
  * server-side rendering, command line tools 등에 사용

* npm 이란?

  * Package Manager
  * library, package 들을 쉽게 관리할 수 있도록 해줌
  * `package.json` 파일안에 사용하는 외부 라이브러리들과 버전 정보들이 들어있다.

* npx 란?

  * 원하는 library, package를 실행할 수 있도록 해줌

  * 실행하는 방법

    ```bash
    npx "some-package"
    ```

* [node.js 공식사이트](https://nodejs.org/en/)

  ![download nodejs](C:/Users/moo/Desktop/TIL/web/frontend/react/images/download_nodejs.PNG)

* node, npm version 확인

  ```bash
  node -v
  v14.15.1
  
  npm -v
  6.14.8
  ```



## Getting Started

### Vue 개발환경 만들기

#### `package.json` 파일 생성

```bash
npm init
```

#### Vue 설치

```bash
npm install vue
```

#### Webpack 설치 

>  `webpack.config.js` 파일 생성

```bash
npm install webpack webpack-cli -D
```

* webpack은 개발환경에서 `모듈 번들러`로써 활용하기 위한 것으로 `-D`옵션을 통해 `package.json`에서 `DevDependencies`에 추가

#### Vue 파일들을 번역, 불러오기 위한 작업

```bash
npm install vue-loader vue-template-compiler -D
```

* `vue-loader` : Vue 파일을 불러오는 역할
* `vue-template-compiler` : Vue 파일을 해석하는 역할

#### index.html에 사용하기

```html
<script src="../dist/app.js"></script>
```

* 생성된 `app.js` 파일을 `index.html`에 위와 같이 삽입하면 Vue Component를 사용할 수 있다. 

#### 변경사항 적용

```bash
npm run build
```

* 변경사항이 생긴다면 위 명령어로 적용해주자

#### Style

> CSS 불러오기

```bash
npm install vue-style-loader css-loader -D
```

* `vue-style-loader` : vue의 style
* `css-loader` : webpack css를 불러오는 로더

```js
// webpack.config.js // module -> rules 에 추가
{
    test: '/\.css$/',
    use: ['vue-style-loader', 'css-loader'] // 앞에꺼가 css를 만들거고 뒤에꺼가 불러와서 처리해준다
}
```



