#ifndef SYSVSEMAPHORE_DRIVER_H
#define SYSVSEMAPHORE_DRIVER_H

#include "SYSVsemaphore.h"
#include <sys/time.h>
#include <sys/errno.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <debug_utils.h>
#include <math.h>

int SYS_V_semaphore_execute();

double SYSVmin, SYSVmax, SYSVsum, SYSVmean, SYSVvariance, SYSVstandard_deviation;

#endif