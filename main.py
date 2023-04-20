s1 = 'даша лучший препод'
s2 = 'но я хочу спать'

#задание a
print(len(s1) * len(s2))

#задание b
print(s1, s2)

#задание c
print(s1, s2, sep=',\t')

#задание d
print(f"Hello, {s1}! Just wanted to say: '{s2}'")

#задание e
q = s1.split()
r = s2.split()
print(q[0], r[0])

#задание f
q = s1.split()
r = s2.split()
print(len(q))

#задание
print(s2.find(s1))