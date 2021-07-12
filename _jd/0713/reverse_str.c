#include <stdio.h>
#include <string.h>

int main()
{

    char str[100] = "hello";
    int max_len = strlen(str)/sizeof(char);
    printf("%d\n", max_len);

    for(int j=max_len-1;j>=0;j--)
    {
        printf("char = %c\n", str[j]);

    }

    return 0;
}