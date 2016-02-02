import subprocess

p = subprocess.Popen(['cat'],stdin=subprocess.PIPE)
print(p.stdin)
p = subprocess.Popen(['cat'],stdin=subprocess.PIPE,bufsize=1, universal_newlines=True)
print(p.stdin)
