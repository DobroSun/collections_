.PHONY: clean run test

CC=gcc
CFLAGS=-Wall -I./../../include/ -I./../
DEPS=src/deque.h

run: clean test
	@./test

%.o: %.c $(DEPS)
	@$(CC) -c -o $@ $< $(CFLAGS)

test: test.o
	@$(CC) -o test test.o $(CFLAGS)


clean:
	@rm -f *.o test
