#include <stdio.h>
#include <stdlib.h>

#include "test/my_test.h"
#include "src/stack.h"

TEST(My_Case) {
    INIT();
    int *a = {2, 3, 4, 4};
    int b = 2;
    ASSERT_EQ(a, b);
    RETURN();
}

int main(int argc, char **argv) {
    RUN(My_Case);



/*  
    Stack *st = stack.init(2);

    for(int i = 0; i < 302; i++) {
        stack.push(st, i);
        stack.back(st);
        stack.size(st);
    }
    for(int i = 0; i < 302; i++) {
        stack.pop(st);
        stack.size(st);
    }
    printf(yellow("NEW MAXSIZE: ")"%i", stack.maxsize(st));
    printf("\n");
    printf(green("Passed")"\n");

    stack.del(st);
*/
    return 0;
}
