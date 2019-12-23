#include "globals.h"

typedef struct Stack {
    int *arr;
    unsigned maxsize, top;
} Stack;


void _rewrite(Stack *st, size_t size) {
    for(unsigned i = 0; i < st->top; i++) {
        printf("Nothing for now\n");
    }
}


Stack *init(size_t size) {
    Stack *st = (Stack*)malloc(sizeof(Stack));
    st->arr = (int*)malloc(sizeof(size));
    st->maxsize = size;
    st->top = 0;
    return st;
}

void del(Stack *st) {
    free(st->arr);
    free(st);
}

unsigned maxsize(Stack *st) {
    return st->maxsize;
}

unsigned size(Stack *st) {
    printf("Size is: %i\n", st->top);
    return st->top;
}

void push(Stack *st, int value) {
    if(st->top > st->maxsize) {
        st->maxsize *= 10;
        _rewrite(st, st->maxsize);
    }
    if(st->top > st->maxsize) {
        printf("Error:\n");
        printf("Already on maxsize of stack.\n");
        return;
    }
    st->arr[st->top] = value;
    printf("Pushed is: %i\n", st->arr[st->top]);
    st->top++;
}

int back(Stack *st) {
    unsigned prev = st->top;
    prev--;
    printf("Back is: %i\n", st->arr[prev]);
    return st->arr[prev];
}

void remove_last(Stack *st) {
    st->top--;
    st->arr[st->top] = 0;
}

int pop(Stack *st) {
    int res = back(st);
    remove_last(st);
    return res;
}

static const struct _Stack {
    Stack *(*init)(size_t size);
    void (*del)(Stack *st);

    unsigned (*maxsize)(Stack *st); 
    unsigned (*size)(Stack *st); 

    void (*push)(Stack *st, int value);
    int (*back)(Stack *st);
    void (*remove_last)(Stack *st);
    int (*pop)(Stack *st);
} stack = {
    init,
    del,
    maxsize,
    size,
    push,
    back,
    remove_last,
    pop,
};
