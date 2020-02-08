#include "element.h"
#include <assert.h>
#include <stdlib.h>

typedef struct Node Node;
typedef struct Node {
    Node *next;
    Node *prev;
    element val;
} Node;

void init_first(Node *n, element *el) {
    n->next = NULL;
    n->prev = NULL;
    n->val = *el;
}

typedef struct Deque {
    Node *head;
    Node *tail;
    unsigned size;
} Deque;

Deque *init() {
    Deque *q = (Deque*)malloc(sizeof(Deque));
    q->head = NULL;
    q->tail = NULL;
    q->size = 0;

    assert(q && "Error: Cannot allocate memory for queue!");
    return q;
}

void del(Deque *q) {
}

unsigned size(Deque *q) {
    return q->size;
}

element front(Deque *q) {
    return q->head->val;
}

element back(Deque *q) {
    return q->tail->val;
}

void push_back(Deque *q, element *el) {
    if(!q->head && !q->tail) {
        q->head = (Node*)malloc(sizeof(Node));
        q->tail = (Node*)malloc(sizeof(Node));
        assert(q->head && "Error: Cannot allocate memory for queue's element!");
        assert(q->tail && "Error: Cannot allocate memory for queue's element!");

        init_first(q->head, el);
        init_first(q->tail, el);
    } else {
        printf("HERE\n");
    }
}

static const struct _Deque {
    Deque *(*init)();
    void (*del)(Deque *q);

    unsigned (*size)(Deque *q);

    element (*front)(Deque *q);
    element (*back)(Deque *q);
    void (*push_back)(Deque *q, element *el);
} deque = {
    init,
    del,
    size,
    front,
    back,
    push_back,
};

