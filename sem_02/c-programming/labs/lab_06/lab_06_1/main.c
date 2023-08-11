#include <stdio.h>
#include <stdlib.h>

int process(FILE *, FILE *, char *, char *);
void usage(void);

int main(int argc, char **argv)
{
    int rc = 0;
    if (argc != 3)
    {
        usage();
        rc = -1;
    }
    else
    {
        FILE *fsrc = NULL, *fdst = NULL;
        char *f_in = argv[1];
        char *f_out = argv[2];
        rc = process(fsrc, fdst, f_in, f_out);
    }
    return rc;
}

