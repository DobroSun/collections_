#include <string.h>

#define ANSI_COLOR_RED "\x1b[31m"
#define ANSI_COLOR_GREEN "\x1b[32m"
#define ANSI_COLOR_YELLOW  "\x1b[33m"
#define ANSI_COLOR_BLUE    "\x1b[34m"
#define ANSI_COLOR_MAGENTA "\x1b[35m"
#define ANSI_COLOR_CYAN    "\x1b[36m"
#define ANSI_COLOR_RESET "\x1b[0m"

#define cyan(A) ANSI_COLOR_CYAN A ANSI_COLOR_RESET
#define blue(A) ANSI_COLOR_BLUE A ANSI_COLOR_RESET
#define yellow(A) ANSI_COLOR_YELLOW A ANSI_COLOR_RESET
#define green(A) ANSI_COLOR_GREEN A ANSI_COLOR_RESET
#define red(A) ANSI_COLOR_RED A ANSI_COLOR_RESET

#define typename(A) _Generic((A), \
          _Bool: "_Bool",                      unsigned char: "unsigned char",          \
           char: "char",                         signed char: "signed char",            \
      short int: "short int",             unsigned short int: "unsigned short int",     \
            int: "int",                         unsigned int: "unsigned int",           \
       long int: "long int",               unsigned long int: "unsigned long int",      \
  long long int: "long long int",     unsigned long long int: "unsigned long long int", \
          float: "float",                             double: "double",                 \
    long double: "long double", \
         void *: "void *",                   unsigned char *: "unsigned char *", \
         char *: "char *",                     signed char *: "signed char *",            \
    short int *: "short int *",         unsigned short int *: "unsigned short int *",     \
          int *: "int *",                     unsigned int *: "unsigned int *",           \
     long int *: "long int *",           unsigned long int *: "unsigned long int *",      \
long long int *: "long long int *", unsigned long long int *: "unsigned long long int *", \
        float *: "float *",                         double *: "double *",                 \
  long double *: "long double *", \
        default: "other")

#define get_format(A) _Generic((A), \
          _Bool: "%d",                      unsigned char: "%u",          \
           char: "%i",                         signed char: "%i",            \
      short int: "%i",             unsigned short int: "%u",     \
            int: "%i",                         unsigned int: "%u",           \
       long int: "%i",               unsigned long int: "%u",      \
  long long int: "%i",     unsigned long long int: "%u", \
          float: "%f",                             double: "%f",                 \
    long double: "%f", \
         void *: "%p",                   unsigned char *: "%n", \
         char *: "%s",                     signed char *: "%n",            \
    short int *: "%n",         unsigned short int *: "%n",     \
          int *: "%n",                     unsigned int *: "%n",           \
     long int *: "%n",           unsigned long int *: "%n",      \
long long int *: "%n", unsigned long long int *: "%n", \
        float *: "%n",                         double *: "%n",                 \
  long double *: "%n", \
        default: "%n")

#define check_literal(A) (#A[0] == '"')? 1: 0
#define check_types(A, B) !strcmp(typename(A), typename(B))
            

#define TEST(A) int TestCase__##A(const char *A)

#define INIT() \
    int TEST_CASE_RESULT = 0; \
    int TEST_CASE_COUNTER = 0;

#define RETURN() \
    return TEST_CASE_RESULT;

#define RUN(A) \
    printf("Running %s\n", #A); \
    int TEST_CASE_RESULT = TestCase__##A(#A); \
    if(TEST_CASE_RESULT) printf(yellow("%s")" "green("Passed")"\n", #A); \
    else printf(yellow("%s")" "red("Failed")"\n", #A);


#define ASSERT_EQ(first, second) \
    TEST_CASE_COUNTER++; \
    printf(yellow("%i)")" "cyan("Checking if ") #first cyan(" is equal to ") #second"\n", TEST_CASE_COUNTER); \
    if(!check_types(first, second)) { \
        TEST_CASE_RESULT = 0; \
    } else { \
        TEST_CASE_RESULT = first == second; \
    } \
    if(TEST_CASE_RESULT) { \
        printf(green("[Passed]")"\n"); \
    } else { \
        char fmt[1024] = ""; \
        strcat(fmt, "Expected "); \
        strcat(fmt, get_format(first)); \
        strcat(fmt, " To be equal to "); \
        strcat(fmt, get_format(second)); \
\
        printf( \
            fmt, \
            first, second); \
        printf(red("[Failed]")"\n"); \
    }
