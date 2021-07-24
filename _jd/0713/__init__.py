''''

ssh root@192.168.1.22 "cd /opt/data/04/; fast-archive -c data --exclude=data/\*.pid" | fast-archiver -x
ssh root@192.168.1.26 "cd /opt/data/04/; fast-archive -c data --exclude=data/\*.pid" | fast-archiver -x

tar -cf - /opt/data/04 | ssh root@192.168.1.26 'tar -xvf - -C /opt/'



stack overflow
- K

heap G

scanf

gets

fgets
stdin

stdout

man 3 scanf

man 3 puts
add \r\n on end...

fputs(s, stdout);

strlen
valid str length , no '\0', exclude

reverse a chinese character list...

3*1

3*2

3*3

3*n

low-high
i len-i+1

3i-3
3i-2
3i-1

gbk
utf-8


strcat(a,b)

strncat
for str len error . stack overflow error...

sizeof
strlen
-1


strcmp
strncmp

memset(a,0 sizeof(a));

strncmp(a,'exit',4)
express len of obj string

strcpy(b, a)

sprintf(a,"a++++++",10)
express char list to ...

char *e = strstr(a, "345")
return point to the first str

strtok
char *p = srtok(buf, "@")

#include <string.h>
#include <stdio.h>

int main () {
   char str[80] = "This is - www.tutorialspoint.com - website";
   const char s[2] = "-";
   char *token;

   /* get the first token */
   token = strtok(str, s);

   /* walk through other tokens */
   while( token != NULL ) {
      printf( " %s\n", token );

      token = strtok(NULL, s);
   }

   return(0);
}


atoi

#include <time.h>
int t  = (int)time(NULL)
srand(t)

data  = rand()


'''