CC=gcc
CFLAGS=-Wall -I./include/ -I.src/
DEPS=src/stack.h

run: clean test
	@./test

%.o: %.c $(DEPS)
	@$(CC) -c -o $@ $< $(CFLAGS)

test: test.o
	@$(CC) -o test test.o $(CFLAGS)

.PHONY: clean
clean:
	@rm -f *.o test
