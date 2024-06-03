#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
    char* filename = argv[1];
    FILE* file = fopen(filename,"rt");
    printf("EUID : %d \n", geteuid());
    printf("EGID : %d \n", getegid());
    printf("RUID : %d \n", getuid());
    printf("RGID : %d \n", getgid());
    char c;
    while((c=fgetc(file))!=EOF){
        printf("%c",c);
    }
    fclose(file);
    return 0;
}

