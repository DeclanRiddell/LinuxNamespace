#ifndef SYSVSEMAPHORE_DRIVER_H
#define SYSVSEMAPHORE_DRIVER_H

#include "SYSVsemaphore.h"
#include <sys/time.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int sysvsemaphore_execute(int argc, char* argv[]);

struct sembuf lock;
struct sembuf unlock;

#endif