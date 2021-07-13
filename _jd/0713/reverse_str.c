#include <stdio.h>
#include <string.h>

int main()
{

    unsigned char str[100] = "你好中文";
    int max_len = strlen(str)/sizeof(unsigned char);
    printf("%d\n", max_len);

    for(int j=max_len-1;j>=0;j--)
    {
        printf("char = %x\n", str[j]);

    }
    int a = 0xe4b0a0;

    //printf("%d\n", a);

    char b[3] = {0};
    fgets(b,sizeof(b)/sizeof(char),stdin);
    printf("%s\n", b);

    char x[] = "hello world";
    printf("%s\n", x);

    printf("1\n#\n");

    return 0;
}