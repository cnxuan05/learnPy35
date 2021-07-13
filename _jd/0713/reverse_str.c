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

    printf("%d", a);

    return 0;
}