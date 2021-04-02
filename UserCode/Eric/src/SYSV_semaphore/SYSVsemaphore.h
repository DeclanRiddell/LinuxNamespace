#ifndef SYSVSEMAPHORE_H
#define SYSVSEMAPHORE_H

#include <stdio.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/time.h>
#include <sys/sem.h>
#include <math.h>
#include <stdlib.h>
#include <debug_utils.h>


struct sembuf lock;
struct sembuf unlock;

int semaphore;

void* sysv_thread(void* arg);


#endif