# Compiler
CC := gcc

# Compilation Options
CFLAGS := -std=c99 -Wall -Werror -pedantic

# Common object files
OBJS := main.o check_IO.o IO.o process.o

ifeq ($(mode), debug)
	# Debug build: add the generation of debugging information
	CFLAGS += -g3
endif

ifeq ($(mode), release)
	# Final assembly: exclude debugging information and statements (asserts)
	CFLAGS += -DNDEBUG -g0
endif

main.exe: $(OBJS)
	$(CC) -o $@ $^ 
	
*.o : *.c
	$(CC) $(CFLAGS) -c $<

clean:
	$(RM) *.o *.exe
	
