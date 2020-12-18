n = int(input())
for _ in range(n):
    bracket = input()
    hashmap = {'(': 0, '[': 0}
    answer = 0
    for b in bracket:
        if b == '(': hashmap['('] += 1
        elif b == '[': hashmap['['] += 1
        elif b == ')':
            if hashmap['(']:
                hashmap['('] -= 1
                answer += 1
        elif b == ']':
            if hashmap['[']:
                hashmap['['] -= 1
                answer += 1
    print(answer)