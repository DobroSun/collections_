#define FOO printf("Hello world");

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



#define TEST(A) int _A(const char *A)

#define INIT() \
    int res = 0; \
    int count = 1;

#define RETURN() \
    return res;

#define RUN(A) \
    printf("Running %s\n", A); \
    int res = _A(A); \
    if(res) printf(yellow("%s")" "green("Passed")"\n", A); \
    else printf(yellow("%s")" "red("Failed")"\n", A);


#define ASSERT_EQ(first, second) \
    res = (first == second)? 1: 0; \
    int *pfirst = &first; \
    int *psecond = &second; \
    char *a = ((char*)pfirst); \
    char *b = ((char*)psecond); \
    printf(yellow("%i)")" "cyan("Checking if %s is equal to %s\n"), count, a, b); \
    if(res) printf(green("[Passed]")"\n"); \
    else { \
        printf( \
            "Expected %s\n"\
            "To be equal to %s\n", \
            a, b); \
        printf(red("Failed")"\n"); \
   }
