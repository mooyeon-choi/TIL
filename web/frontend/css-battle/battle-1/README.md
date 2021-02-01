# Battle #1 Pilot Battle

> [사이트 바로가기](https://cssbattle.dev/battle/1)

## 목차

* [Target #1 Simply Square](#target-1-simply-square)
* [Target #2 Carrom](#target-2-carrom)
* [Target #3 Carrom](#target-3-push-button)

## Target #1 Simply Square

* [문제](https://cssbattle.dev/play/1)

  ![problem1](./images/battle1.PNG)

* 풀이

  ```html
  <div></div>
  <style>
    * {
      margin: 0;
      background: #5d3a3a;
    }
    div {
      width: 200px;
      height: 200px;
      background: #b5e0ba;
    }
  </style>
  
  ```

  * 먼저 body의 margin을 지워주고 div크기를 맞춰주었다.

## Target #2 Carrom

* [문제](https://cssbattle.dev/play/2)

  ![problem2](./images/battle2.PNG)

* 풀이

  ```html
  <div id="first"></div>
  <div id="second"></div>
  <div id="third"></div>
  <div id="fourth"></div>
  <style>
    body {
      margin: 0;
      background: #62374e;
    }
    div {
      position: absolute;
      width: 50px;
      height: 50px;
      background: #fdc57b;
    }
    #first {
      top: 50px;
      left: 50px;
    }
    #second {
      top: 50px;
      right: 50px;
    }
    #third {
      bottom: 50px;
      left: 50px;
    }
    #fourth {
      bottom: 50px;
      right: 50px;
    }
  </style>
  ```

  * 기본적인 방법을 통해서 구현해주었다.
  * 4개의 `<div>`를 만들고 각각의 속성에 `top, bottom, left, right` 옵션을 주었다.

## [Target #3 Carrom](#target-3-push-button)

* [문제](https://cssbattle.dev/play/3)

  ![problem3](./images/battle3.PNG)

* 풀이

  ```html
  <div id="square">
    <div id="big">
      <div id="middle">
        <div id="small"></div>
      </div>
    </div>
  </div>
  <style>
    * {
      margin: 0;
      background: #6592CF;
    }
    
    div {
      position: relative;
    }
    
    #square {
      top: 75px;
      left: 50px;
      width: 300px;
      height: 150px;
      background: #243D83;
    }
    
    #big {
      top: -50px;
      left: 25px;
      width: 250px;
      height: 250px;
      border-radius: 125px;
      background: #6592CF;
    }
    
    #middle {
      top: 50px;
      left: 50px;
      width: 150px;
      height: 150px;
      border-radius: 75px;
      background: #243D83;
    }
    
    #small {
      top: 50px;
      left: 50px;
      width: 50px;
      height: 50px;
      border-radius: 25px;
      background: #EEB850;
    }
  </style>
  ```

  * `border-radius`를 활용해 원을 만들어줄 수 있다.