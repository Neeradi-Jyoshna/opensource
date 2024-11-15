x, y, z = map(int, input().split())
remain_capa = z - y
max_mangoes = max(0, remain_capa // x)
print(max_mangoes)
