#ifndef DEBUG_UTILS_H
#define DEBUG_UTILS_H
#include <stdio.h>
//#ifdef DEBUG
#define DBG_WRAP_DRIVER(x) printf("=\tStarting '%s'\n", #x); x; printf("=\tEnd of '%s'\n", #x)
//#else 
//#define DBG_WRAP_DRIVER(x) x

#define ITERATION_COUNT 1024
#endif