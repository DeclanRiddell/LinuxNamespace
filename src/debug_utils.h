#ifndef DEBUG_UTILS_H
#define DEBUG_UTILS_H
#include <stdio.h>
#define DBG_WRAP_DRIVER(x) printf("=\tStarting '%s'\n", #x); x; printf("=\tEnd of '%s'\n", #x)

#endif