# React

## 목차

* [필요한 툴 설치](#필요한-툴-설치)
* [Getting Started](#getting-started)
* [프로젝트 구조](#프로젝트-구조)
* [숨겨진 툴](#숨겨진-툴)
* [React Basic](#react-basic)



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

  ![download nodejs](./images/download_nodejs.png)
  
* node, npm version 확인

  ```bash
  node -v
  v14.15.1
  
  npm -v
  6.14.8
  ```



### yarn

* yarn 이란?
  * facebook에서 만들어진 Package Manager
  * npm에서 버전관리, 성능, 보안 문제를 보완 및 개선
  * npm에서 쓰는 `package.js`와 호환가능

* npm을 사용해 설치

  ```bash
  npm install yarn --global
  ```



## Getting Started

> `create react-app` 을 통해 생성되는 프로젝트에 포함된 툴은 어떤것이 있는지 알아본다.

* [React 공식문서](https://reactjs.org/docs/create-a-new-react-app.html)

* project 생성

  ```bash
  yarn create react-app 'project name'
  ```

  * 처음 생성시 1분정도 소요

  * 프로젝트가 생성되면 가능한 명령어 목록이 표시된다.

    ```bash
    ...
    Inside that directory, you can run several commands:
    
      yarn start // 실행
        Starts the development server.
    
      yarn build // 실행x 만든 앱을 배포할 수 있도록 build
        Bundles the app into static files for production.
    
      yarn test // 작성한 unit test를 실행해서 성공 or 실패 여부 출력
        Starts the test runner.
    
      yarn eject // 받아진 package, library들을 하나하나 확인, 수정 할 때
        Removes this tool and copies build dependencies, configuration files
        and scripts into the app directory. If you do this, you can’t go back!
    
    We suggest that you begin by typing:
    
      cd test
      yarn start
    
    Happy hacking!
    Done in 73.20s.
    ```

* Project 실행

  ```bash
  yarn start
  ```

  ![start page](./images/start.png)

* Project 중지

  `ctrl + c`

## 프로젝트 구조

```bash
project
├── .gitignore
├── node_modules/
├── package-lock.json
├── package.json
├── public/
|  ├── favicon.ico
|  ├── index.html
|  ├── logo192.png
|  ├── logo512.png
|  ├── manifest.json
|  └── robots.txt
├── src/
|  ├── App.css
|  ├── App.js
|  ├── App.test.js
|  ├── index.css
|  ├── index.js
|  ├── logo.svg
|  ├── reportWebVitals.js
|  └── setupTests.js
├── README.md
└── yarn.lock

```

### .gitignore

### package.json

* npm에서 버전을 관리할때 내 프로그램에서 사용하는 외부 라이브러리와 그 라이브러리 들의 버전이 명시되어 있다.

  ```json
  {
    "name": "test", // 어플리케이션 이름
    "version": "0.1.0", // 어플리케이션 버전
    "private": true, // private or public
    "dependencies": { // 사용하는 외부 라이브러리
      "@testing-library/jest-dom": "^5.11.4",
      ...
    },
    "scripts": { // yarn "scripts" 입력시 실제 scripts
      "start": "react-scripts start",
      ...
    },
    ...
  }
  ```

### README.md

### yarn.lock

* yarn을 이용할 경우 설치됨

### node_modules/

* 외부 라이브러리를 추가했을때 자동적으로 추가됨
* 라이브러리 구조 확인 가능

### public/

* 사용자에게 배포할 때 외부적으로 보여지는 것들
* `farvicon.ico`, `index.html`, logo image 등
* `manifest.json
  * pwa(프로그래시브 웹 어플리케이션), 모바일에서 저장하는 웹어플리케이션을 만들 때 사용
* `robots.txt`
  * 웹 크롤링을 위해 사용됨

### src/

* 소스코드
* `index.js`, `app.js` 등

## 숨겨진 툴

### create react-app

* 라이브러리를 이용해서 project를 간편하게 만드는 페이스북에서 만든 패키지
* `create react-app project-name`을 이용해서 프로젝트 생성시 깃도 초기화된다.
  * `.git` 파일도 같이 생성됨

### yarn eject

* 포함된 툴들을 모두 열어서 볼 수 있다.

* 내부를 수정하면 되돌릴 수 없으므로 사용시 주의해야한다.

  ```bash
  yarn eject
  ```

* `config/` directory 생성

* `package.js`에 `babel`, `postcss` 등 숨겨져있던 패키지들도 보여준다.

### Babel

* JavaScript transcompiler
* ECMAscript 2015+ 버전의 코드를 이전 버전으로 변환해준다.
* TypeScript, JSX 를 JavaScript로 변환해준다.

### Webpack

* Bundling the code, JavaScript module bundler
* 소스코드, 이미지, 리소스들을 하나로 묶어서 번들 단위로 사용자에게 제공할 수 있도록 해준다.(bundling)
* 소스코드를 줄여준다.
* 긴 변수나 함수의 이름을 해커, 다른 사람들이 알아보지 못하도록 수정

### ESLint

* checking your code
* Bundling the code, JavaScript module bundler
* 즉각적으로 코드에 잘못된 점이 있으면 경고 표시

### Jest

* delightful JavaScript testing framework
* Unit test를 할 수 있게 도와주는 testing framework

### PostCSS

* expandable CSS libraries
* CSS 전처리기 중 하나 (ex. less, sass)
* framework에 맞게 CSS를 작성하면 브라우저가 이해할 수 있는 CSS로 변환
* sass는 정해진 것들만 할 수 있는 반면 다양한 플러그인이 있어서 원하는 것을 조금 더 추가해서 할 수 있다.

## React Basic

> 간단한 템플릿 프로젝트를 만들어보며 알아보는 React 기초

* [자세히 보기](./react_basic/)