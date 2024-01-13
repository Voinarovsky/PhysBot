x = int(input())
y = int(input())
z = int(input())

def solution(x, y, z):
    su_per = x + y + z
    for i in range(-su_per, su_per + 1):
        for j in range(-su_per, su_per + 1):
            k = su_per - i - j
            if abs(i + j + k) == su_per and i + j == su_per - x and j + k == su_per - y:
                return [i, j, k]

result = solution(x, y, z)
for i in result:
    print(i)
