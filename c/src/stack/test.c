#include "test/my_test.h"
#include "stack.h"

TEST(Stack_Case) {
    INIT();
    Stack *st = stack.init(10);

    ASSERT_EQ(stack.empty(st), 1);
    ASSERT_EQ(stack.size(st), 0);

    int i;
    for(i = 0; i < 302; i++) {
        element val;
        init_element(&val, i);


        stack.push(st, &val);
        element get = stack.back(st);
        ASSERT_EQ(get.data, i);
    }
    ASSERT_EQ(stack.size(st), i);

    stack.del(st);

    return TEST_CASE_RESULT;
}

int main(int argc, char **argv) {
    RUN(Stack_Case);

    return 0;
}
