#include <stdio.h>
#include <stdlib.h>

#include "test/my_test.h"
#include "src/stack.h"

TEST(My_Case) {
    INIT();
    Stack *st = stack.init(10);

    ASSERT_EQ(stack.empty(st), 1);
    ASSERT_EQ(stack.size(st), 0);

    int i;
    for(i = 0; i < 302; i++) {
        element val;
        init_element(&val, i);


        stack.push(st, val);
        element get = stack.back(st);
        ASSERT_EQ(get.data, i);
    }
    ASSERT_EQ(stack.size(st), i);

    stack.del(st);
    return TEST_CASE_RESULT;
}

int main(int argc, char **argv) {
    RUN(My_Case);

    //printf("%i", check_literal(stack.empty(st)));
/*
    for(int i = 0; i < 302; i++) {
        stack.pop(st);
        stack.size(st);
    }
    printf(yellow("NEW MAXSIZE: ")"%i", stack.maxsize(st));
    printf("\n");
    printf(green("Passed")"\n");
*/
    //stack.del(st);
    return 0;
}
