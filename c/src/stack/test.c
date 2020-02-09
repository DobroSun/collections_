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
    ASSERT_EQ(stack.back(st).data, 2);
    stack.push(st, vv);
    ASSERT_EQ(stack.back(st).data, 3);
    stack.push(st, vvv);
    ASSERT_EQ(stack.back(st).data, 4);
    ASSERT_EQ(stack.size(st), 3);
    ASSERT_EQ(st->arr[1].data, 3);

    // Iterator.
    Stack_iterator i;
    for(i = stack.begin(st); i < stack.end(st); i++) {
        printf("%i <- given value\n", i->data);
    }

    // Search.
    element l;
    element ll;
    init_element(&l, 10);
    init_element(&ll, 4);
    ASSERT_EQ((stack.find(st, l) == stack.end(st)), 1);
    ASSERT_EQ(equals(stack.find(st, ll), &ll), 1);

    ASSERT_EQ(stack.size(st), 3);
    ASSERT_EQ(stack.pop(st).data, 4);
    ASSERT_EQ(stack.size(st), 2);
    ASSERT_EQ(stack.pop(st).data, 3);
    ASSERT_EQ(stack.size(st), 1);
    ASSERT_EQ(stack.pop(st).data, 2);
    ASSERT_EQ(stack.size(st), 0);
    stack.del(st);



    Stack *s = stack.init(10);
    element bar;
    init_element(&bar, 2);
    element bb;
    init_element(&bb, 3);
    element bbb;
    init_element(&bbb, 4);
    stack.push(s, bar);
    stack.push(s, bb);
    stack.push(s, bbb);
    stack.push(s, vvv);

    ASSERT_EQ(stack.size(s), 4);
    Stack_iterator it;
    for(it = stack.begin(s); it < stack.end(s); it++) {
        printf("%i <- given value\n", it->data);
    }

    stack.clear(s);
    ASSERT_EQ(stack.size(s), 0);
    stack.del(s);
    return TEST_CASE_RESULT;
}

int main(int argc, char **argv) {
    RUN(Stack_Case);

    return 0;
}
