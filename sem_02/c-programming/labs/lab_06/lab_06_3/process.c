#include "process.h"


int process(FILE *fsrc, FILE *fdst, char *f_in, char *f_out)
{
    int rc = 0;
    rc = check_file_in(&fsrc, f_in);

    if (!rc)
    {
        rc = check_file_out(&fdst, f_out);
        if (!rc)
        {
            output(fdst, solver(fsrc));
            fclose(fdst);
        }
        fclose(fsrc);
    }

    return rc;
}