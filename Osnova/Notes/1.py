x = int(input())
y = int(input())
z = int(input())

def solution(x, y, z):
    su_per = x + y + z
    for i in range(-su_per, su_per + 1):
        for j in range(-su_per, su_per + 1):
            for k in range(-su_per, su_per + 1):
                if abs(i - j) == x and abs(j - k) == y and abs(k - i) == z:
                    res = [i, j, k]
                    return res
                if abs(i - j) > x:  # оптимизация: пропустить значения, которые уже не подходят для i - j
                    break
                if abs(j - k) > y:  # оптимизация: пропустить значения, которые уже не подходят для j - k
                    break
                if abs(k - i) > z:  # оптимизация: пропустить значения, которые уже не подходят для k - i
                    break

result = solution(x, y, z)
for i in result:
    print(i)
