#include "test/my_test.h"
#include "deque.h"

TEST(Deque_Case) {
    INIT();
    Deque *q = deque.init();
    ASSERT_EQ(deque.size(q), 0);

    element val;
    init_element(&val, 2);
    deque.push_back(q, &val);
    element data_b = deque.back(q);
    element data_f = deque.front(q);
    ASSERT_EQ(data_b.data, 2);
    ASSERT_EQ(data_f.data, 2);

    deque.del(q);
    return TEST_CASE_RESULT;
};

int main(int argc, char **argv) {
    RUN(Deque_Case);
    return 0;
};
