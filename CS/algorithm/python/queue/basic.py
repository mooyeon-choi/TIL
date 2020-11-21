Q = [0] * 10
front = rear = -1

def enqueue(item):
    global rear
    # full 상태 체크
    if rear == N - 1:
        return
    rear += 1
    Q[rear] = item

def dequeue():
    global front
    # empty 상태 체크
    if front == rear: return
    front += 1
    return Q[front]

Q = []
Q.append(1)
while len(Q) > 0:
    Q.pop(0)