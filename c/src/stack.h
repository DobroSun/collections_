#include "globals.h"
#include <assert.h>

typedef struct Stack {
    int *arr;
    unsigned maxsize, top;
} Stack;


void _rewrite(Stack *st, size_t size) {
    int *new_arr = (int*)malloc(sizeof(size));
    for(unsigned i = 0; i < st->top; i++) {
        new_arr[i] = st->arr[i];
        printf("COPIED TO NEW_ARR: %i, expected: %i", new_arr[i], st->arr[i]);
        printf("\n");
    }
    printf("ST->TOP: %i", st->top);
    printf("\n");

    st->arr = new_arr;
    free(new_arr);
}


Stack *init(size_t size) {
    Stack *st = (Stack*)malloc(sizeof(Stack));
    st->arr = (int*)malloc(sizeof(size));
    st->maxsize = size;
    st->top = 0;

    assert(st && "Error: Cannot allocate memory for stack!");
    assert(st->arr && "Error: Cannot allocate memory for stack!");
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

bool empty(Stack *st) {
    return (st->top == 0)? true: false;
}

void push(Stack *st, int value) {
    if(st->top >= st->maxsize) {
        st->maxsize *= 10;
        _rewrite(st, st->maxsize);
    }
    assert(st->top < st->maxsize && "Error: Top of stack is greater than maxsize!");

    st->arr[st->top] = value;
    printf("Pushed is: %i\n", st->arr[st->top]);
    st->top++;
}

int back(Stack *st) {
    if(empty(st)) {
        printf("Stack is empty!\n");
        return 0;
    }
    unsigned prev = st->top;

    printf("Back is: %i\n", st->arr[--prev]);
    return st->arr[prev];
}

void remove_last(Stack *st) {
    if(empty(st)) return;
    st->arr[--st->top] = 0;
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
    bool (*empty)(Stack *st); 

    void (*push)(Stack *st, int value);
    int (*back)(Stack *st);
    void (*remove_last)(Stack *st);
    int (*pop)(Stack *st);
} stack = {
    init,
    del,
    maxsize,
    size,
    empty,
    push,
    back,
    remove_last,
    pop,
};
