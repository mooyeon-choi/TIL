let numbers = [10, 1, 3, 5];

numbers[0]; // 10
numbers[-1]; // undefined
numbers.length; // 4

numbers.reverse(); // return + 원본 변경.
numbers.push(20); // 마지막에 원소 추가 + return (길이)
numbers.pop(); // 20 : 마지막 원소 pop + return (해당 원소)
numbers.unshift(3); // 맨앞에 원소 추가 + return (길이)
numbers.shift(); // 맨앞 원소 제거 + return (해당 원소)

numbers.includes(1); // true : 포함여부 확인
numbers.indexOf(1); // 가장 먼저 존재하는 위치

numbers.join(); // 기본이 ,
numbers.join("-"); // -로 연결.
