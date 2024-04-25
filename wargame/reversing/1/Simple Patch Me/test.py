from pwn import *
import subprocess

with ELF('./simple_patch_me') as e:
    e.asm(e.address+0x12a6, 'nop;'*5)
    e.save('./simple_patch_me_patched')

opt = subprocess.check_output("./simple_patch_me_patched")
print(opt.decode())