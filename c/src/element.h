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

int equals(element *self, element *other) {
    if(other->data == self->data) {
        return 1;
    } else {
        return 0;
    }
}
#endif
