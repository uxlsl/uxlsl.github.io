
f = open('/tmp/hello1','w')
print(f)
f.write('hello')

f = open('/tmp/hello2','wb')
print(f)
f.write(b'hello')
