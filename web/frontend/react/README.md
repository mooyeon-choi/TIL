# React

## 목차





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

  

  

