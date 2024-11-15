x,y,z = map(int, input().split())
if x>z:
    print("0")
elif z<(x+y):
    print("1")
else:
    print("2")
