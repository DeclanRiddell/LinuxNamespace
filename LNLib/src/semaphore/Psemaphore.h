#ifndef PSEMAPHORE_H
#define PSEMAPHORE_H


#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <sys/time.h>
#include <math.h>



//This program willl use the POSIX implementation of semaphores



void* thread(void* arg);

#define SIZE_TIMES 65536

float times [SIZE_TIMES]; // This array will hold the elapsed time of each wait()/post() executed by the threads while looping

int count; //Will count how many wait()/post() are executed by the threads while looping




#endif