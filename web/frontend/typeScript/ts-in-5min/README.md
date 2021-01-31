# 5분 만에 보는 TypeScript

> TypeScript가 무엇인지, 어떻게 사용하는지 간략하게 미리 보자

## 목차

* [타입 추론 (Types by Inference)](#타입-추론-types-by-inference)
* [타입 정의하기 (Defining Types)](#타입-정의하기-defining-types)
* [타입 구성 (Composing Types)](#타입-구성-composing-types)
  * [유니언 (Unions)](#유니언-unions)
  * [제네릭 (Generics)](#제네릭-generics)
  * [구조적 타입 시스템 (Structural Type System)](#구조적-타입-시스템-structural-type-system)

## 타입 추론 (Types by Inference)

 TypeScript는 JavaScript 위에서 동작하기 때문에 변수를 생성하면서 동시에 특정값에 할당하는 경우, TypeScript는 그 값을 해당 변수의 타입으로 사용한다.

```typescript
// 재사용 가능성이 없으면 그 자체를 타입으로 지정
const helloWorld = "Hello World" // type: "Hello World"

// 재사용 가능하면 데이터의 타입을 변수 타입으로 지정
let hiWorld = "Hi World" // type: string
```

 VS Code로 JavaScript 작업을 할 때 편집기의 자동 완성 기능을 많이 사용해왔을 것이다. 이는 TypeScript에 쓰이는 JavaScript에 대한 이해가 JavaScript 작업을 개선하기 위해 내부적으로 사용되었기 때문이다.

## 타입 정의하기 (Defining Types)

 JavaScript는 다양한 디자인 패턴을 가능하게 하는 동적 언어이다. 몇몇 디자인 패턴은 자동으로 타입을 제공하기가 힘든데(동적 프로그래밍을 사용하고 있을 것이기 때문에) 이러한 경우에 TypeScript는 타입이 무엇이 되어야 하는지 명시 가능한 JavaScript 언어의 확장을 지원한다.

 다음은 `name: string`과 `id: number`을 포함하는 추론 타입을 가진 객체를 생성하는 예제이다.

```typescript
const user = {
    name: "Hayes",
    id: 0
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

## 타입 구성 (Composing Types)

> 타입을 구축하기 위해서는 두 가지 구문이 있다. `interface`를 우선적으로 사용하되 특정 기능이 필요할 때는 `type`을 사용해야 한다.

 객체들을 조합하여 더 크고 복잡한 객체를 만드는 방법과 유사하게 TypeScript에는 타입으로 이를 수행하는 도구가 있다. 여러가지 타입을 합쳐 새 타입을 작성하기 위해 가장 많이 사용되는 두 가지 코드로는 유니언(Union)과 제네릭(Generic)이 있다.

### 유니언 (Unions)

 유니언은 타입이 여러 타입 중 하나일 수 있음을 선언하는 방법이다. 예를 들어, `boolean` 타입은 `true`또는 `false`로 선언된 아래의 코드와 같다.

```typescript
type MyBool = true | false;
```

> `MyBool` 위에 마우스를 올리면, `boolean`으로 분류되어 있을 것이다. 이는 구조적 타입 시스템의 프로퍼티이며, 자세한 내용은 아래의 [구조적 타입 시스템 (Structural Type System)](#구조적-타입-시스템-structural-type-system)에서 알아보자

 유니언 타입이 가장 많이 사용되는 사례 중 하나는 다음과 같이 허용되는 `string` 또는 `number`의 리터럴(Literal)집합을 설명할 때이다.

```typescript
type WindowStates = "open" | "closed" | "minimized";
type LockStates = "locked" | "unlocked";
type OddNumbersUnderTen = 1 | 3 | 5 | 7 | 9;
```

 유니언은 타입처리를 위해 다양한 방법을 제공한다. 아래와 같이 매개변수로 `array` 또는 `string`을 받는 함수를 정의할 수 있다.

```typescript
function getLength(obj: string | string[]) {
    return obj.length;
}
```

  타입을 구분하기 위한 기능도 제공하는데 아래의 표와 같이 표현한다.

| Type      | Predicate                          |
| --------- | ---------------------------------- |
| string    | `typeof s === "string"`            |
| number    | `typeof n === "number"`            |
| boolean   | `typeof b === "boolean"`           |
| undefined | `typeof undefined === "undefined"` |
| function  | `typeof f === "function"`          |
| array     | `Array.isArray(a)`                 |

 아래와 같은 방법으로 `obj`의 타입이 `string`인지 `array`인지 구분할 수 있다.

```typescript
function wrapInArray(obj: string | string[]) {
    if (typeof obj === "string") {
        return [obj];
    } else {
        return obj;
    }
}
```

### 제네릭 (Generics)

 제네릭은 C#, Java 등의 언어에서 재사용성이 높은 컴포넌트를 만들 때 자주 활용되는 특징이다. 특히, 한가지 타입보다 여러 타입에서 동작하는 컴포넌트를 생성하는데 사용된다.

```typescript
// 제네릭 사용예시
// Array
type StringArray = Array<string>;
type NumberArray = Array<number>;
type ObjectWithNameArray = Array<{ name: string }>;

// 제네릭을 사용하는 고유 타입 선언
interface Backpack<Type> {
    add: (obj: Type) => void;
    get: () => Type;
}

declare const backpack: Backpack<string>;

const object = backpack.get(); // string
backpack.add(23); // error // string으로 선언하여 number 사용 불가
```

### 구조적 타입 시스템 (Structural Type System)

 TypeScript의 핵심 원칙 중 하나는 타입 검사가 값의 형태에만 집중한다는 것이다. 이는 "덕 타이핑(duck typing)" 또는 "구조적 타이핑(Structural Type System)" 이라 불린다.

 구조적 타입 시스템에서 두 객체가 같은 형태를 가지면 같은 것으로 간주한다.

```typescript
interface Point {
    x: number;
    y: number;
}

function printPoint(p: Point) {
    console.log(`${p.x}, ${p.y}`);
}

const point = { x: 12, y: 26 };
printPoint(point); // "12, 26" 출력
```

 `point` 변수는 `Point` 타입으로 선언된 적이 없지만, TypeScript는 타입 검사에서 `point`의 형태와 `Point`를 형태를 비교하여 같은 것으로 처리한다.

 형태 일치는 일치시킬 객체 필드의 하위 집합만 비교한다.

```typescript
interface Point {
    x: number;
    y: number;
}

function printPoint(p: Point) {
    console.log(`${p.x}, ${p.y}`);
}

const rect = { x: 33, y: 3, width: 30, height: 80 };
printPoint(rect); // "33, 3" 출력
```

 Class와 Object를 비교할 때도 같은 원리가 적용된다.

```typescript
interface Point {
    x: number;
    y: number;
}

function printPoint(p: Point) {
    console.log(`${p.x}, ${p.y}`);
}

class VirtualPoint {
    x: number;
    y: number;

    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
    } 
}

const newVPoint = new VirtualPoint(13, 56);
printPoint(newVPoint); // "13, 56" 출력
```

