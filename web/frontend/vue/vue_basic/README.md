# Vue Basic

## 목차

* [Template 프로젝트 만들기](#template-프로젝트-만들기) 



## Template 프로젝트 만들기

### Project 생성

```bash
vue create template
```

* Directory Tree 형태

  ```
  template/
  ├── babel.config.js
  ├── node_modules/
  ├── package-lock.json
  ├── package.json
  ├── public/
  |  ├── favicon.ico
  |  └── index.html
  ├── README.md
  └── src/
     ├── App.vue
     ├── assets/
     ├── components/
     └── main.js
  ```

  * `components/` : 공통적으로 사용하는 component들을 보통 하나의 폴더로 묶어서 관리해준다.
  * 파일명은 Vue.js Style Guide를 따라 파스칼케이스로 만들어주었다.
  * Vue component 파일은 `.vue`로 저장한다.

## 간단한 프로젝트로 배우기

> Habit tracker

### Template 복사하기

```bash
cd -R template habit-tracker
```

* template의 상위 디렉토리에서 입력

### Vue Mount

* 공식 문서

  * [Lifecycle-Diagram](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram)
  * [mounted](https://kr.vuejs.org/v2/api/index.html#mounted)

* 우리가 만든 컴포넌트를 `html`과 연결해 준다.

* `public/index.html`

  ```html
  <body>
      ...
      ...
      <div id="app"></div>
  </body>
  ```

* `src/main.js`

  ```js
  new Vue({
    render: h => h(App),
  }).$mount('#app')
  ```

* `app` component는 Virtual DOM에 저장되고 `vm.$mount(el)`이 호출되었을 때 DOM에 업데이트 된다.

### VUE 정리

> Vue Component를 저장해주기 위해 `app.vue` 로 만들어 주었다. 그럼 `.vue` 란 무엇일까?

* 공식문서

  * [Vue Single-File Component (SFC)](https://vue-loader.vuejs.org/spec.html)

* `.vue` 가 없었을 때 Vue 작성법

  ```js
  // 등록
  Vue.component('my-component', {
    template: '<div>사용자 정의 컴포넌트 입니다!</div>'
  })
  
  // 루트 인스턴스 생성
  new Vue({
    el: '#example'
  })
  ```

* `html` 처럼 입력할 수 있도록 해주는 `.vue`

  ```vue
  <template>
    <h1>Hello :)</h1>
  </template>
  ```

#### 비즈니스 로직 작성

  ```vue
  <template>
    <div class="example">{{ msg }}</div>
	{{ ok ? 'YES' : 'NO' }}
  </template>
  ```

#### Language Blocks

```vue
<template>
  <div class="example">{{ msg }}</div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Hello world!',
      ok: true
    }
  }
}
</script>

<style>
.example {
  color: red;
}
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>
```

##### Template

* `vue-template-compiler`에 의해 JavaScript code로 Compile되어 html `<script>` section에 삽입된다.

##### Script

* Vue.js [Component option object](https://vuejs.org/v2/api/#Options-Data) 로 실행된다.
* ES Module을 실행하며, Webpack 규칙을 따른다.

##### Style

* CSS 코드를 입력할 수 있다.

##### Custom Blocks

* 이외에도 추가적으로 Custom Block을 만들어 줄 수 있다.
* [상세 내용](https://vue-loader.vuejs.org/guide/custom-blocks.html)

### Habit tracker

#### habit component 만들기

* `vueInit` + tap 을 누르면 자동으로 기본적인 코드가 써진다.

  (Vue 3 Snippets extention이 설치된 경우)

* file name은 두가지 이상 단어의 합성어로 PascalCase로 작성한다.

#### Fontawesome 추가

* 설치

  ```bash
  npm i --save @fortawesome/fontawesome-svg-core
  npm i --save @fortawesome/free-solid-svg-icons
  ## Using Vue 2.x
  npm i --save @fortawesome/vue-fontawesome@latest
  ```

* [공식문서](https://fontawesome.com/how-to-use/on-the-web/using-with/vuejs)

* `src/main.js`에 추가

  ```js
  import Vue from "vue";
  import App from "./App.vue";
  import { library } from "@fortawesome/fontawesome-svg-core";
  import { "사용할 icon" } from "@fortawesome/free-solid-svg-icons";
  import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
  
  library.add("사용할 icon");
  
  Vue.component("font-awesome-icon", FontAwesomeIcon);
  
  Vue.config.productionTip = false;
  
  new Vue({
    render: (h) => h(App),
  }).$mount("#app");
  ```

* Fontawesome에서 검색해서 추가하기

  * 상단 검색창에서 원하는 icon 검색

  * `src/main.js`에 icon 추가

    * import 목록에 추가

      `import { "사용할 icon" } from "@fortawesome/free-solid-svg-icons";`

    * `library`에 추가

      `library.add("사용할 icon");`

#### Data 이해하기

* Component 안에는 Data라는 함수가 있고 그 함수는 Object를 return 한다.

* Data의 각 속성들이 변경되면 Vue가 `vm.mount()` 함수를 호출하여 UI가 업데이트 된다.

  * 이때 Data의 각 속성들에 대해 shallow(얕게) 비교하므로 각 속성들의 Reference만 비교해준다.

    따라서, 속성에 Object가 저장되어있고 Object 내부의 값이 변경될 경우 Vue에서 변화를 감지하지 못한다.

#### 디렉티브

* `v-` 접두사가 있는 특수속성으로 표현식의 값이 변경될 때 바뀐 결과를 DOM에 적용한다.

  ```html
  <!-- 예시 -->
  <p v-if="seen">Now you see me</p>
  <!-- "seen"의 boolean 값에 따라 <p>가 생성/삭제된다. --> 
  ```

* `v-bind`

  * Data의 속성값을 가져올 수 있다.

  ```html
  <img v-bind:src="url" width=200px;>
  <!-- 약어 -->
  <img :src="url" width=200px;>
  ```

* `v-on`

  * Vue에서 DOM 이벤트를 들을 수 있게 해준다.

  ```html
  <!-- 예시 -->
  <button v-on:click="counter += 1">Add 1</button>
  <!-- 약어 -->
  <button @click="counter += 1">Add 1</button>
  ```

  이벤트 핸들러의 로직은 복잡하므로 주로 메소드의 이름을 호출하고 많은 수식어를 제공한다.

  자세한 내용은 이후 이벤트 수식어에서 알아보자.

* `v-model`

  * Data를 양방향으로 바인딩 해준다.

  * `v-model` 은 `v-bind`와 `v-on`으로 구현할 수 있다.

      다음 두 코드의 동작방식은 완전히 똑같다.

      ```html
      <input v-model="searchText">
      ```

      ```html
      <input
        v-bind:value="searchText"
        v-on:input="searchText = $event.target.value"
      >
      ```

* `v-for` 와 `v-if`

  > `v-for`는 `template`에서 for문을 사용할 수 있게 해주고`v-if` 는 if문을 사용하게 해준다.
  >
  > 이 둘은 같이 쓰이는 경우도 많으므로 같이 알아보자.

  * `v-for` 와 `v-if`를 같이 써줄 경우 `v-for`가 더 높은 우선순위를 가진다.

    따라서 `v-if`는 루프가 반복될 때마다 실행된다.

      ```html
    <!-- 예시 (권장하지 않음) -->
    <ul>
      <li
        v-for="user in users"
        v-if="user.isActive"
        :key="user.id"
      >
        {{ user.name }}
      </li>
    </ul>
      ```

      하지만 `v-for`가 더 높은 우선순위를 가지는 특성 때문에 이렇게 코드를 작성할 경우 `v-else` 와 이중 for문을 작성할 수 없는등 여러 문제가 발생 할 수 있어 매우 좋지 못한 습관이다.

  * `v-for`와 `v-if`를 혼용할 때는 다음의 Vue Style Guide 권장 사항을 따르자
    
      ```html
      <!-- 미리 필터링해준 List를 사용 -->
      <ul>
        <li
          v-for="user in activeUsers"
          :key="user.id"
        >
          {{ user.name }}
        </li>
      </ul>
      ```
      
      ```html
      <!-- v-if를 부모요소에 적용 -->
      <ul v-if="shouldShowUsers">
        <li
          v-for="user in users"
          :key="user.id"
        >
          {{ user.name }}
        </li>
      </ul>
      ```

* `v-for` 와 `key`

  * 서브트리의 내부 컴포넌트 상태를 유지하기 위해 `v-for` 는 항상 `key` 와 함께 사용한다.

* `v-if` 와 `v-show`

  * element를 조건부로 표시하기 위한 옵션
  * `v-if` 
    * 조건에 따라 블록을 렌더링한다.
    * 데이터 토글 비용이 높다.
  * `v-show` 
    * 항상 렌더링 되고 조건에 따라 CSS `display` 속성을 변경한다.
    * 초기 렌더링 비용이 높다.
  * 따라서 조건을 자주 변경해주어야 하는 경우 `v-show`, 조건이 변경되지 않을 경우 `v-if`가 선호된다.

#### Props와 Emit

##### Props란

* Component 밖에서 주어지는 데이터

* 부모 컴포넌트에서

  ```html
  <child message="안녕하세요!"></child>
  ```

  와 같이 Props를 전달해주면 자식 컴포넌트에서 

  ```html
  <template>
  	<span>{{ message }}</span>
  </template>
  ```

  ```js
  props: ['message'] // 권장하지 않음 자동으로 타입 구분
  props: {           // 권장
      message: String
  }
  ```

  와 같이 `props`를 받아와서 사용할 수 있다.

