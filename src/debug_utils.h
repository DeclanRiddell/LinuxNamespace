#ifndef DEBUG_UTILS_H
#define DEBUG_UTILS_H
#include <stdio.h>
#define DBG_WRAP_DRIVER(x) printf("Starting '%s'\n", #x); x; printf("End of '%s'\n", #x)

#endif