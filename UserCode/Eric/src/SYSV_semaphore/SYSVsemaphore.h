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

#define SIZE_TIMES 65536*2
#define MIN_TIME_EXE 0.00001

float times[SIZE_TIMES]; //This array will hold the elapsed time of each pair of semop system calls

int count; //will count how many pairs of semop system calls are executed


#endif