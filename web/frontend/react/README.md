# React

## 목차

* [How to start React](#how-to-start-react)
* [React Basic](#react-basic)
* [PureComponent](#pure-component)



## How to start React

* [바로가기](./getting_started) 

```
React 개발을 시작하기 위해 필요한 툴 설치 및 환경설정🏃
```

1. 필요한 툴 설치
2. Getting Started
3. 프로젝트 구조
4. 숨겨진 툴

## React Basic

* [바로가기](./react_basic/)

```
간단한 템플릿 프로젝트를 만들어보며 알아보는 React 기초
```

1. 전반적인 개념
2. Template 프로젝트 만들기
3. 간단한 프로젝트로 배우기(Habit tracker)

## PureComponent

* [바로가기](./pure_component)

```
React는 VDOM으로 해당 Component나 상위 Component의 state가 변경되었을 때만 DOM 요소를 업데이트 해준다.

하지만 PureComponent를 사용하는 이유를 찾아보면 또 state가 변경될 때 마다 모든 Component가 re-render 된다고 한다.😵

DOM 요소가 업데이트 되는 것과 re-render는 어떤 차이가 있는걸까❓

또 왜 re-render가 되면 성능에 영향을 끼치는 걸까❓
```

1. React의 중요한 컨셉
2. Habit Tracker 다시 살펴보기
3. Render 함수의 호출
4. Component 정리
5. PureComponent를 사용하는 이유
6. React Dev Tools로 re-render 확인하기
7. PureComponent와 memo
8. Habit에 PureComponent 적용하기