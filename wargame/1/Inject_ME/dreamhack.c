// #include <stdio.h>
// #include <windows.h>

// int main() {
//     LoadLibrary("prob_rev.dll");
//     return 0;
// }

#include <windows.h>

int main() {
    HINSTANCE prob = LoadLibraryA("prob_rev.dll");
    return 0;
}