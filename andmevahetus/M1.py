fail = open('tervitus.txt', 'r', encoding='utf-8')

sisu = fail.read()

print(sisu)

fail.close()