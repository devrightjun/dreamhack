// gcc -o no_canary canary.c -fno-stack-protector
// gcc -o canary canary.c

#include <unistd.h>

int main() {
    char buf[8];
    read(0, buf, 32);
    return 0;
}