year = int(input())
print(1 if not year % 400 else 0 if not year % 100 else 1 if not year % 4 else 0)