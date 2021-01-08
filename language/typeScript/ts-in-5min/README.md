# 5분 만에 보는 TypeScript

> TypeScript가 무엇인지, 어떻게 사용하는지 간략하게 미리 보자

## 목차

* [타입 추론 (Types by Inference)](#타입-추론-types-by-inference)

## 타입 추론 (Types by Inference)

 TypeScript는 JavaScript 위에서 동작하기 때문에 변수를 생성하면서 동시에 특정값에 할당하는 경우, TypeScript는 그 값을 해당 변수의 타입으로 사용한다.

```typescript
let helloWorld = "Hello World"
```

 VS Code로 JavaScript 작업을 할 때 편집기의 자동 완성 기능을 많이 사용해왔을 것이다. 이는 TypeScript에 쓰이는 JavaScript에 대한 이해가 JavaScript 작업을 개선하기 위해 내부적으로 사용되었기 때문이다.

## 타입 정의하기 (Defining Types)

 JavaScript는 다양한 디자인 패턴을 가능하게 하는 동적 언어이다. 몇몇 디자인 패턴은 자동으로 타입을 제공하기가 힘든데(동적 프로그래밍을 사용하고 있을 것이기 때문에) 이러한 경우에 TypeScript는 타입이 무엇이 되어야 하는지 명시 가능한 JavaScript 언어의 확장을 지원한다.

 다음은 `name: string`과 `id: number`을 포함하는 추론 타입을 가진 객체를 생성하는 예제이다.

```typescript
const user = {
    name: "Hayes",
    id, 0
};
```

 이 객체의 형태를 명시적으로 나타내기 위해서는 `interface`로 선언한다.

```typescript
interface User {
    name: string;
    id: number;
}
```

 이제 변수를 선언할 때 뒤에 `: TypeName` 구문을 사용해 JavaScript 객체가 `interface`의 형태를 따르고 있음을 선언할 수 있다.

```typescript
interface User {
    name: string;
    id: number;
}

const user: User = {
    name: "Hayes",
    id: 0,
}
```

 해당 인터페이스에 맞지 않는 객체를 생성하면 TypeScript는 경고를 준다.

```typescript
// @errors: 2322
interface User {
    name: string;
    id: number;
}

const user: User = {
    username: "Hayes",
    id: 0,
}
```

 클래스와 객체 지향 프로그래밍 또한 TypeScript로 만들 수 있다.

```typescript
interface User {
    name: string;
    id: number;
}

class UserAccount {
    name: string;
    id: number;
    
    constructor(name: string, id: number) {
        this.name = name;
        this.id = id;
    }
}

const user: User = new UserAccount("Murphy", 1);
```

 인터페이스는 함수에서 매개변수와 리턴값을 명시하는데 사용되기도 한다.

```typescript
interface User {
    name: string;
    id: number;
}

// return값
function getAdminUser(): User {
    //...
}

// 매개변수
function deleteUser(user: User) {
    //...
}
```



 TypeScript에서는 JavaScript에서 기본적으로 제공하는 원시타입(`boolean`, `number`, `string`, `null`, `undefined`, `symbol`) 외에도 `any`, `unknown`, `never`, `void` 등 이 추가된다.

