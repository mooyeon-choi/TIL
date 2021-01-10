# Vanilla JS Basic

> 간단한 템플릿 프로젝트를 만들어보며 익히는 Vanilla JS FE 개발

## 목차

* [Template 만들기](#template-만들기)
  * [필요한 툴 설치](#필요한-툴-설치)
  * [Getting Started](#getting-started)
* [OOP](#oop)
* [Functional Programming](#functional-programming)

## Template 만들기

> project 생성하기

### 필요한 툴 설치

#### node.js

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

  ![download nodejs](https://github.com/mooyeon-choi/TIL/blob/master/web/frontend/react/getting_started/images/download_nodejs.png?raw=true)

* node, npm version 확인

  ```bash
  node -v
  v14.15.1
  
  npm -v
  6.14.8
  ```

#### yarn

* yarn 이란?

  * facebook에서 만들어진 Package Manager
  * npm에서 버전관리, 성능, 보안 문제를 보완 및 개선
  * npm에서 쓰는 `package.js`와 호환가능

* npm을 사용해 설치

  ```bash
  npm install yarn --global
  ```

### Getting Started

> 프로젝트 진행을 위한 기본적인 뼈대 갖추기

#### index.html 생성

```html
<!-- ! + tab -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```

#### package.json

* using npm module

  ```bash
  npm init
  ```

* using yarn module

  ```bash
  yarn init
  ```

#### 필요한 툴 추가하기

* using npm

  * [공식문서](https://docs.npmjs.com/specifying-dependencies-and-devdependencies-in-a-package-json-file)

  ```bash
  npm install <package-name> [--save-prod]
  npm install <package-name> --save-dev
  ```

  * `npm install <package-name>` or `npm install <package-name> [--save-prod]`

    To add an entry to the `"dependencies"`

  * using `--save-dev`

    To add an entry to the `"devDependencies"`

* using yarn

  * [공식문서](https://classic.yarnpkg.com/en/docs/managing-dependencies)

  ```bash
  yarn add [package]
  yarn add --dev [package]
  ```

  * `yarn add [package]`

    To add an entry to the `"dependencies"`

  * using `--dev`

    To add an entry to the `"devDependencies"`

##### Babel

* [Babel Usage Guide](https://babeljs.io/docs/en/usage)

* using npm

  ```bash
  npm install --save-dev @babel/core @babel/cli @babel/preset-env
  npm install --save @babel/polyfill
  ```

  설치 완료 후 `project` 폴더 내에 `babel.config.json` 파일 생성

  ```json
  {
    "presets": [
      [
        "@babel/env",
        {
          "targets": {
            "edge": "17",
            "firefox": "60",
            "chrome": "67",
            "safari": "11.1",
          },
          "useBuiltIns": "usage",
          "corejs": "3.6.5",
        }
      ]
    ]
  }
  ```

##### Webpack

* [npmjs Webpack package](https://www.npmjs.com/package/webpack)

* using npm

  ```bash
  npm install --save-dev webpack
  ```

* using yarn

  ```bash
  yarn add webpack --dev
  ```

##### Jest

> 코드가 제대로 동작하는지 확인하는 **test case**를 만드는 **Testing Framework**

* [Jest Docs - Getting started](https://jestjs.io/docs/en/getting-started)

* using npm

  ```bash
  npm install --save-dev jest
  ```

* using yarn

  ```bash
  yarn add --dev jest
  ```

## OOP

* [바로가기](./oop)

```
Class를 활용하여 객체 지향 프로그래밍(Object Oriented Programming) 방식의 개발 방법을
간단한 프로젝트를 개발하며 익혀보자
```

## Functional Programming

* [바로가기](./functional)

```
Function을 활용한 함수형 프로그래밍(Functional Programming) 방식의 개발 방법을
간단한 프로젝트를 개발하며 익혀보자
```





