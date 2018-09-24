import random

f = open("words.txt", 'r')
block = f.read()
f.close()
words = block.split('\n')


f2 = open("def.txt", 'r', encoding='utf8')
block2 = f2.read()
f2.close()
defs = block2.split('~')

d = dict(zip(words, defs))

x = ""

while (x != "stop"):
    word, ans = random.choice(tuple(d.items()))
    print("\n")
    print(word)
    x = input("")
    print(ans)
    x = input('\nType "stop" to end program ')
