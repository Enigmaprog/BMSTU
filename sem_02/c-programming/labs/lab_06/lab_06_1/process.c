#include <stdio.h>

const int maxN = 100;

void input(FILE *, int *, int **);
void output(FILE *, const int);
int check_file_in(FILE **, char *);
int check_file_out(FILE **, char *);

int process(FILE *fsrc, FILE *fdst, char *f_in, char *f_out)
{
    int rc = 0;
	rc = check_file_in(&fsrc, f_in);
	
    if (!rc)
    {
        rc = check_file_out(&fdst, f_out);
		if (!rc)
		{
			int a[maxN];
			int *p_start = a, *p_end;
			input(fsrc, p_start, &p_end);

			int max = -99999, temp = 0;
			for (int *i = p_start, *j = p_end; i != p_end; i++)
			{
				j -= 1;
				if (i > j)
					break;
				temp = *i + *j;
				printf("temp = %d\n", temp);
				if (temp > max)
					max = temp;
			}
			output(fdst, max);
			fclose(fdst);
		}
		fclose(fsrc);
    }

    return rc;
}