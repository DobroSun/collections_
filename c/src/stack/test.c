#include "test/my_test.h"
#include "stack.h"

TEST(Stack_Case) {
    INIT();
    Stack *st = stack.init(10);

    ASSERT_EQ(stack.empty(st), 1);
    ASSERT_EQ(stack.size(st), 0);

    element val;
    init_element(&val, 2);
    element vv;
    init_element(&vv, 3);
    element vvv;
    init_element(&vvv, 4);

    // Push.
    stack.push(st, val);
    stack.push(st, vv);
    stack.push(st, vvv);
    ASSERT_EQ(stack.size(st), 3);
    ASSERT_EQ(st->arr[1].data, 3);

    // Iterator.
    Stack_iterator i;
    for(i = stack.begin(st); i < stack.end(st); i++/*stack.next(st)*/) {
        printf("%i <- given value\n", (*i).data);
    }

    // Search.
    element l;
    element ll;
    init_element(&l, 10);
    init_element(&ll, 4);
    ASSERT_EQ((stack.find(st, l) == stack.end(st)), 1);
    ASSERT_EQ(equals(stack.find(st, ll), &ll), 1);
    stack.del(st);

    return TEST_CASE_RESULT;
}

int main(int argc, char **argv) {
    RUN(Stack_Case);

    return 0;
}
