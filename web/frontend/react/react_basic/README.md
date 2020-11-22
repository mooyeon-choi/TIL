# React Basic

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
    
    ```

    * `components/` : 공통적으로 사용하는 component들을 보통 하나의 폴더로 묶어서 관리해준다.

    * 파일이름은 보통 소문자로 시작한다.

    * react component 파일은 `.jsx` 로 저장하여 JavaScript 파일과 구분

      ![.jsx Vs. .js](./images/jsxVsJs.png)

      





