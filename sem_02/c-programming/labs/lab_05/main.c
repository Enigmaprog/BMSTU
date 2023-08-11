#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int maxN = 100;

int process(FILE *, FILE *, char *, char *);
void usage(void);
void input(FILE *, int *, int **);
void output(FILE *, const int);
int check_file_in(FILE **, char *);
int check_file_out(FILE **, char *);


int main(int argc, char **argv)
{
    FILE *fsrc, *fdst;
	int rc = 0;
	if (argc != 3)
    {
        usage();
        rc = -1;
    }
	else
	{	
		char *f_in = argv[1];
		char *f_out = argv[2];
		int rc = process(fsrc, fdst, f_in, f_out);
		
	}
    return rc;
}

void usage(void)
{
    printf("main.exe <source file> <destination file>");
}

void input(FILE *f, int *p_start, int **p_end)
{
    int *p_cur = p_start;
    int count = 0;
    while (1)
    {
        fscanf(f, "%d", p_cur);
        p_cur++;
        count++;
        if (feof(f))
            break;
        if (count >= 100)
        {
            printf("The size of array has exceeded limit. Input terminated.");
            break;
        }
    }
    *p_end = p_cur;
}

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

void output(FILE *f, const int res)
{
    fprintf(f, "Result: %d", res);
}

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