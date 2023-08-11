# Compiler
CC := gcc

# Compilation Options
CFLAGS := -std=c99 -Wall -Werror -pedantic

# Common object files
OBJS := check_IO.o IO.o process.o solver.o 

ifeq ($(mode), debug)
	# Debug build: add the generation of debugging information
	CFLAGS += -g3
endif

ifeq ($(mode), release)
	# Final assembly: exclude debugging information and statements (asserts)
	CFLAGS += -DNDEBUG -g0
endif
	
main: $(OBJS) main.o
	$(CC) -o $@ $^ 
	
test: $(OBJS) test.o
	$(CC) -o $@ $^
	
%.o : %.c *.h
	$(CC) $(CFLAGS) -c $<

clean:
	$(RM) *.o *.exe *.txt
	
