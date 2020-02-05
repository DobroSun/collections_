#ifndef SRC_ELEMENT_H
#define SRC_ELEMENT_H

typedef struct _Element {
    int data;
} element;

void dummy(element *val) {
    val->data = 0;
}

void init_element(element *val, int data) {
    val->data = data;
}
#endif
