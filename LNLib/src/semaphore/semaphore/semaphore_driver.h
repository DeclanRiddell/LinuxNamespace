#ifndef SEM_DRIVER_H
#define SEM_DRIVER_H

#include "Psemaphore.h"
#include <sys/time.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int psemaphore_execute(int argc, char* argv[]);

float min, max, sum, mean, variance, standard_deviation; 


#endif