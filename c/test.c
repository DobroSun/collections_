#include <stdio.h>
#include <stdlib.h>

#include "test/my_test.h"
#include "src/stack.h"

int main(int argc, char **argv) {
    Stack *st = stack.init(2);

    stack.push(st, 3);
    stack.back(st);
    stack.size(st);

    stack.push(st, 23);
    stack.back(st);
    stack.size(st);
    printf(green("Passed"));

    stack.del(st);
    return 0;
}
