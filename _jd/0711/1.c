#include <stdio.h>
#include <stdlib.h>

int main(int argc,char *argv[])
{
    printf("pam num is %d\n",argc);

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int c = a*b;
    printf("a * b = %d\n", c);


}