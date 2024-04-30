from pwn import *

context.arch = 'amd64'

code = shellcraft.sh()
code = asm(code)
print(code)