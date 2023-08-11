#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check_file_in(FILE **f, char *fname)
{
    int rc = 0;
    *f = fopen(fname, "r");
    if (!(*f))
    {
        fprintf(stderr, "Could not open '%s' due to error: %s\n", fname, strerror(errno));
        rc = -2;
    }
    return rc;
}

int check_file_out(FILE **f, char *fname)
{
    int rc = 0;
    *f = fopen(fname, "w");
    if (!(*f))
    {
        fprintf(stderr, "Could not create '%s' due to error: %s\n", fname, strerror(errno));
        rc = -3;
    }
    return rc;
}

void usage(void)
{
    printf("main.exe <source file> <destination file>");
}