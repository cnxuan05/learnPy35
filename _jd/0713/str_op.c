#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{

    char a[100] = {0};
    char b[100] = {0};

    fgets(a,sizeof(a),stdin);
    fgets(b,sizeof(a),stdin);

    strcat(a,b);
    printf("a = %s\n", a);

    return 0;
}