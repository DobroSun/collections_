#include "element.h"
#include <assert.h>
#include <stdlib.h>

typedef struct Node Node;
typedef struct Node Deque_iterator;
typedef struct Node {
    Node *next;
    Node *prev;
    element val;
} Node;

void init_el(Node *n, element *el) {
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
    q->head = (Node*)malloc(sizeof(Node));
    q->tail = q->head;
    q->size = 0;

    assert(q && "Error: Cannot allocate memory for queue!");
    assert(q->head && "Error: Cannot allocate memory for queue's element!");
    return q;
}

void del(Deque *q) {
/*
    Node *tmp = q->head;
    while(tmp) {
        Node *cur = tmp;

        tmp = cur->next;
        free(cur);
    }
*/
}

unsigned size(Deque *q) {
    return q->size;
}

unsigned empty(Deque *q) {
    return (q->size)? 0: 1;
}

Node head(Deque *q) {
    return *(q->head);
}

Node tail(Deque *q) {
    return *(q->tail);
}

element front(Deque *q) {
    return q->head->val;
}

element back(Deque *q) {
    return q->tail->val;
}

void push_back(Deque *q, element *el) {
    if(!q->size) {
        init_el(q->head, el);
    } else {
        Node *pp = (Node*)malloc(sizeof(Node));
        Node *tmp = q->tail;

        q->tail = pp;
        init_el(q->tail, el);
        tmp->next = q->tail;
        q->tail->prev = tmp;
    }
    q->size++;
}

void push_front(Deque *q, element *el) {
    if(!q->size) {
        init_el(q->head, el);
    } else {
        Node *pp = (Node*)malloc(sizeof(Node));
        Node *tmp = q->head;

        assert(pp && "Error: Cannot allocate memory for queue's element");

        q->head = pp;
        init_el(q->head, el);
        tmp->prev = q->head;
        q->head->next = tmp;
    }
    q->size++;
}

element pop_front(Deque *q) {
    element res;
    if(!q->size) {
        dummy(&res);
    } else if(q->head == q->tail) {
        res = front(q);
        free(q->head);
    } else {
        res = front(q);
        Node *tmp = q->head->next;
        free(q->head);

        q->head = tmp;
        tmp->prev = NULL;
    }
    q->size--;
    return res;
}

element pop_back(Deque *q) {
    element res;
    if(!q->size) {
        dummy(&res);
    } else if(q->head == q->tail) {
        res = back(q);
        free(q->head);
    } else {
        res = back(q);
        Node *tmp = q->tail->prev;
        free(q->tail);

        q->tail = tmp;
        tmp->next = NULL;
    }
    q->size--;
    return res;
}

element *find(Deque *q, element val) {
    Node *cur = q->head;
    while(cur) {
        if(equals(&cur->val, &val)) {
            return &cur->val;
        }
        cur = cur->next;
    }
    return NULL;
}


static const struct _Deque {
    Deque *(*init)();
    void (*del)(Deque *q);

    unsigned (*size)(Deque *q);
    unsigned (*empty)(Deque *q);
    Node (*head)(Deque *q);
    Node (*tail)(Deque *q);

    element (*front)(Deque *q);
    element (*back)(Deque *q);
    void (*push_front)(Deque *q, element *el);
    void (*push_back)(Deque *q, element *el);
    element (*pop_front)(Deque *q);
    element (*pop_back)(Deque *q);

    element *(*find)(Deque *q, element val);
} deque = {
    init,
    del,
    size,
    empty,
    head,
    tail,
    front,
    back,
    push_front,
    push_back,
    pop_front,
    pop_back,
    find,
};

