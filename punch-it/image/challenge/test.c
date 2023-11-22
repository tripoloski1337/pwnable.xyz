#include <stdio.h>
#include <string.h>
void main(){
    int x = strlen("\x00");
    printf("%d\n", x);
}
