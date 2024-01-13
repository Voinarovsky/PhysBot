x = int(input())
y = int(input())
z = int(input())

def solution(x, y, z):
    j = 0
    i = j + x
    k = i + z
    res = [i, j, k]
    return res

result = solution(x, y, z)
for i in result:
    print(i)