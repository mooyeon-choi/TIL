def find():

n, m = map(int, input().split())
background = [list(map(int, input().split())) for _ in range(n)]
starti, startj, startd = map(int, input().split())
endi, endj, endd = map(int, input().split())
route = []

