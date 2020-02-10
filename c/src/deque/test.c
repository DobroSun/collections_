#include "test/my_test.h"
#include "deque.h"

TEST(Deque_Case) {
    INIT();
    Deque *q = deque.init();
    ASSERT_EQ(deque.size(q), 0);

    element val;
    init_element(&val, 2);
    deque.push_back(q, &val);

    ASSERT_EQ(deque.front(q).data, 2);
    ASSERT_EQ(deque.back(q).data, 2);
    ASSERT_EQ(deque.size(q), 1);

    element vv;
    init_element(&vv, 3);
    deque.push_back(q, &vv);

    ASSERT_EQ(deque.front(q).data, 2);
    ASSERT_EQ(deque.back(q).data, 3);
    ASSERT_EQ(deque.size(q), 2);

    element vvv;
    init_element(&vvv, 4);
    deque.push_back(q, &vvv);

    ASSERT_EQ(deque.front(q).data, 2);
    ASSERT_EQ(deque.back(q).data, 4);
    ASSERT_EQ(deque.size(q), 3);


    ASSERT_EQ(deque.head(q).val.data, 2);
    ASSERT_EQ(deque.head(q).next->val.data, 3);
    ASSERT_EQ(deque.head(q).next->next->val.data, 4);

    ASSERT_EQ(deque.tail(q).val.data, 4);
    ASSERT_EQ(deque.tail(q).prev->val.data, 3);
    ASSERT_EQ(deque.tail(q).prev->prev->val.data, 2);

    element bv; dummy(&bv);
    ASSERT_EQ((deque.find(q, bv) == NULL), 1);
    ASSERT_EQ(equals(deque.find(q, vvv), &vvv), 1);


    element gg = deque.pop_front(q);
    element ggf = deque.pop_front(q);
    element ggff = deque.pop_front(q);

    ASSERT_EQ(gg.data, 2);
    ASSERT_EQ(ggf.data, 3);
    ASSERT_EQ(ggff.data, 4);

    ASSERT_EQ(deque.size(q), 0);
    ASSERT_EQ(deque.empty(q), 1);
    deque.del(q);



    Deque *qq = deque.init();

    element va;
    element vaa;
    init_element(&va, 2);
    init_element(&vaa, 3);
    deque.push_front(qq, &va);
    deque.push_front(qq, &vaa);

    ASSERT_EQ(deque.head(qq).val.data, 3);
    ASSERT_EQ(deque.head(qq).next->val.data, 2);

    ASSERT_EQ(deque.tail(qq).val.data, 2)
    ASSERT_EQ(deque.tail(qq).prev->val.data, 3)


    ASSERT_EQ(deque.pop_back(qq).data, 2);
    ASSERT_EQ(deque.pop_back(qq).data, 3);

    ASSERT_EQ(deque.size(qq), 0);
    ASSERT_EQ(deque.empty(qq), 1);

    deque.del(qq);
    return TEST_CASE_RESULT;
};

int main(int argc, char **argv) {
    RUN(Deque_Case);
    return 0;
};
