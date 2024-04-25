from pwn import *


def main():
    # v7 = v6(rand_num) ^ 7d1c4b0a을 만족하는 v7가 플래그
    r = remote("host3.dreamhack.games", 13512)

    r.recvuntil(b"Random number: ")
    v6 = int(r.recvline()[:-1].decode(), 16)    # v6: Rando number
    s2 = int("a0b4c1d7"[::-1], 16)              # s2: 비교해야할 값
    v7 = v6 ^ s2

    r.sendlineafter(b"Input? ", str(v7).encode())
    r.recvuntil(b"Congrats!\n")

    print(r.recvline()[:-1].decode())


if __name__ == "__main__":
    main()