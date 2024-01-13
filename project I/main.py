open_secrets = open('letter3.txt', 'r')
stroka = ''
for word in open_secrets.read().split():
    stroka += chr(int(word))
print(stroka)
