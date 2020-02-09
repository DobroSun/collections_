#include "element.h"
#include <assert.h>
#include <stdlib.h>

typedef element* Stack_iterator;
typedef struct Stack {
    element *arr;
    unsigned maxsize, top, iterator_counter;
} Stack;


void _rewrite(Stack *st, size_t size) {
    element *new_arr = (element*)malloc(sizeof(size));
    for(unsigned i = 0; i < st->top; i++) {
        new_arr[i] = st->arr[i];
    }
    st->arr = new_arr;
    free(new_arr);
}


Stack *init(size_t size) {
    Stack *st = (Stack*)malloc(sizeof(Stack));
    st->arr = (element*)malloc(size * sizeof(element));
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
    return st->top;
}

unsigned empty(Stack *st) {
    return (st->top == 0)? 1: 0;
}

void push(Stack *st, element val) {
    if(st->top >= st->maxsize) {
        st->maxsize *= 10;
        _rewrite(st, st->maxsize);
    }
    assert(st->top < st->maxsize && "Error: Top of stack is greater than maxsize!");

    st->arr[st->top] = val;
    st->top++;
}

element back(Stack *st) {
    if(empty(st)) {
        printf("Stack is empty!\n");
        element val; dummy(&val);

        return val;
    }
    unsigned prev = st->top;
    return st->arr[--prev];
}

void remove_last(Stack *st) {
    if(empty(st)) return;
    element val; dummy(&val);

    st->arr[--st->top] = val;
}

element pop(Stack *st) {
    element res = back(st);
    remove_last(st);
    return res;
}

element *begin(Stack *st) {
    st->iterator_counter = 0;
    return &st->arr[st->iterator_counter];
}

element *end(Stack *st) {
    return &st->arr[size(st)];
}

element *find(Stack *st, element val) {
    Stack_iterator i;
    for(i = begin(st); i < end(st); i++) {
        if(equals(i, &val)) {
            return i;
        }
    }
    return end(st);
}

void clear(Stack *st) {
    int decrease_count = 0;
    element tt;
    dummy(&tt);

    Stack_iterator i;
    for(i = begin(st); i < end(st); i++) {
        if(!equals(i, &tt)) {
            decrease_count++;
            *i = tt;
        }
    }
    st->top -= decrease_count;
}

static const struct _Stack {
    Stack *(*init)(size_t size);
    void (*del)(Stack *st);

    unsigned (*maxsize)(Stack *st); 
    unsigned (*size)(Stack *st); 
    unsigned (*empty)(Stack *st);

    void (*push)(Stack *st, element val);
    element (*back)(Stack *st);
    void (*remove_last)(Stack *st);
    element (*pop)(Stack *st);

    element *(*begin)(Stack *st);
    element *(*end)(Stack *st);
    element *(*find)(Stack *st, element val);
    void (*clear)(Stack *st);
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
    begin,
    end,
    find,
    clear,
};
