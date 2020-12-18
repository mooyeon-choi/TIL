for _ in range(int(input())):
  N, M = map(int, input().split())
  N_list = set(input().split())
  M_list = set(input().split())
  print(len(N_list & M_list))