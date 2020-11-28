# React Basic

## 목차

* [전반적인 개념](#전반적인-개념)
  * [Component](#component)
* [Template 프로젝트 만들기](#template-프로젝트-만들기)
  * [Project 생성](#project-생성)
  * [사용하지 않는 파일 삭제](#사용하지-않는-파일-삭제)
* [간단한 프로젝트로 배우기(Habit tracker)](#간단한-프로젝트로-배우기)
  * [Template 복사하기](#template-복사하기)
  * [React Dom](#react-dom)
  * [JSX 정리](#jsx-정리)
  * [Habit tracker](#habit-tracker)
    * [habit component 만들기](#habit-component-만들기)
    * [Fontawesome 추가](#fontawesome-추가)
    * [State 이해하기](#state-이해하기)
    * [Props란](#props란)
    * [Ref](#ref)

## 전반적인 개념

### Component

* Class와 Function 두가지 형태로 만들 수 있다.

* Class

  >  React.Component, React.PureComponent

  

  ```react
  class LikeButton extends Component {
      state = {};
  	render() {}
  }
  ```

  * React에서 제공하는 Component 클래스를 extends, 상속해서 만들 수 있다.
  * 내 Component에 State가 있고 그 상태에 따라 Component가 주기적으로 업데이트 되어야 할 때
  * Component에서 가지고 있는 상태, 데이터를 담을 수 있는 `state` object가 들어있다.
  * `state`가 변경이 되면 `render()` 함수가 호출 되면서 업데이트된 내용이 사용자에게 보여짐
  * lifecycle methods
    * 다양한 컴포넌트의 상태에 따라서 우리가 함수를 구현해 놓으면 알아서 불러주는 Method가 있다.
      * Component가 사용자에게 보여질때
      * DOM tree에 올라갔을 때
      * DOM tree에서 나왔을 때
      * Component가 업데이트 되었을 때

* Function

  > function, memo(function), React Hook

  

  ```react
  function App() {
      return <h1>Hello</h1>
  }
  ```

  * 내 Component에 상태가 없고 정적으로 데이터가 표시될 때
  * `state`, lifecycle methods가 없다. (16.8 이전 버전)
  * React Hook(16.8 버전부터)
    * `state`, lifecycle methods를 사용할 수 있게 됨
    * 기존에 Class Component에서 할 수 있던 기능을 Function에서도 가능하도록 해주었다.
    * 개발 배경
      * Class 구조에 익숙하지 않은 개발자들이 많다.
      * Class에서 멤버변수에 접근할 때 항상 `this.`을 붙여야해서 불편하다.
      * Class의 Binding issue
      * Functional programming의 유행
      * 중복되는 코드를 줄일 수 있다.

## Template 프로젝트 만들기

### Project 생성

```bash
yarn create react-app template
```

### 사용하지 않는 파일 삭제

* 다음 파일들은 아직 사용하지 않으므로 제거

    ```
    \template
    ├── public
    |  ├── logo192.png
    |  ├── logo512.png
    |  ├── manifest.json
    |  └── robots.txt
    ├── src
    |  ├── App.test.js
    |  ├── logo.svg
    |  ├── reportWebVitals.js
    |  └── setupTests.js
    ```
    
* 최종 Directory Tree 형태

    ```
    \template
    ├── node_modules/
    ├── package.json
    ├── public/
    |  ├── favicon.ico
    |  └── index.html
    ├── README.md
    ├── src/
    |  ├── app.css
    |  ├── app.jsx
    |  ├── components/
    |  ├── index.css
    |  └── index.js
    └── yarn.lock
    ```
    
    * `components/` : 공통적으로 사용하는 component들을 보통 하나의 폴더로 묶어서 관리해준다.
    
    * 파일이름은 보통 소문자로 시작한다.
    
    * react component 파일은 `.jsx` 로 저장하여 JavaScript 파일과 구분
    
      ![.jsx Vs. .js](./images/jsxVsJs.PNG)
    
      

## 간단한 프로젝트로 배우기

> Habit tracker

### Template 복사하기

```bash
cp -R template habit-tracker
```

* template의 상위 디렉토리에서 입력

### React Dom

* 우리가 만든 컴포넌트를 `html`과 연결해 준다.

* `index.html`

  ```html
  <body>
      ...
      ...
      <div id="root"></div>
  </body>
  ```

* `index.js`

  ```react
  ReactDOM.render(
    <React.StrictMode> // js의 "use strict"와 같은
      <App />
    </React.StrictMode>,
    document.getElementById("root")
  );
  ```

* `index.html`의 `root div` 에 최상위 컴포넌트인 `App`을 연결해준다.

### JSX 정리

> React Component와 JavaScript code 파일을 구분하기 위해 `app.jsx` 로 만들어주었다. 그럼 JSX란 무엇일까?

* 공식문서

  * [Introducing JSX](https://reactjs.org/docs/introducing-jsx.html)
  * [JSX In Depth](https://reactjs.org/docs/jsx-in-depth.html)

* JSX가 없었을때 React 작성법

  ```react
  function App() {
      return React.createElement('h1', {}, 'Hello:)');
  }
  ```

  * 코드가 복잡하고 어려웠다.

* `html` 처럼 입력할 수 있도록 해주는 JSX

  ```react
  function App() {
      return <h1>Hello:)</h1>
  }
  ```

  * `html`처럼 작성할 수 있지만 JSX는 JavaScript code이다.

* 비즈니스 로직 작성

  ```react
  function App() {
      const name = 'moo';
      return <h1>Hello {name} :)</h1>
  }
  ```

  ```react
  function App() {
      const name = 'moo';
      return (
          <>
              {name && <h1>Hello! {name}:)</h1>}
              // name이 있다면 && 뒤의 태그를 출력
          	
              {[1, 2].map(item => 
              	(<h1>{item}</h1>)}
          <>
      )
  }
  ```

  

* `tag` 묶어주기 

  * `<div></div>`

      ```react
      function App() {
          const name = 'moo';
          return (
              <div>
                  <h1>Hello! {name} :)</h1>
                  <h1>Hello!</h1>
              </div>
          )
      }
      ```
      
      * div tag가 만들어짐
      
  * `React.Fragment`

      ```react
      function App() {
          const name = 'moo';
          return (
              <React.Fragment>
                  <h1>Hello! {name} :)</h1>
                  <h1>Hello!</h1>
              </React.Fragment>
          )
      }
      ```

      * 따로 tag 가 만들어지지 않고 묶어준다.

  * 의미 없이 단순히 그룹으로 묶어주고만 싶을때

      ```react
      function App() {
          const name = 'moo';
          return (
              <>
                  <h1>Hello! {name} :)</h1>
                  <h1>Hello!</h1>
              </>
          )
      }
      ```

      * tag안을 비워도 동작한다.

### Habit tracker

#### habit component 만들기

* `rcc` + tap 을 누르면 자동으로 기본적인 코드가 써진다

  (React code snippet extension이 설치된 경우)

* file name은 소문자로 class name은 대문자로 시작!

  `rcc` + tap을 사용할 경우 파일명과 똑같이 써주므로 고쳐줘야한다.

#### Fontawesome 추가

* 설치

  ```bash
  yarn add @fortawesome/fontawesome-free
  ```

* 공식문서

  * https://fontawesome.com/how-to-use/on-the-web/using-with/react

* Fontawesome에서 검색해서 추가하기

  * 상단 검색창에서 원하는 icon 검색

  * 원하는 아이콘 선택후 태그를 클릭하면 복사된다.

    ![fontawesome icon](./images/fontawesome_icon.PNG)

  * react에서는 `className`을 쓰므로 `class`를 `className` 으로 고쳐준다.

#### State 이해하기

* Component 안에는 State라는 멤버변수가 있고 그 변수는 Object이다.

* State가 변경되면 react가 `render()` 함수를 호출하여 UI가 업데이트 된다.

  * 이때 State가 변경되었다는 것을 알게 하기 위해선 꼭 `setState()` method를 호출해야 한다.

* `setState()`

  * 동작 방식

    ```
    함수가 호출되면 현재 component가 가지고 있는 State(`this.state`)와 업데이트 해야하는 새로운 State(setState 함수의 인자로 전달된 새로운 Object) 두가지를 비교하여 업데이트가 필요한 경우 `render()` method를 호출한다.
    ```
    
  * 비동기 API

    ```
    `setState()`도 webAPIs 중 하나인 setTimeout, setInterval과 같은 비동기 method이다.
    따라서 setState를 호출하면 task queue에 저장되고 cycle이 돌때 하나씩 실행이된다.
    ```

* State 자체를 수정하면 안되는 이유

  * react에서는 상태를 직접적으로 수정하지말자!
    * 절대 안된다! 라고 하지 않는 이유는 State를 직접적으로 수정하는 것을 막아놓거나 수정한다고 해서 심각한 오류가 나오는 것은 아니기 때문
  * react state는 Immuatability를 항상 유지하는 것이 좋다.
  * State를 직접적으로 수정하는게 좋지 않은 이유
    1. setState는 비동기적으로 동작한다.
       * setState는 task queue에 저장되므로 setState에 의해 이전에 변경된 state가 다시 덮어 씌워진다.
    2. `PureComponent`에서 동작하지 않는다
       * `PureComponent` 에서는 `this.state` 와 `setState()`의 object를 비교하여 업데이트가 필요한 경우에만 `render()` method를 호출해 Rerendering 해준다.
       * State를 직접적으로 수정해 `this.state` 와 `setState()` 의 object가 같아진다면 두 레퍼런스가 동일하므로 업데이트가 필요 없다고 판단해 `render()` 함수를 호출해 주지 않는다.

#### Props란

* Component 밖에서 주어지는 데이터

* 부모 컴포넌트에서

  ```react
  <Child title={'Like'} onClick={this.handleClick} />
  ```

  와 같이 Props를 전달해주면 자식 컴포넌트에서 `this.props.title`, `this.props.onClick`으로 각각 전달된 `Like`와 `this.handleClick()` 함수에 접근할 수 있다.

* 자식 컴포넌트에서 `Props` 한번에 변수로 저장하기

  ```react
  const { name, count } = this.props.habit;
  ```

  위와 같이 `{ }` 로 묶어서 한번에 변수로 저장 할 수 있다.

* List Prop

  * 리스트를 넘겨줄때는 고유한 `key`를 가지고 있어야한다.

    * 이때 배열의 index를 사용해주면 안된다.

      -> 순서가 바뀌게 되었을때 index가 달라질 수 있기때문

  * 리스트의 값들을 변경해줄때도 마찬가지로 `setState()`를 사용해야 한다. 따라서 `this.state.list`를 복사하여 `setState()`에 넣어준다.

    ```react
    const habits = [...this.state.habits]; // this.state.habits를 복사
    const index = habits.indexOf(habit);
    habits[index].count++;
    this.setState({ habits }); // { habits : habits } 와 같이 동일한 이름의 데이터는 한번에 써줄 수 있다.
    ```

* event 처리

  * method를 `props`로 넘겨줘서 처리

  * 처리방법

    * `render()`의 태그안에 직접 입력

      ```react
      <button 
          className="habit-button habit-delete"
          onClick={() => {
              this.props.onDelete(this.props.habit)
          }}
      >
      ```

      * `render()` 함수는 Rerendering 될 때 마다 항상 다시 실행된다.
      * `render()` 함수가 호출될 때 마다 `arrow function`이 반복적으로 생성된다. 
      * 보통의 경우 문제가 되지 않지만 문제가 될 수 있어 멤버변수로 사용하는 것을 권장

    * Member 변수로 만들어주어서 사용

      ```react
      handleIncrement = () => {
          this.props.onIncrement(this.props.habit);
      }
      ```

      * 만들어진 `arrow function` 이 `handleIncrement`에 할당되어져 있어 한번만 생성된다.

#### Ref

* [공식문서](https://reactjs.org/docs/refs-and-the-dom.html)

* React에서는 Dom element를 직접적으로 다루지 않기 때문에 React에서 다른 React 요소에 접근하려면 `Ref`를 써야한다.

* 사용법

  ```react
  class HabitAddForm extends Component {
  
    inputRef = React.createRef();
    ...
    ...
    render() {
      return (
        <form>
          <input ref={this.inputRef}>
          ...
          ...
        </form>
      );
    }
  }
  ```

  1. 멤버 변수 입력

     `inputRef = React.createRef();`

     `Ref`를 만들어줄땐 변수명에 항상 `000Ref`라고 만들어주자

  2. 원하는 요소의 `ref={}`에 전달해준다.

     `<input ref={this.inputRef}>`

* 동작 원리

  1. `Component` 가 브라우저에 표기되면 `<input>` element가 `inputRef`와 연결된다.
  2. 이렇게 연결된 요소를 통해 해당하는 데이터를 읽어올 수 있다.

* `Ref`에 저장된 요소 확인

  ```react
  this.inputRef.current.value;
  ```

* `form` 요소에 저장된 값 초기화해주기

  ```react
  class HabitAddForm extends Component {
  
    formRef = React.createRef();
    inputRef = React.createRef();
    ...
    ...
    function = () => {
        this.formRef.current.reset();
    }
    render() {
      return (
        <form ref={this.inputRef}>
          <input ref={this.inputRef}>
          ...
          ...
        </form>
      );
    }
  }
  ```

  * `form` 요소 안에 값을 리셋해 줄땐 `form.reset()`을 사용하자

